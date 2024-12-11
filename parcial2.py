from flask import Flask, jsonify
import pandas as pd

# Suponiendo que tienes un DataFrame llamado 'df' con los datos cargados

app = Flask(__name__)

@app.route('/vacunas/paises')
def get_paises():
    """Devuelve una lista de todos los países con datos disponibles."""
    paises = df['pais'].unique().tolist()
    return jsonify(paises)

@app.route('/vacunas/pais/<pais>')
def get_pais(pais):
    """Devuelve los datos de vacunación para un país específico."""
    data = df[df['pais'] == pais].to_dict('records')
    return jsonify(data)

@app.route('/vacunas/rango/<inicio>/<fin>')
def get_rango(inicio, fin):
    """Devuelve los datos de vacunación para un rango de años."""
    data = df[(df['ano'] >= int(inicio)) & (df['ano'] <= int(fin))].to_dict('records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)