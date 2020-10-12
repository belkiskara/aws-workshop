from flask import Flask, render_template, url_for, request
app = Flask(__name__)

def roman(input):
   numerals={1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C",
            90:"XC", 50:"L", 40:"XL",10:"X", 9: "IX",  5:"V", 4:"IV", 1:"I"}          
   result=""
   for value, numeral in numerals.items():
      while input >= value:
        result += numeral
        input -= value
   return result

@app.route('/', methods=['GET'])
def main_get():
   return render_template('index.html', devoloper_name='Belkis')

@app.route('/', methods=['POST'])
def main_post():
   x = request.form['number']
   if not x.isdecimal():
      return render_template('index.html', devoloper_name='Belkis', not_valid=True) 
   number = int(x) 
   if not 0 < number < 4000:
      return render_template('index.html', name='Belkis', not_valid=False)
   return render_template('result.html', number_decimal=number, number_roman=roman(number), devoloper_name='Belkis')
if __name__== "__main__":
   # app.run('localhost', port=5000, debug=True)
   # app.run(host='127.0.0.1', port=5000)
   # app.run(debug=True)
   app.run('0.0.0.0', port=80)