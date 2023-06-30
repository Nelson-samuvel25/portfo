from flask import Flask,render_template,request,redirect
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def store_data(data):
    with open('database.txt',mode='a') as database:

        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\nname:{name},email:{email},subject:{subject},message:{message}')
    return file

def store_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])
    return csv_writer

@app.route('/<html_page>')
def webpage(html_page):
    return render_template(html_page)

@app.route('/form_submit',methods=['GET','POST'])
def submitform():
    if request.method =='POST':
       try:
        data = request.form.to_dict()
        store_csv(data)
        return redirect('/thanks.html')
       except:
           return 'not saved to database'
    else:
        return 'something went wrong'