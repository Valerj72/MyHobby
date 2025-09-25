words = []

def load_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        file_text = f.read()
        for file_word in file_text.lower().split():
            if file_word.isalpha():
                words.append(file_word)


def main():
    print("Список команд")
    print("-------------")
    print("load file.txt - загрузить слова из файла")
    print("wordcount word - количество повторений слова в файле")
    print("clear-memory - очистка данных о словах")
    print("words - получить список загруженных слов")
    print("exit - выход из программы")
    while True:
        command = input("Введите команду: ")
        if "load" in command:
            file_name = command.split()[1]
            load_file(file_name)
            print(f"Файл {file_name} был загружен! Добавлено {len(words)} слов.")
        elif "wordcount" in command:
            word_count = command.split()[1]
            count = words.count(word_count)
            print(f"Количество повторений слова '{word_count}' в файле: {count}")
        elif command == "clear-memory":
            words.clear()
        elif command == "words":
            print(f"Список загруженных слов: {words}")
        elif command == "exit":
            print("Программа успешно завершена!")
            break


if __name__ == '__main__':
    main()
