from flask import Flask, render_template

app = Flask(__name__)

@app.route('/faq')
def faq():
    faqs = [
        {"question": "How do I reset my password?", "answer": "Click on 'Forgot Password' at login."},
        {"question": "Where can I see my purchases?", "answer": "Navigate to your dashboard and click 'Orders'."},
        {"question": "Do you offer student discounts?", "answer": ""},
        {"question": "Can I cancel my subscription anytime?", "answer": "Yes, cancellation is available under account settings."}
    ]
    return render_template('faq.html', faqs=faqs)

if __name__ == '__main__':
    app.run(debug=True)
