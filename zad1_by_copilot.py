import math
from datetime import datetime, timedelta

def calculate_biorhythms(days_lived):
    yp = math.sin((2 * math.pi / 23) * days_lived)
    ye = math.sin((2 * math.pi / 28) * days_lived)
    yi = math.sin((2 * math.pi / 33) * days_lived)
    return yp, ye, yi

def main():
    # Pobieranie danych od użytkownika
    name = input("Podaj swoje imię: ")
    year_of_birth = int(input("Podaj rok urodzenia: "))
    month_of_birth = int(input("Podaj miesiąc urodzenia: "))
    day_of_birth = int(input("Podaj dzień urodzenia: "))

    # Obliczanie ilości przeżytych dni
    birth_date = datetime(year_of_birth, month_of_birth, day_of_birth)
    today = datetime.today()
    days_lived = (today - birth_date).days

    # Obliczanie biorytmów
    yp, ye, yi = calculate_biorhythms(days_lived)
    yp_next, ye_next, yi_next = calculate_biorhythms(days_lived + 1)

    # Wyświetlanie wyników
    print(f"\nWitaj, {name}!")
    print(f"Dzisiaj jest {days_lived}-ty dzień Twojego życia.")
    print(f"Twój fizyczny biorytm: {yp:.2f}")
    print(f"Twój emocjonalny biorytm: {ye:.2f}")
    print(f"Twój intelektualny biorytm: {yi:.2f}")

    # Sprawdzanie wyników biorytmów
    if yp > 0.5:
        print("Gratulacje! Masz wysoki fizyczny biorytm.")
    elif yp < -0.5:
        print("Twój fizyczny biorytm jest niski.")
        if yp_next > yp:
            print("Nie martw się. Jutro będzie lepiej!")

    if ye > 0.5:
        print("Gratulacje! Masz wysoki emocjonalny biorytm.")
    elif ye < -0.5:
        print("Twój emocjonalny biorytm jest niski.")
        if ye_next > ye:
            print("Nie martw się. Jutro będzie lepiej!")

    if yi > 0.5:
        print("Gratulacje! Masz wysoki intelektualny biorytm.")
    elif yi < -0.5:
        print("Twój intelektualny biorytm jest niski.")
        if yi_next > yi:
            print("Nie martw się. Jutro będzie lepiej!")

if __name__ == "__main__":
    main()

# Zrobienie całego zadania z Copilotem zajęło mi 18 minut, krócej niż zrobienie go samodzielnie.