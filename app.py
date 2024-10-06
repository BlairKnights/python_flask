from flask import Flask,redirect,url_for,render_template,request

# Jinja2 Template Engine 
'''
Examples

{% for %}..{% endfor %}  
{% if %}..{% endif %}
 
{%...%} - for loop and condition statements
{{  }} - expressions to print output
{#...#} - this is for comments
'''

#this will create a WSGI application
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

#redirecting function
@app.route('/results/<int:marks>')
def results(marks):
    status=''
    if marks<50:
        status='failed'
    else:
        status='passed'
    result={'marks':marks,'status':status}
    return render_template('results.html',result=result)

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