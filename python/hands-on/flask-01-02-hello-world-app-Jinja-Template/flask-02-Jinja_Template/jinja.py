from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1=20, number2 = 40)

@app.route('/mult')
def number():
    var1, var2 =23,45
<<<<<<< HEAD
    return render_template('body.html', num1 = var1, num2 = var2,multiplication=var1*var2 )


if __name__ == '__main__':
     #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
=======
    return render_template('body.html',num1=var1,num2=var2,x=num1*num2 )




if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
>>>>>>> 3c3759b017fbd0837f5f4843768a6a263cfcde6d
