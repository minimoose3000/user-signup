
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])

def index():

	# defaults for the template
	fields = {}
	errors = {}
	has_error = False

	# handle form post request
	if request.method == 'POST':
		# set the values of the fields 
		fields['username'] = request.form['username']
		fields['password'] = request.form['password']
		fields['password_confirm'] = request.form['password_confirm']
		fields['email'] = request.form['email']

		# error for username
		if not fields['username'] or len(fields['username']) < 3  or len(fields['username']) >20 or ' ' in fields['username']:
			errors['username'] = "Complete the username field. Must be 3 characters or more and less than 20 characters with no spaces"
			has_error = True

		# error for password
		if not fields['password'] or len(fields['password']) < 3 or len(fields['password']) >20 or ' ' in fields['password'] :
			errors['password'] = "Password is invalid. Must be 3 characters or more and less than 20 characters with no spaces"
			has_error = True

		# error for password_confirm
		if fields['password']  != fields['password_confirm']:
			errors['password_confirm'] = "Passwords do not match"
			has_error = True

		#email is optional so only do this check if there is a value
		if fields['email']:
			# error for email - could  combine these into one check or a regex
			if not '@' in fields['email']:
				errors['email'] = "Enter a valid email address"
				has_error = True

			if not '.' in fields['email']:
				errors['email'] = "Enter a valid email address"
				has_error = True

		# check if has_error is still false, then redirect or show errors
		if not has_error:
			#redirects
			return redirect(url_for("success", name=fields['username']))
		else:
			return render_template('form.html', fields=fields, errors=errors, has_error=has_error)

	else: 
		return render_template('form.html',fields=fields, errors=errors, has_error=has_error)


@app.route('/success')
def success():
	return render_template('success.html', name=request.args.get('name'))

if __name__ =='__main__':
app.run()