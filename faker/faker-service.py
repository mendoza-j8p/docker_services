from flask import Flask
from faker import Faker

app = Flask(__name__)
faker = Faker()

@app.route('/faker_data')
def get_fake_data():
    try:
        return "Hola mundo, hola desde get_fake_data"
    except:
        return "Error en el endpoint de get_fake_data"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
