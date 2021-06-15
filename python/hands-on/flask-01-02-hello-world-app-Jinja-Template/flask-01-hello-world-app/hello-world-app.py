from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello World !")

@app.route('/second')
def second():
    return('Bize her yer Erzurum')

@app.route('/third/subthird')
def third():
    return('Burası Subthird')


@app.route('/forth/<string:id>')
def forth(id):
    return(f'Bu sayfanın Numarası {id}')


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)