from flask import Flask, render_template, flash, request
import os

app = Flask(__name__)
app.secret_key = 'Necessary_to_have'
app.debug = True

@app.route('/', methods = ["GET","POST"])
def hello_world():

    if request.method == 'POST':
        flash('Learn how to remove Flask flash banners with this ---------------------------------------------------->', 'info')
    return render_template('home.html')


@app.route('/progress_bar', methods=['GET','POST'])
def progress_bar():
    if request.method == 'POST':
        uploadData=request.files['media']
        data_file_name = uploadData.filename
        uploadData.save(os.path.join(app.root_path,data_file_name))
    return render_template('progress_bar.html')


if __name__ == '__main__':
    app.run()