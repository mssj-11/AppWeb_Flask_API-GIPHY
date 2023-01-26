from flask import Flask, render_template, request
import requests


app = Flask(__name__)


#   Ruta, Metodos
@app.route('/', methods=['GET', 'POST'])
def home():
    #   Si el metodo enviado es GET
    if request.method == 'GET':
        #   Retornamos sin ninguna informacion
        return render_template('index.html')
    
    
    #   Si el metodo enviado es POST
    if request.form['search']:
        #   Consumimos la API
        url = "https://api.giphy.com/v1/gifs/search?api_key=VUFksjupeQfhsEb3HULIPNknLK0ikRkM&limit=24&q=" + request.form['search']
        #   Respuesta
        response_giphy = requests.get(url)
        #   Formato JSON
        data_giphy = response_giphy.json()
        
        #   Retornamos el HTML con la informacion
        return render_template('index.html', data=data_giphy['data'])
    #   Si no se encuentra la informacion
    else:
        #   Retornamos sin ninguna informacion
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)