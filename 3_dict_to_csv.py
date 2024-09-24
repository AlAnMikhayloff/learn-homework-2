"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    import csv
    workers = [
               {'name': 'Ben', 'age': '25', 'job': 'engineer', 'hobby': 'drawing'}, 
               {'name': 'Steve', 'age': '36', 'job': 'programmer', 'hobby': 'diving'},
               {'name': 'Rubby', 'age': '22', 'job': 'florist', 'hobby': 'classical music'},
               {'name': 'Louis', 'age': '52', 'job': 'economist', 'hobby': 'rock music'},
               {'name': 'Joe', 'age': '62', 'job': 'musician', 'hobby': 'washing dishes'}
                ]
    
    with open('neighbours.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job', 'hobby']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in workers:
            writer.writerow(user)


if __name__ == "__main__":
    main()
