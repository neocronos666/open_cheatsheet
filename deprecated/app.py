from flask import Flask, render_template, request, redirect, url_for
import os
from settings_manager import SettingsManager
from utils import get_categories

app = Flask(__name__)
settings_manager = SettingsManager('cfg/settings.json')

@app.route('/')
def index():
    categories = get_categories()  # Función que obtiene las categorías
    formulas = get_formulas()      # Función que obtiene las fórmulas
    return render_template('index.html', categories=categories, formulas=formulas)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        for key, value in request.form.items():
            settings_manager.update_setting(key, value)
        return redirect(url_for('settings'))
    settings = settings_manager.load_settings()
    return render_template('settings.html', settings=settings)

@app.route('/sheet/<formula_id>')
def sheet(formula_id):
    formula = get_formula_by_id(formula_id)  # Función que obtiene la fórmula
    return render_template('sheet.html', formula=formula)

if __name__ == '__main__':
    app.run(debug=True)
