import psycopg2
import re
from environs import Env

class DBPostgresql:

    def __init__(self, estructura, table_name):
        self._table_name = table_name
        self._estruct = estructura
        env = Env()
        env.read_env()
        self._connect = psycopg2.connect(
            host=env('POSTGRES_HOST'), 
            database=env('POSTGRES_DB'), 
            user=env('POSTGRES_USER'), 
            password=env('POSTGRES_PASSWORD')
        )

        self._cur = self._connect.cursor()
        self._launch_query('SELECT 1')
        print("Conexion exitosa")
            

    #def __del__(self):
    #    self._connect.close()
    #    self._cur.close()




    def _launch_query(self, query):
        print(query)
        self._cur.execute(query)
        matches = re.search(r"^SELECT", query, re.IGNORECASE)
        if not matches:
            self._connect.commit()


    def insert(self, data):

        values = "'" + "', '".join(data.values()) + "'"
        query = f'INSERT INTO public.{self._table_name} ({", ".join(data.keys())}) VALUES ({values});'

        self._launch_query(query)

        return True


    def delete(self, id_object):
        query = f'DELETE FROM public.{self._table_name} WHERE id = {id_object};'

        self._launch_query(query)


    def update(self, id_object, data):

        list_update = []
        for field_name, field_value in data.items():
            list_update.append(f"{field_name}='{field_value}'")
        

        query = f'''UPDATE "organizaciones".{self._table_name} SET {", ".join(list_update)} WHERE id_org = '{id_object}';'''
        self._launch_query(query)


    def get_by_id(self, id_object):
        query = f'SELECT * FROM public.{self._table_name} WHERE id = {id_object};'

        table_keys = []
        for schema_key in self._estruct.keys():
            table_keys.append(schema_key)
            
        data = {}
        self._launch_query(query)
        row = self._cur.fetchone()
        for key, value in enumerate(row):
            data[table_keys[key]] = value

        return data


    def get_by_filters(self, filters=None):

        list_filters = []

        where = '1=1'
        if filters is not None:
            for field_name, field_value in filters.items():
                list_filters.append(f"{field_name} LIKE '%{field_value}%'")

                where = " AND ".join(list_filters)

        query = f'SELECT * FROM public.{self._table_name} WHERE {where};'

        table_keys = []
        for schema_key in self._estruct.keys():
            table_keys.append(schema_key)

        list_data = []
        self._launch_query(query)
        rows = self._cur.fetchall()

        for row in rows:
            data = {}
            for key, value in enumerate(row):
                data[table_keys[key]] = value

            list_data.append(data)

        return list_data


    def get_all(self):
        return self.get_by_filters()
