

import psycopg2


def con():
        connection = psycopg2.connect(user = "weather",
                                    password = "shivam13",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "weatherdb")
        return connection