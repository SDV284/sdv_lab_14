import numpy as np
import matplotlib.pyplot as plt

def calculate_function(x):
    # Обчислення функції Y(x)=5*sin(10*x)*sin(3*x)/(x^x)
    return 5 * np.sin(10*x) * np.sin(3*x) / (x**x)

def plot_function():
    # Створюємо масив значень x
    # Використовуємо невеликий зсув від 0, щоб уникнути ділення на 0
    x = np.linspace(0.1, 8, 1000)
    # Обчислюємо значення функції
    y = calculate_function(x)
    # Створюємо графік
    plt.figure(figsize=(12, 6))
    # Будуємо графік з заданими параметрами
    plt.plot(x, y, 
             label='Y(x) = 5*sin(10x)*sin(3x)/x^x',
             color='blue',
             linewidth=2,
             linestyle='-'
    )
    # Налаштування графіка
    plt.title('Графік функції Y(x) = 5*sin(10x)*sin(3x)/x^x', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('Y(x)', fontsize=12)
    # Додаємо сітку
    plt.grid(True, linestyle='--', alpha=0.7)
    # Додаємо легенду
    plt.legend(fontsize=10)
    # Встановлюємо межі осей для кращого відображення
    plt.xlim(0, 8)
    plt.ylim(-8, 6)
    # Додаємо осі x та y через центр
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    # Налаштовуємо відступи
    plt.tight_layout()
    # Показуємо графік
    plt.show()

if __name__ == "__main__":
    plot_function()