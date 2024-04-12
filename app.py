from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
import math

app = Flask(__name__)

# Ruta del inicio que muestra la página de descripción y los botones
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/muestra')
def muestra():
    # Aquí debes renderizar una plantilla HTML para la página del entorno, por ejemplo:
    return render_template('muestra.html')

@app.route('/muestra', methods=['GET', 'POST'])
def calcular_muestra():
    if request.method == 'POST':
        #K = float(request.form['K'])
        K=1.96
        #p = float(request.form['p'])
        p=0.25
        N = int(request.form['N'])
        #E = float(request.form['E'])
        E = 0.05
        n = (K**2 * N * p * (1-p)) / (((N-1) * E**2) + (K**2 * p * (1-p)))
        n = math.ceil(n)  # Redondear hacia arriba para obtener un entero
        resultado_visible = True  # Hacemos visible el resultado después de calcular
        # Retorna las variables incluyendo resultado_visible
        return render_template('muestra.html', resultado_visible=resultado_visible, n=n, K=K, p=p, N=N, E=E)
    else:
        # La página se carga por primera vez, el resultado no debe ser visible
        return render_template('muestra.html', resultado_visible=resultado_visible, n=None, K=None, p=None, N=None, E=None)
    
# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)