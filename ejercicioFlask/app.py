from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista en memoria donde se irán acumulando todas las vulnerabilidades registradas
vulnerabilities = [
    {
        "id": 1,
        "title": "SQL Injection in login",
        "category": "A03 - Injection",
        "severity": "High"
    },
    {
        "id": 2,
        "title": "Cross-Site Scripting (XSS)",
        "category": "A03 - Injection",
        "severity": "Medium"
    },
    {
        "id": 3,
        "title": "Broken Access Control",
        "category": "A01 - Broken Access Control",
        "severity": "High"
    }
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Capturamos los datos enviados desde el formulario
        title = request.form.get('title')
        category = request.form.get('category')
        severity = request.form.get('severity')

        # Si el usuario ingresó un título, creamos un nuevo registro
        if title and title.strip():
            new_id = len(vulnerabilities) + 1
            new_vuln = {
                "id": new_id,
                "title": title.strip(),
                "category": category,
                "severity": severity
            }
            # Lo añadimos a nuestra lista
            vulnerabilities.append(new_vuln)
            
        # Redirigimos a GET para evitar reenvíos dobles del formulario al refrescar
        return redirect(url_for('index'))

    # Si es GET, mostramos la página con la lista actualizada
    return render_template('index.html', vulnerabilities=vulnerabilities)

if __name__ == '__main__':
    app.run(debug=True)