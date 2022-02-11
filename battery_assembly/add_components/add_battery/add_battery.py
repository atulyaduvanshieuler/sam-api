import json
import psycopg2
from psycopg2 import sql
from verify_battery import verify_function

database_config = {
    "user": 'postgres',
    "password": '9812376024',
    "host": '172.19.0.2',
    "port": 5432,
    "dbname": 'postgres'
}
#input will be motor_id and emch
def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    emch_number = body["emch"]
    battery_id = body["battery_id"]

    verification=verify_function(battery_id)
    if verification[0]:
        with psycopg2.connect(**database_config) as conn: 
            with conn.cursor() as cur:

                dbquery = """
                            UPDATE battery_assemblies SET battery=(sub_query_2.id) FROM 
                            ( SELECT battery_assembly FROM vehicles WHERE emch=%s ) AS sub_query_1,
                            (SELECT id FROM batteries WHERE battery_id= %s ) AS sub_query_2
                            WHERE battery_assemblies.id= sub_query_1.battery_assembly
                                
                            """
                cur.execute(dbquery, (emch_number,battery_id))
                conn.commit()

        msg = {
            "message": "battery with battery id: %s added successfully in vehicle with following EMCH number: %s"
            % (battery_id, emch_number)
        }
    else:
        msg={
            "message":verification[1]
        }

    return {"statusCode": 200, "body": json.dumps(msg)}
