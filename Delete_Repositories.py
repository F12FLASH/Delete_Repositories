import requests
import time
from getpass import getpass

def delete_github_repos():
    username = input("Nhập username GitHub của bạn: ")
    token = getpass("Nhập GitHub Personal Access Token (có quyền repo hoặc admin:org): ")
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    print("\n🔍 Đang lấy danh sách repositories...")
    try:
        repos = []
        page = 1
        while True:
            repos_url = f"https://api.github.com/user/repos?type=all&per_page=100&page={page}"
            response = requests.get(repos_url, headers=headers)
            response.raise_for_status()
            new_repos = response.json()
            if not new_repos:
                break
            repos.extend(new_repos)
            page += 1
        
        if not repos:
            print("❌ Không tìm thấy repository nào.")
            return
            
        print("\n📋 Danh sách repositories:")
        for i, repo in enumerate(repos, 1):
            print(f"{i}. {repo['full_name']} (Owner: {repo['owner']['type']})")
            
        to_delete = input("\n⌨️ Nhập số thứ tự hoặc tên repositories muốn xóa (cách nhau bằng dấu phẩy, hoặc 'all'): ")
        
        delete_list = []
        if to_delete.lower() == 'all':
            delete_list = repos
            print(f"\n⚠️ Bạn đã chọn xóa TẤT CẢ {len(delete_list)} repositories!")
        else:
            selections = to_delete.split(',')
            for sel in selections:
                sel = sel.strip()
                if sel.isdigit():
                    index = int(sel) - 1
                    if 0 <= index < len(repos):
                        delete_list.append(repos[index])
                else:
                    found = [r for r in repos if sel.lower() in r['full_name'].lower()]
                    if found:
                        delete_list.extend(found)
            
            if not delete_list:
                print("❌ Không có repository nào được chọn.")
                return
                
            print(f"\n⚠️ Bạn đã chọn xóa {len(delete_list)} repositories:")
            for repo in delete_list:
                print(f"- {repo['full_name']} (Owner: {repo['owner']['type']})")
        
        confirm = input("\n❓ Bạn có CHẮC CHẮN muốn xóa? (y/n): ")
        if confirm.lower() != 'y':
            print("🚫 Hủy thao tác.")
            return
            
        print("\n🗑️ Đang xóa...")
        success_count = 0
        for repo in delete_list:
            try:
                delete_url = f"https://api.github.com/repos/{repo['full_name']}"
                del_response = requests.delete(delete_url, headers=headers)
                del_response.raise_for_status()
                print(f"✅ Đã xóa: {repo['full_name']}")
                success_count += 1
                time.sleep(1)
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 403:
                    print(f"❌ Lỗi 403: Token không có quyền xóa {repo['full_name']} (Kiểm tra quyền repo/admin:org)")
                else:
                    print(f"❌ Lỗi {e.response.status_code}: {e.response.text}")
            except Exception as e:
                print(f"❌ Lỗi không xác định: {str(e)}")
        
        print(f"\n🎉 Hoàn thành! Đã xóa {success_count}/{len(delete_list)} repositories.")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Lỗi kết nối: {str(e)}")

if __name__ == "__main__":
    delete_github_repos()