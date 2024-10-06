from flask import Flask,redirect,url_for,render_template,request

#this will create a WSGI application
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/info')
def info():
    return "Second page."

'''
@app.route('/failed/<int:marks>')
def failed(marks):
    return "Failed:"+str(marks)
'''
'''
@app.route('/passed/<int:marks>')
def passed(marks):
    res=''
    if marks<50:
        res='failed'
    else:
        res='passed'
    return render_template('results.html',result=res)
'''

#redirecting function
@app.route('/results/<int:marks>')
def results(marks):
    res=""
    if marks<50:
        res="failed" 
    else:
        res="passed"
    return render_template('results.html',result=res)

#result checker
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        programming=float(request.form['programming'])
        devops=float(request.form['devops'])
        statsml=float(request.form['statsml'])
        total_score=(programming+devops+statsml)/3
    return redirect(url_for('results',marks=total_score))

if __name__=="__main__":
    app.run(debug=True)