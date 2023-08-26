from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mtg')
def mtg():
    return render_template('mtg.html')

@app.route('/mtg1')
def mtg1():
    return render_template('mtg1.html')

@app.route('/mtg2')
def mtg2():
    return render_template('mtg2.html')

@app.route('/mtg3')
def mtg3():
    return render_template('mtg3.html')

@app.route('/mtg4')
def mtg4():
    return render_template('mtg4.html')

@app.route('/khb')
def khb():
    return render_template('khb.html')

@app.route('/khb1')
def khb1():
    return render_template('khb1.html')

@app.route('/khb2')
def khb2():
    return render_template('khb2.html')

@app.route('/khb3')
def khb3():
    return render_template('khb3.html')

if __name__ == '__main__':
    app.run(debug=True)