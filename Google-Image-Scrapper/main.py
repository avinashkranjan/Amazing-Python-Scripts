from flask import Flask, render_template, request, flash, redirect, send_from_directory
from scrapper import simple_image_download
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email
import os

app = Flask(__name__, template_folder='templates')
response = simple_image_download()
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'
bootstrap = Bootstrap(app)
downloaded = [False]
image_request = {'name': '', 'number_of_images': 0}


class ImageForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    number_of_images = IntegerField(
        'number_of_images', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ImageForm()
    if form.validate_on_submit():
        image_request['name'] = request.form['name']
        image_request['number_of_images'] = request.form['number_of_images']
        flash('Your images are being downloaded. Please wait.')
        downloaded[0] = True
        return redirect('/')

    if downloaded[0]:
        response.download(image_request['name'], int(
            image_request['number_of_images']))
        flash('All of your images have been downloaded')
        downloaded[0] = False
        return redirect('/')
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
