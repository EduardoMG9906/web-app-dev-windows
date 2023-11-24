import functools
import db
import pymysql

def get_medicamentos():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM medicamentos"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_medicamento(medicamento_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM medicamentos WHERE id_medicamento = {}".format(medicamento_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_medicamento(dosis, via, nombre, frecuencia_dia, duracion_dias, observaciones):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO medicamentos(dosis, via, nombre, frecuencia_dia, duracion_dias, observaciones) VALUES('{}','{}','{}','{}','{}','{}')".format(dosis, via, nombre, frecuencia_dia, duracion_dias, observaciones)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_medicamento(dosis, via, nombre, frecuencia_dia, duracion_dias, observaciones, medicamento_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE medicamentos set dosis='{0}', via='{1}',nombre='{2}', frecuencia_dia='{3}',duracion_dias='{4}', observaciones='{5}' WHERE id_medicamento = {6}".format(dosis, via, nombre, frecuencia_dia, duracion_dias, observaciones, medicamento_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_medicamento(medicamento_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM medicamentos WHERE id_medicamento = {}".format(medicamento_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
