from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/home/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        ################# text processing ####################
        my_text = request.form['my_text']
        with open('text.txt', 'w', encoding='utf-8') as fp:
            fp.write(my_text)
        return redirect(url_for('success', my_text='yes'))
    else:
        pass


@app.route('/success/<my_text>')
def success(my_text):
    return render_template('text_show.html', my_text=my_text)


if __name__ == '__main__':
    
    # host : 默认为127.0.0.1（localhost）。设置为'0.0.0.0'以使服务器在外部可用。虽然显示Running on http://192.168.0.2:8080/ (Press CTRL+C to quit)。但是还是不行。
    #       但是居然 host='192.168.0.2'，显示也一样，就行了！
    # port 默认值为5000
    # app.run(host='192.168.0.2', port=8080)




    #  * Running on http://127.0.0.1:8080
    app.run(port=8080)


##########################
'''
python hello.py
'''
##########################
