# 13. Hotel Room Booking Form 
'''
Requirements: 
 Fields: Full Name, Email, Room Type (SelectField), Nights (Integer) 
 Nights must be ≥ 1 
 Flash “Booking for [name] confirmed: [nights] nights in [room type]” 
 Show validation errors
'''

from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'secretkey' 

ROOM_TYPES = ['Single', 'Double', 'Suite']

@app.route('/', methods=['GET', 'POST'])
def book_room():
    errors = {}
    values = {}

    if request.method == 'POST':
        full_name = request.form.get('full_name', '').strip()
        email = request.form.get('email', '').strip()
        room_type = request.form.get('room_type', '')
        nights = request.form.get('nights', '').strip()

        values = {'full_name': full_name, 'email': email, 'room_type': room_type, 'nights': nights}

       
        if not full_name:
            errors['full_name'] = 'Full name is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if room_type not in ROOM_TYPES:
            errors['room_type'] = 'Invalid room type selected.'
        try:
            nights_int = int(nights)
            if nights_int < 1:
                errors['nights'] = 'Nights must be 1 or more.'
        except ValueError:
            errors['nights'] = 'Nights must be an integer.'

        if not errors:
            flash(f"Booking for {full_name} confirmed: {nights} nights in {room_type}", 'success')
            return redirect(url_for('book_room'))

    return render_template('booking_form.html', errors=errors, values=values, room_types=ROOM_TYPES)

if __name__ == '__main__':
    app.run(debug=True)