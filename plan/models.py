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
            columns = [col[0] for col in cursor.description]
            print("columns:", columns)
            print("\n\n\n")
            plans = [dict(zip(columns, row)) for row in cursor.fetchall()]
            print("plans:", plans)

            print(f"The count: {len(plans)} plans")
            return plans
