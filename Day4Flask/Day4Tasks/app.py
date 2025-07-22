from flask import Flask, render_template, request, redirect, flash
from forms import UserForm

app = Flask(__name__)
app.secret_key = 'form_secret_123'

#2. Capture the submitted form data in a POST request and print it to the console 
@app.route("/", methods=["GET", "POST"])
def index():
    form = UserForm()

    if request.method == "POST":
        print("\n--- FORM DATA ---")
        print({field.name: field.data for field in form})
        print("Errors:", form.errors)

        if form.validate_on_submit():
            flash("Form submitted successfully!", "success")
            flash(f"Welcome, {form.name.data}!", "info")
            if form.age.data > 60:
                flash("Note: You're above 60. Consult trainer before heavy workouts.", "warning")
            return render_template("success.html", form=form)
        else:
            flash("Please correct the errors and resubmit.", "danger")
    return render_template("index.html", form=form)

if __name__=='__main__':
    app.run(debug=True)