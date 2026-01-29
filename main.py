class Task:
    def __init__(self, description, deadline, stat):
        self.description = description
        self.deadline = deadline
        self.stat = stat


# ФУНКЦИЯ ДЛЯ ДОБАВЛЕНИЯ ЗАДАЧ
tasks = []  # сюда будем складывать все созданные задачи

def add_task(description, deadline, stat=False):
    task = Task(description, deadline, stat)  # создаём объект Task
    tasks.append(task)  # добавляем в список (append добавляет элемент в конец списка)
    return task


# ОТМЕТКА ЗАДАЧИ КАК ВЫПОЛНЕННОЙ
def mark_done(task_number):
    # task_number — номер задачи в списке tasks (начиная с 1, как человеку удобнее)
    tasks[task_number - 1].stat = True
    return tasks[task_number - 1]


# ВЫВОД ТЕКУЩИХ (НЕ ВЫПОЛНЕННЫХ) ЗАДАЧ
def show_current_tasks():
    # оставляем только те задачи, у которых stat == False (фильтрация через if в цикле/списке) [web:32]
    for i, task in enumerate(tasks, start=1):  # enumerate даёт и номер, и объект задачи [web:36]
        if task.stat == False:
            print(f"{i}. {task.description} (до {task.deadline})")


add_task("Сдать отчет", "2026-02-10", False)
add_task("Купить билеты", "2026-01-30", True)

show_current_tasks()      # покажет только невыполненные
mark_done(1)              # отметим 1-ю задачу выполненной
show_current_tasks()      # теперь список невыполненных изменится
