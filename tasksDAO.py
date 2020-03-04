from dbBroker import dbBroker

class tasksDAO:

    def getAll(self):
        getAll_query = 'SELECT * FROM tasks;'   
        return dbBroker().query(getAll_query)

    def get(self, task_id):
        getTask_query = f"SELECT * FROM tasks WHERE id={task_id};"
        return dbBroker().query(getTask_query)