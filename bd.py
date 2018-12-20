import psycopg2


class DatabaseDB:
    def __init__(self, database, user, password, model):
        self.database = database
        self.user = user
        self.password = password
        self.model = model


    def listar(self):
        con = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        cur = con.cursor()
        query = "SELECT * FROM {};".format(self.model)
        cur.execute(query)
        for registro in cur.fetchall():
            print(registro)

        cur.close()
        con.close()


class DistritoDB(DatabaseDB):

    def insertar(self, id, nombre):
        con = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        cur = con.cursor()
        query = "INSERT INTO {}(id, nombre) " \
                "values(%s, %s);".format(self.model)

        data = (id, nombre)
        cur.execute(query, data)
        con.commit()

        cur.close()
        con.close()


    def update(self, id, nombre):
        con = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        cur = con.cursor()
        query = "UPDATE {} set " \
                " nombre = %s" \
                " where id = %s;".format(self.model)

        data = (nombre, id)
        updated_rows = cur.rowcount
        cur.execute(query, data)
        con.commit()

        cur.close()
        con.close()

        return updated_rows


    def delete(self, id):
        con = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        cur = con.cursor()
        query = "DELETE FROM {} " \
                " where id = %s;".format(self.model)

        data = (id, )
        cur.execute(query, data)
        con.commit()

        cur.close()
        con.close()

    def poblar(self):
        self.insertar(1, 'Lima')
        self.insertar(2, 'Callao')
        self.insertar(3, 'Linceeee')


class MotelDB(DatabaseDB):

    def insertar(self, id, nombre, direccion, telefono, horario, tarifa, distrito):
        con = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        cur = con.cursor()
        query = "INSERT INTO {}(id, nombre, direccion, telefono, horario, tarifa, distrito_id) " \
                "values(%s, %s, %s, %s, %s, %s, %s);".format(self.model)

        data = (id, nombre, direccion, telefono, horario, tarifa, distrito)
        cur.execute(query, data)
        con.commit()

        cur.close()
        con.close()

    def poblar(self):
        self.insertar(1, 'Motel Riso', 'Riso 234', '', '08 - 16', 80, 1)
        self.insertar(2, 'Wimbledon', 'Riso 234', '', '08 - 16', 120, 3)


d = DistritoDB(database="moteles", user='postgres', password='123456', model='motel_distrito')
d.update(3, 'Ejemplo')
d.insertar(4, 'Para borrar')
d.listar()
d.delete(4)
d.listar()

m = MotelDB(database="moteles", user='postgres', password='123456', model='motel_motel')
#m.poblar()
m.listar()
