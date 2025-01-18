import requests, colorama, os
from colorama import Fore, init

init()

banner = """


 /$$$$$$$            /$$      /$$           /$$      
| $$__  $$          | $$  /$ | $$          | $$      
| $$  \ $$ /$$   /$$| $$ /$$$| $$  /$$$$$$ | $$$$$$$ 
| $$$$$$$/| $$  | $$| $$/$$ $$ $$ /$$__  $$| $$__  $$
| $$____/ | $$  | $$| $$$$_  $$$$| $$$$$$$$| $$  \ $$
| $$      | $$  | $$| $$$/ \  $$$| $$_____/| $$  | $$
| $$      |  $$$$$$$| $$/   \  $$|  $$$$$$$| $$$$$$$/
|__/       \____  $$|__/     \__/ \_______/|_______/ 
           /$$  | $$                                 
          |  $$$$$$/                                 
           \______/                                  



"""

print(Fore.RED + banner)
print(Fore.WHITE)

url = input("Lütfen URL'yi giriniz:")
testing = requests.get(url=url)
testing2 = requests.post(url=url)
if (testing.status_code == 200 or testing2.status_code == 200):
    dosya = input("Lütfen wordlist dosya yolunuzu giriniz:")
    if os.path.exists(dosya):
        uzanti = input("Lütfen aradığınız dosya uzantısını yazınız(örnek: html,php,js,png,jpg)>>>")
        print("İşlem başlatılıyor...")
        with open(dosya, "r") as file:
            for files in file:
                files = files.strip()
                if files:  
                    aranacak = url + "/" + files + "." + uzanti
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
                        "Connection": "keep-alive",
                        "Upgrade-Insecure-Requests": "1",
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
                    }
                    getting = requests.get(url=aranacak, allow_redirects=True, headers=headers)
                    posting = requests.post(url=aranacak, allow_redirects=True, headers=headers)
                    if (getting.status_code == 200 or posting.status_code == 200):
                        print(Fore.GREEN + aranacak)
                    elif (getting.status_code == 404 or posting.status_code == 404):
                        print(Fore.RED + aranacak)
    else:
        print("Girdiğiniz PATH yanlış veya böyle bir dosya bulunmuyor!")
else:
    print(Fore.RED + "Site bulunamadı!")
