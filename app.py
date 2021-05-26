from flask import Flask,render_template,session,url_for,redirect,request
app= Flask(__name__)
app.secret_key='a'

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/CALCULATOR')
def Calculator():
    return render_template('Calculator.html') 

@app.route('/BMI',methods=['GET','POST'])
def BMI():
    if request.method == 'POST':
        Height= request.form.get('Height')
        Weight = request.form.get('Weight')
        Answer = round(int(Weight)/(int(Height)*int(Height))*10000,2)
        return render_template("bmi.html",ans=Answer)
    return render_template('bmi.html') 

@app.route('/PERCENTAGE',methods=['POST','GET'])
def PERCENTAGE():
    if request.method == 'POST':
        value= request.form.get('value')
        total = request.form.get('total')
        Answer = round(int(value)/int(total)*100,2)
        return render_template("percentage.html",ans=Answer)
    return render_template('percentage.html')

@app.route('/INTEREST',methods=['POST','GET'])
def INTEREST():
    if request.method == 'POST':
        Principle = request.form.get('Principle')
        NOY = request.form.get('NOY')
        ROI = request.form.get('ROI')
        Answer = round(int(Principle)*int(NOY)*int(ROI)/100,2)
        return render_template("interest.html",ans=Answer)
    return render_template('interest.html')

@app.route('/EMI',methods=['POST','GET'])
def EMI():
    if request.method == 'POST':
        Principle = request.form.get('Principle')
        NOY = request.form.get('NOY')
        ROI = request.form.get('ROI')
        Answer = round(int(Principle)*int(int(ROI))*(((1+int(ROI))**int(NOY))/((1+int(ROI))**int(NOY)-1)),2)
        return render_template("emi.html",ans=Answer)
    return render_template('emi.html')

@app.route('/TEMPERATURE',methods=['GET','POST'])
def TEMPERATURE():
    if request.method == 'POST':
        Celsius = request.form.get('Celsius')
        Answer = 1.8*int(Celsius)+32
        return render_template("temperature.html",ans=Answer)
    return render_template('temperature.html')

if __name__=='__main__':
    app.run(debug=True)