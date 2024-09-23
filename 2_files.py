"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        filename = 'referat2.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content + '\n')
            #f.write('\n')

        len_str = str(len(content))
        with open(filename, 'a', encoding='utf-8', newline='\n') as f:
            f.write(len_str + '\n')
            
        number_of_word = str(len(content.split(' ')))
        with open(filename, 'a', encoding='utf-8', newline='\n') as f:
            f.write(number_of_word + '\n')
           
        change = content.replace('.', '!')
        with open(filename, 'a', encoding='utf-8', newline='\n') as f:
            f.write(change)
    
    
    
    

if __name__ == "__main__":
    main()
