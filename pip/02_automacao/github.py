import pyautogui as auto
import time



def main():
    # auto.PAUSE = 1
    # auto.hotkey("ctrl","j")
    # auto.press("enter")
    # auto.write("cd..")
    # auto.press("enter")

    auto.press("git config --global --unset-all usert.nome")
    auto.press("enter")
    auto.press("git config --global --unset-all usert.email")
    auto.press("enter")

    auto.write('git config --global user.name "amos-silva"')
    auto.press("enter")
    auto.write('git config --global user.email "amosdasilva86@gmail.com"')
    auto.press("enter")

    auto.write("git status")
    auto.press("enter")
    auto.write("git add .")
    auto.press("enter")

    msg = input("aula do Dia: ")
    auto.write(f"git commit -m {msg}")
    auto.press("enter")
    
    auto.write("git push")
    auto.press("enter")  

if __name__ == "__main__":
    main()
