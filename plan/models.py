from django.db import models, connection

# Plan model


class Plan():
    # state

    # constructor
    def __init__(self):
        self.connection = connection

    # method
    def get_home(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM plan WHERE 1 = 1")
            result = cursor.fetchall()
            print(result)
