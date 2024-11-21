import json
import matplotlib.pyplot as plt

def read_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def create_price_categories(cars):
    # Створюємо цінові категорії
    categories = {
        '0-10k': 0,
        '10k-20k': 0,
        '20k-30k': 0,
        '30k-40k': 0,
        '40k+': 0
    }
    
    # Розподіляємо автомобілі за категоріями
    for car in cars:
        price = car['price']
        if price < 10000:
            categories['0-10k'] += 1
        elif price < 20000:
            categories['10k-20k'] += 1
        elif price < 30000:
            categories['20k-30k'] += 1
        elif price < 40000:
            categories['30k-40k'] += 1
        else:
            categories['40k+'] += 1
    
    return categories

def create_pie_chart(categories):
    # Створюємо кругову діаграму
    plt.figure(figsize=(10, 8))
    
    # Дані для діаграми
    sizes = list(categories.values())
    labels = list(categories.keys())
    
    # Кольори для секторів
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
    
    # Відступ для виділення секторів
    explode = [0.05] * len(categories)
    
    # Створюємо діаграму
    plt.pie(sizes, 
           explode=explode,
           labels=labels,
           colors=colors,
           autopct='%1.1f%%',  # Показувати відсотки з одним знаком після коми
           shadow=True,
           startangle=90)
    
    plt.title('Розподіл автомобілів за ціновими категоріями')
    plt.axis('equal')  # Робимо діаграму круглою
    
    # Додаємо легенду
    plt.legend(labels, 
              title="Цінові категорії (USD)",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.show()

def main():
    # Зчитуємо дані з файлу
    data = read_json_file('cars.json')
    
    # Створюємо категорії
    categories = create_price_categories(data['cars'])
    
    # Створюємо кругову діаграму
    create_pie_chart(categories)

if __name__ == "__main__":
    main()