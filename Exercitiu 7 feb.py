
# Scrieti o clasa TaskManager, care stocheaza o lista de task-uri in ea, si care are mai multe functii pentru management-ul task-urilor

# Puteti folosi un array simplu [] ca o variabila in clasa, pentru a stoca task-urile.
# Un task este un dictionar care contine urmatoarele informatii:
# { description: "test description", done: False }
# description este descrierea task-ului
# done, care poate fi True sau False, este starea unui task, daca a fost completata inca, sau nu.

# Creati urmatoarele functii:
# .add_task(task), care adauga un task in lista de task-uri, in aceasta clasa
# .remove_task(task_description), care sterge un task din lista
# .mark_as_done(task_description), care gaseste un task dupa description, si ii schimba proprietatea "done" din False in True
# .get_pending_tasks(), care returneaza o lista de task-uri care nu au fost copmletate, deci care au proprietatea "done" ca fiind False.

# Exemplu cod:

# manager = TaskManager()
# manager.add_task({"description": "task 1 to be done", "done": False})
# manager.add_task({"description": "t2 task", "done": False})
# manager.add_task({"description": "t3333 task", "done": False})
#
# manager.remove_task("task 1 to be done")
# manager.mark_as_done("t2 task")
# manager.get_pending_tasks() -> [{"description": "t3333 task", "done": False}]

class TaskManager:
    def __init__(self):
        self.task = []

    def remove_task(self, description1):
        for task in self.task:
            if task["description"] != description1:
                self.task.remove(task)

    def add_task(self, task):
        self.task.append(task)

    def mark_as_done(self, description1):
        for task in self.task:
            if task["description"] == description1:
                task["done"] = True

    def get_pending_tasks(self):
        pending_tasks = []
        for task in self.task:
            if task["done"]:
                pending_tasks.append(task)
        return pending_tasks

        self.task.get_pending_tasks(description1)

manager = TaskManager()
manager.add_task({"description": "task 1 to be done", "done": False})
manager.add_task({"description": "t2 task", "done": False})
manager.add_task({"description": "t3333 task", "done": False})

manager.remove_task("task 1 to be done")
manager.mark_as_done("t2 task")
manager.get_pending_tasks()


print(manager.task)
