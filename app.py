from flask import Flask
import os

app = Flask(__name__)

# Configuración del directorio para subir archivos
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

@app.route('/')
def index():
    return "¡Hola desde Flask!"

if __name__ == '__main__':
    # Crear carpeta de uploads si no existe
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Ejecutar la aplicación
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=5000))
