# zadanie 2 zmodyfikowane przez copilota
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Stałe
V = 50
H = 100
G = 9.81

def count_d(angle):
    """
    Oblicza odległość, wartości x i y dla danego kąta.
    
    Parameters:
    angle (int): Kąt nachylenia w stopniach
    
    Returns:
    tuple: Odległość, wartości x i y
    """
    angle_radians = math.radians(angle)
    v_x = V * math.cos(angle_radians)
    v_y = V * math.sin(angle_radians)
    
    t_total = (v_y / G) + math.sqrt(2 * (H + (v_y**2) / (2 * G)) / G)
    t_values = np.linspace(0, t_total, num=100)

    d = v_x * t_total    
    x_values = v_x * t_values
    y_values = H + v_y * t_values - 0.5 * G * t_values**2

    return round(d, 1), x_values, y_values

def draw_trajectory(angle, x_values, y_values):
    """
    Rysuje trajektorię pocisku.
    
    Parameters:
    angle (int): Kąt nachylenia w stopniach
    x_values (array): Wartości x
    y_values (array): Wartości y
    """
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, label=f'Kąt {angle}°', color='b')
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.title("Trajektoria pocisku")
    plt.legend()
    plt.grid()
    plt.savefig("./lab01/trajektoria.png")
    plt.show()

def get_angle():
    """
    Pobiera kąt nachylenia od użytkownika.
    
    Returns:
    int: Kąt nachylenia
    """
    while True:
        try:
            angle = int(input("Wprowadź kąt nachylenia (0-90): "))
            if 0 <= angle <= 90:
                return angle
            else:
                print("Podaj prawidłowy kąt nachylenia (0-90)")
        except ValueError:
            print("Nieprawidłowe dane. Jako kąt nachylenia podaj liczbę całkowitą w zakresie 0-90.")

def main():
    target = random.randint(50, 340)
    print("Cel: ", target)
    attempts = 0

    while True:
        angle = get_angle()
        d, x_values, y_values = count_d(angle)
        attempts += 1

        if target - 5 <= d <= target + 5:
            print(f"Cel trafiony! Łączna liczba prób: {attempts}.")
            draw_trajectory(angle, x_values, y_values)
            break
        else:
            print(f"Odległość: {d}. Cel nie został trafiony.")

if __name__ == "__main__":
    main()