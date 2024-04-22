import os


print("\n\nAntes de prosseguir, certifique que está usando a VENV adequada")

if input("Continuar? (y/n) ") == "y":
    print("\n\natualizando pip...")
    os.system('python.exe -m pip install --upgrade pip')

    print("\n\nInstalando dependencias...")
    os.system('pip install -r requirements.txt')

else:
    quit()