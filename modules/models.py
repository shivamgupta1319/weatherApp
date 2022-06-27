
from database.config import config

def db():
    try:
        conn = config()

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
                                        'date date NOT NULL);'
                                        )
    except:
        print("table not created")


    conn.commit()

    cur.close()
    conn.close()