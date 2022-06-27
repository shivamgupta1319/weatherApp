import os
import psycopg2
try:
    conn = psycopg2.connect(user = "weather",
                        password = "shivam13",
                        host = "127.0.0.1",
                        port = "5432",
                        database = "weatherdb")

except:
    print("connection error")
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS weather;')
try:
    cur.execute('CREATE TABLE weather (id serial PRIMARY KEY,'
                                    'city_name varchar (150) NOT NULL,'
                                    'min_temp integer NOT NULL,'
                                    'max_temp integer NOT NULL,'
                                    'weather_type text,'
                                    'date1 date NOT NULL,'
                                    'date2 date NOT NULL,'
                                    'date3 date NOT NULL);'
                                    )
except:
    print("table not created")


conn.commit()

cur.close()
conn.close()