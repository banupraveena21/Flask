from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/gallery')
def gallery():
    gallery_folder = os.path.join(app.static_folder, 'images/gallery')
    image_files = [
        f for f in os.listdir(gallery_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
    ]
    return render_template('gallery.html', images=image_files)

if __name__ == '__main__':
    app.run(debug=True)
