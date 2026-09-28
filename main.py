# todo.py

tasks = []

def show_menu():
    print("\n--- Список задач ---")
    print("1. Добавить задачу лентяю")
    print("2. Показать задачи холопу")
    print("3. Удалить задачу")
    print("4. Выход")

while True:
    show_menu()
    choice = input("Выберите действие: ")

    if choice == '1':
        task = input("Введите текст задачи: ")
        tasks.append(task)
        print("Задача добавлена!")
    elif choice == '2':
        if not tasks:
            print("Список пуст.")
        else:
            print("\nВаши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == '3':
        if not tasks:
            print("Нечего удалять.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                num = int(input("Введите номер задачи для удаления: "))
                if 0 < num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Задача '{removed}' удалена.")
                else:
                    print("Неверный номер.")
            except ValueError:
                print("Пожалуйста, введите число.")
    elif choice == '4':
        print("Выход...")
        break
    else:
        print("Неверный ввод, попробуйте снова.")