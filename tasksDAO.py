from dbBroker import dbBroker

class tasksDAO:

    def getAll(self):
        query = 'SELECT * FROM tasks;'   
        return dbBroker().query(query)

    def get(self, task_id):
        query = f"SELECT * FROM tasks WHERE id={task_id};"
        return dbBroker().query(query)

    def set(self, priority, task):
        query = f"INSERT INTO tasks (priority, task) VALUES ('{priority}', '{task}');"
        dbBroker().execute(query)

    def update(self, task_id, priority, task):
        query = f"UPDATE tasks SET priority='{priority}', task='{task}' WHERE id='{task_id}';"
        dbBroker().execute(query)

    def delete(self, task_id):
        query = f"DELETE FROM tasks WHERE id={task_id};"
        dbBroker().execute(query)

    def deleteAll(self):
        query = f"DELETE FROM tasks;"
        dbBroker().execute(query)