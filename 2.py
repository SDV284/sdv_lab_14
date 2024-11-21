import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    # Читаємо CSV файл
    df = pd.read_csv(filename)
    
    # Відбираємо тільки потрібні стовпці
    years = [col for col in df.columns if 'YR' in col]
    
    # Перетворюємо дані у більш зручний формат
    data = {}
    for _, row in df.iterrows():
        if pd.notna(row['Country Name']):  # Перевіряємо, чи не пустий рядок
            country_data = {}
            for year in years:
                try:
                    # Конвертуємо значення в float, ігноруючи '..' та пусті значення
                    value = row[year]
                    if pd.notna(value) and value != '..':
                        country_data[int(year.split('[YR')[1][:4])] = float(value)
                except (ValueError, TypeError):
                    continue
            if country_data:  # Додаємо країну тільки якщо є дані
                data[row['Country Name']] = country_data
    
    return data

def plot_comparison(data):
    plt.figure(figsize=(12, 6))
    
    # Побудова графіків для обох країн
    for country in data.keys():
        years = list(data[country].keys())
        values = list(data[country].values())
        plt.plot(years, values, marker='o', label=country)
    
    plt.xlabel('Рік')
    plt.ylabel('Кількість дітей поза школою')
    plt.title('Динаміка кількості дітей поза школою')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_bar_chart(data, country):
    if country not in data:
        print(f"Країна '{country}' відсутня в даних")
        return
    
    # Створюємо стовпчасту діаграму
    plt.figure(figsize=(10, 5))
    years = list(data[country].keys())
    values = list(data[country].values())
    
    plt.bar(years, values)
    plt.xlabel('Рік')
    plt.ylabel('Кількість дітей поза школою')
    plt.title(f'Кількість дітей поза школою: {country}')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()

def main():
    # Зчитуємо дані
    data = read_data('data.csv')
    
    # Будуємо графік порівняння для обох країн
    plot_comparison(data)
    
    # Виводимо список доступних країн
    print("\nДоступні країни:")
    print(", ".join(data.keys()))
    
    # Запитуємо користувача про країну для побудови стовпчастої діаграми
    while True:
        country = input("\nВведіть назву країни для побудови стовпчастої діаграми (або 'exit' для виходу): ")
        if country.lower() == 'exit':
            break
        plot_bar_chart(data, country)

if __name__ == "__main__":
    main()