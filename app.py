from flask import Flask,render_template

app = Flask(__name__)


#route() decorators
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portfolio.html')
def portfolio():
    return render_template('portfolio.html')



@app.route('/status', methods=['GET'])
def status():
  return 'OK', 200




if __name__ == '__main__':
    app.run()
