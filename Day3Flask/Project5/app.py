'''
5. Job Listings Board 
 Requirements: 
 /jobs route passes a list of jobs 
 Use {% for job in jobs %} to loop and show cards 
 Use {% if job['remote'] %} to highlight remote jobs 
 Include company logos from static/ 
 Reuse base navbar and footer
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/jobs')
def jobs():
    jobs_list = [
        {
            'title': 'Software Engineer',
            'company': 'Google',
            'logo': 'google.png',
            'location': 'Mountain View, CA',
            'remote': True
        },
        {
            'title': 'Data Analyst',
            'company': 'Amazon',
            'logo': 'amazon.png',
            'location': 'Seattle, WA',
            'remote': False
        },
        {
            'title': 'DevOps Engineer',
            'company': 'RemoteTech',
            'logo': 'remote.png',
            'location': 'Remote',
            'remote': True
        }
    ]
    return render_template('jobs.html', jobs=jobs_list)

if __name__ == '__main__':
    app.run(debug=True)
