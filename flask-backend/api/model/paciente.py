import functools
import db
import pymysql

def get_pacientes():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM pacientes"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_paciente(paciente_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM pacientes WHERE id_paciente = {}".format(paciente_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_paciente(tipo_id, nombre, email, grupo_sanguineo, genero, edad, fecha_nacimiento, direccion, celular, eps, serial_hc):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO pacientes(tipo_id, nombre, email, grupo_sanguineo, genero, edad, fecha_nacimiento, direccion, celular, eps, serial_hc) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(tipo_id, nombre, email, grupo_sanguineo, genero, edad, fecha_nacimiento, direccion, celular, eps, serial_hc)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_paciente(tipo_id, nombre, email, grupo_sanguineo, genero, edad, fecha_nacimiento, direccion, celular, eps, serial_hc, paciente_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE pacientes set tipo_id='{0}', nombre='{1}',email='{2}',grupo_sanguineo='{3}',genero='{4}',edad='{5}',fecha_nacimiento='{6}',direccion='{7}',celular='{8}',eps='{9}',serial_hc='{10}' WHERE id_paciente = {11}".format(tipo_id, nombre, email, grupo_sanguineo, genero, edad, fecha_nacimiento, direccion, celular, eps, serial_hc, paciente_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_paciente(paciente_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM pacientes WHERE id_paciente = {}".format(paciente_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
