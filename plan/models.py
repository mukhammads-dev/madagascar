from django.db import models, connection

# Plan model


class Plan():
    # state

    # constructor
    def __init__(self):
        self.connection = connection

    # method
    def get_home(self):
        print("STEP 3: BACKENDdan DATABASEga jonash ")
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM plan WHERE 1 = 1")
            columns = [col[0] for col in cursor.description]
            print("columns:", columns)
            print("\n\n\n")
            plans = [dict(zip(columns, row)) for row in cursor.fetchall()]

            print("plans:", plans)
            print("STEP 4: DATABASEdan BACKENDga kirib kelish ")

            print(f"The count: {len(plans)} plans")
            return plans

         # Creat with Traditional API

    def create_goal(self, content):
        print("STEP 3 create: BACKENDdan DATABASEga jonash ")
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO plan SET content=%s,
                created_at=CURRENT_TIMESTAMP, updated_at=CURRENT_TIMESTAMP""",
                [content]
            )
            cursor.execute("SELECT LAST_INSERT_ID()")
            new_plan_id = cursor.fetchone()[0]
            print("STEP 4 create: DATABASEdan BACKENDga kirib kelish ")

            print(f"The new plan_id: {new_plan_id} is created")
            return new_plan_id

        # Creat with Rest API

    def create_plan(self, data):  # define
        content = data["content"]
        print("STEP3: Backend > CRUD command > Database")
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

            print("STEP4: Database > CRUD result > Backend")
            print(f"The new plan_id: {new_plan_id} is created")
            return new_plan_id
