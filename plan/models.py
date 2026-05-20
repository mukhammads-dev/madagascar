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

         # Creat with Traditional API

    def create_goal(self, content):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO plan SET content=%s,
                created_at=CURRENT_TIMESTAMP, updated_at=CURRENT_TIMESTAMP""",
                [content]
            )
            cursor.execute("SELECT LAST_INSERT_ID()")
            new_plan_id = cursor.fetchone()[0]

            print(f"The new plan_id: {new_plan_id} is created")
            return new_plan_id

        # Creat with Rest API

    def create_plan(self, data):  # define
        content = data["content"]
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO plan (content,created_at, updated_at)
                VALUES (%s, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP)
                """,
                [content]
            )
            cursor.execute("SELECT LAST_INSERT_ID()")
            new_plan_id = cursor.fetchone()[0]

            print(f"The new plan_id: {new_plan_id} is created")
            return new_plan_id

    def update_plan(self, data):
        content = data.get("new_plan")
        plan_id = data.get("id")

        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE plan
                SET content=%s, updated_at = CURRENT_TIMESTAMP
                WHERE id=%s
                """,
                [content, plan_id]
            )
            rows_affected = cursor.rowcount

        if rows_affected == 0:
            raise ValueError("Plan is not found")
        print(f"The plan_id {plan_id} is updated")
        return plan_id
