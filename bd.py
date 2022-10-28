import sqlite3

#Crear una conexión
miConexion=sqlite3.connect("PrimeraBase")
#Crear un cursor
cursor=miConexion.cursor()
"""cursor.execute(
    "CREATE TABLE PRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(25),CANTIDAD INTEGER,OBSERVACION VARCHAR(45))")
"""
#cursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,'PC',5,'No hay observacion')")
"""productos=[
    ('PC',5,'No hay observacion'),
    ('Mouse',78,'No hay observacion'),
    ('Pantalla',9,'No hay observacion'),
    ('Flas',10,'No hay observacion'),
]
cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)"""
cursor.execute("SELECT * FROM PRODUCTOS")
listaProductos=cursor.fetchall()
for producto in listaProductos:
    print("ID:",producto[0],"Nombre:",producto[1],"Cantidad:",producto[2],"Observación:",producto[3])
cursor.execute("UPDATE PRODUCTOS SET CANTIDAD=20 WHERE ID'"+listaProductos+"'")
cursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")
#print(listaProductos)
miConexion.commit()
miConexion.close()