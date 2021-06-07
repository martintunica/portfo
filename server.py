from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

#home route
@app.route("/")
def world():
    return render_template('index.html')
#html's routes
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


#forn to database txt
def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		messege = data["messege"]
		file = database.write(f'\n{email},\t{subject},\t{messege}')
# form to csv database
def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		messege = data["messege"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,messege])


#form send
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
    	try:
    		data = request.form.to_dict()
    		write_to_csv(data)
    		return redirect('/thank_you.html')
    	except:
    		return 'did not save to database'
    else:
    	return 'ups! something went wrong.'
       


# html routs (clean code)

# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/index.html")
# def world2():
#     return render_template('index.html')
