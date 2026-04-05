from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="registro"
    )
@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/inventario')
def inventario():
    return render_template('inventario.html')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@app.route('/clientes')
def formulario():
    return render_template('interfaz.html')

@app.route('/guardar_cliente', methods=['POST'])
def guardar_cliente():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    direccion = request.form['direccion']

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO clientes (nombre, telefono, correo, direccion) VALUES (%s, %s, %s, %s)",
        (nombre, telefono, correo, direccion)
    )
    conexion.commit()
    cursor.close()
    conexion.close()

    return redirect('/')  
@app.route('/consultar_cliente')
def consultar_cliente():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template('consultar_cliente.html', clientes=clientes)


if __name__ == '__main__':
    app.run(debug=True)

