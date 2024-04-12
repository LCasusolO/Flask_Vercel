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
        N1 = int(request.form['N1'])
        N2 = int(request.form['N2'])
        N3 = int(request.form['N3'])

        #E = float(request.form['E'])
        E = 0.05
        n1 = (K**2 * N1 * p * (1-p)) / (((N1-1) * E**2) + (K**2 * p * (1-p)))
        n1 = math.ceil(n1)  # Redondear hacia arriba para obtener un entero

        n2 = (K**2 * N2 * p * (1-p)) / (((N2-1) * E**2) + (K**2 * p * (1-p)))
        n2 = math.ceil(n2)  # Redondear hacia arriba para obtener un entero

        n3 = (K**2 * N3 * p * (1-p)) / (((N3-1) * E**2) + (K**2 * p * (1-p)))
        n3 = math.ceil(n3)  # Redondear hacia arriba para obtener un entero

        n = n1 + n2 + n3
        resultado_visible = True  # Hacemos visible el resultado después de calcular
        # Retorna las variables incluyendo resultado_visible
        return render_template('muestra.html', resultado_visible=resultado_visible, n1=n1, n2=n2, n3=n3, n=n, K=K, p=p, N1=N1, N2=N2, N3=N3, E=E)
    else:
        # La página se carga por primera vez, el resultado no debe ser visible
        return render_template('muestra.html', resultado_visible=resultado_visible, n1=None, n2=None, n3=None, n=None, K=None, p=None, N1=None, N2=None, N3=None, E=None)
    
# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)