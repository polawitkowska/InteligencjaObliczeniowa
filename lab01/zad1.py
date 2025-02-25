from datetime import date
import math

def yp_count(t):
    yp = math.sin(((2*math.pi)/23)*t)
    return yp

def ye_count(t):
    ye = math.sin(((2*math.pi)/28)*t)
    return ye

def yi_count(t):
    yi = math.sin(((2*math.pi)/33)*t)
    return yi


def main():
    current_date = date.today()

    name = input("Podaj swoje imię: ")
    year = input("Podaj rok swojego urodzenia: ")
    month = input("Podaj miesiąc swojego urodzenia: ")
    day = input("Podaj dzień swojego urodzenia: ")

    birth_date = date(int(year), int(month), int(day))

    days_lived = current_date - birth_date
    t = days_lived.days

    yp = yp_count(t)
    ye = ye_count(t)
    yi = yi_count(t)

    print(f"Witaj {name}! Dziś jest Twój {t} dzień życia. Twoja fizyczna fala wynosi {round(yp, 2)}, emocjonalna {round(ye, 2)}, a intelektualna {round(yi, 2)}.")

    if yp >= 0.5 or ye >= 0.5 or yi >= 0.5:
        print("Gratuluję wysokiego wyniku! Miłego dnia :)")
    elif yp <= -0.5 or ye <= -0.5 or yi <= -0.5:
        print("Wygląda na to, że masz dziś gorszy dzień :( Trzymaj się<3")
        if yp_count(t+1) > yp or ye_count(t+1) > ye or yi_count(t+1) > yi:
            print("Nie martw się. Jutro będzie lepiej!")
        
main()

# Nad pisaniem programu spędziłam mniej więcej 30 minut
