class Task:
    def __init__(self, description, deadline, stat):
        self.description = description
        self.deadline = deadline
        self.stat = stat

# Список для хранения всех задач — раздел 2 "Коллекции (списки)"
tasks_list = []

# Функция для добавления новой задачи
def add_task(description, deadline):
    new_task = Task(description, deadline, False)  # Создание объекта — раздел "Классы и объекты"
    tasks_list.append(new_task)  # Добавление в список — раздел 2 "Коллекции"
    print(f"Задача '{description}' добавлена!")  # F-строка — раздел 1

# Функция для отметки задачи как выполненной
def mark_task_complete(index):
    task = tasks_list[index]  # Получаем задачу из списка — раздел 2 "Коллекции (списки)"
    task.stat = True  # Изменение атрибута объекта — раздел "Классы и объекты"
    print(f"Задача '{task.description}' выполнена!")  # F-строка — раздел 1


# Функция для вывода невыполненных задач
def show_current_tasks():
    print("\n=== Текущие задачи ===")  # Вывод — раздел 1
    for task in tasks_list:  # Цикл for для перебора списка — раздел 2
        if task.stat == False:  # Условный оператор if — раздел 3
            print(f"{task.description} (Срок: {task.deadline})")  # F-строка — раздел 1

# Пример использования:
add_task("Выучить Python", "2026-02-15")
add_task("Сделать домашнее задание", "2026-01-30")
add_task("Прочитать книгу", "2026-03-01")

show_current_tasks()
mark_task_complete(0)
show_current_tasks()
