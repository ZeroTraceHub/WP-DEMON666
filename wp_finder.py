import requests
from bs4 import BeautifulSoup

def find_wp_sites(dork):
    url = f"https://www.google.com/search?q={dork}&num=100"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    
    wp_sites = []
    for link in links:
        if 'wordpress' in link['href']:
            wp_sites.append(link['href'])

    return wp_sites

if __name__ == "__main__":
    dork = input("Enter Google Dork to find WordPress sites: ")
    sites = find_wp_sites(dork)
    if sites:
        print("\n[+] WordPress sites found:")
        for site in sites:
            print(site)
    else:
        print("[-] No WordPress sites found.")