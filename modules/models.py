
from ..database.config import con

def db():
    try:
        conn = con()

    except:
        print("connection error")
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS weather;')
    try:
        cur.execute('CREATE TABLE weather (id serial PRIMARY KEY,'
                                        'city_name varchar (150) NOT NULL,'
                                        'temp_c integer NOT NULL,'
                                        'temp_f integer NOT NULL,'
                                        'weather_condition text,'
                                        'humidity integer,'
                                        'date date NOT NULL);'
                                        )
    except:
        print("table not created")


    conn.commit()

    cur.close()
    conn.close()

db()