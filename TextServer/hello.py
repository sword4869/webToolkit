from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        my_str = request.form['my_str']
        with open('response.txt', 'w', encoding='utf-8') as fp:
            fp.write(my_str)
        return redirect(url_for('success', my_str='yes'))
    else:
        pass


@app.route('/success/<my_str>')
def success(my_str):
    return render_template('hello.html', my_str=my_str)


if __name__ == '__main__':
    # host : 默认为127.0.0.1（localhost）。设置为'0.0.0.0'以使服务器在外部可用。虽然显示Running on http://192.168.0.2:80/ (Press CTRL+C to quit)。但是还是不行。
    #       但是居然 host='192.168.0.2'，显示也一样，就行了！
    # port 默认值为5000
    app.run(host='192.168.0.2', port=80)
    # app.run(port=80)

##########################
# python Hello.py
