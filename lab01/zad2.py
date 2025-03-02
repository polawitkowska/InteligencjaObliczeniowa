import random
import math
import numpy as np
import matplotlib.pyplot as plt

def count_d(angle):  # funkcja napisana przez chatgpt
    v = 50
    h = 100
    g = 9.81

    angle_radians = math.radians(angle)
    v_x = v * math.cos(angle_radians)
    v_y = v * math.sin(angle_radians)
    
    t_total = (v_y / g) + math.sqrt(2 * (h + (v_y**2) / (2 * g)) / g)

    t_values = np.linspace(0, t_total, num=100)

    d = v_x * t_total    
    x_values = v_x * t_values
    y_values = h + v_y * t_values - 0.5 * g * t_values**2

    return round(d, 1), x_values, y_values

def draw_trajectory(angle, x_values, y_values): # funkcja napisana przez chatgpt
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, label=f'Kąt {angle}°', color='b')
    plt.xlabel("Odległość (m)")
    plt.ylabel("Wysokość (m)")
    plt.title("Trajektoria pocisku")
    plt.legend()
    plt.grid()
    plt.savefig("./lab01/trajektoria.png")
    plt.show()

def main():
    target = random.randint(50, 340)
    print("Cel: ", target)
    attempts = 0

    while True:
        # Sprawdzamy czy podany kąt jest poprawny
        try:
            angle = int(input("Wprowadź kąt nachylenia (0-90): "))
            if angle < 0 or angle > 90:
                print("Podaj prawidłowy kąt nachylenia (0-90)")
                continue
        except ValueError:
            print("Nieprawidłowe dane. Jako kąt nachylenia podaj liczbę całkowitą w zakresie 0-90.")
            continue

        # Sprawdzamy czy wygraliśmy
        d, x_values, y_values = count_d(angle)
        if d >= target-5 and d <= target+5:
            attempts += 1
            print(f"Cel trafiony! łączna liczba prób: {attempts}.")
            draw_trajectory(angle, x_values, y_values)
            break
        else:
            attempts += 1
            print(f"Odległość: {d}. Cel nie został trafiony.")
            continue
        
main()
