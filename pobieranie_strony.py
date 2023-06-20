import urllib.request
import os

dzie_zainstalowac = r"C:\Users\MójKomputer\Desktop"

name = input("Podaj pod jaką nazwą zpisać plik: ")
link = input("Podaj link do strony, którą chcesz zapisać: ")

strony = [{'name': name, 'url': link}]

for page in strony:

    try:
        file_name = f"{page['name']}.html"
        path = os.path.join(dzie_zainstalowac, file_name)
        print(f"Pobieram {page['url']} --> {file_name}")

        urllib.request.urlretrieve(page["url"], path)
        print("...Zrobione!")
    except:
        print("Coś poszło nie tak...")
        print("Sprawdź czy podałeś dory link do strony")
        break

else:
    print("Strona pobrana!!!")

