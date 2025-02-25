# Poprosiłam Copilot GPT-4o o poprawę kodu w zad1.py
# O to kopia programu poprawionego przez Copilot:

from datetime import date
import math

def yp_count(t):
    return math.sin(((2 * math.pi) / 23) * t)

def ye_count(t):
    return math.sin(((2 * math.pi) / 28) * t)

def yi_count(t):
    return math.sin(((2 * math.pi) / 33) * t)

def main():
    current_date = date.today()

    name = input("Podaj swoje imię: ")
    
    while True:
        try:
            year = int(input("Podaj rok swojego urodzenia: "))
            month = int(input("Podaj miesiąc swojego urodzenia: "))
            day = int(input("Podaj dzień swojego urodzenia: "))
            birth_date = date(year, month, day)
            break
        except ValueError:
            print("Nieprawidłowa data. Spróbuj ponownie.")

    days_lived = (current_date - birth_date).days
    t = days_lived

    yp = yp_count(t)
    ye = ye_count(t)
    yi = yi_count(t)

    print(f"Witaj {name}! Dziś jest Twój {t} dzień życia. Twoja fizyczna fala wynosi {round(yp, 2)}, emocjonalna {round(ye, 2)}, a intelektualna {round(yi, 2)}.")

    if yp >= 0.5 or ye >= 0.5 or yi >= 0.5:
        print("Gratuluję wysokiego wyniku! Miłego dnia :)")
    elif yp <= -0.5 or ye <= -0.5 or yi <= -0.5:
        print("Wygląda na to, że masz dziś gorszy dzień :( Trzymaj się<3")
        if yp_count(t + 1) > yp or ye_count(t + 1) > ye or yi_count(t + 1) > yi:
            print("Nie martw się. Jutro będzie lepiej!")

if __name__ == "__main__":
    main()
