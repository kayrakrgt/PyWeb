import requests , colorama , os
from colorama import Fore , init


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
      aranacak = url+"/"+files+"."+uzanti
      getting = requests.get(url=aranacak)
      posting = requests.post(url=aranacak)
      if (posting.status_code == 200 or getting.status_code == 200):
        print(Fore.GREEN + aranacak)
      elif (posting.status_code == 404 or getting.status_code == 404):
        print(Fore.RED + aranacak)
   else:
    print("Girdiğiniz PATH yanlış veya böyle bir dosya bulunmuyor!")
else:
  print(Fore.RED + "Site bulunamadı!")

