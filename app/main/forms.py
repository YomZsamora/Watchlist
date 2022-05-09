from flask_wtf import FlaskForm # help us create a Form class.
from wtforms import StringField, TextAreaField, SubmitField # help us create a text field, a text Area field and a submit button. 
from wtforms.validators import InputRequired # Required class validator that will prevent the user from submitting the form without Inputting a value.

class ReviewForm(FlaskForm): #  ReviewForm class that inherits from the FlaskForm class.

    title = StringField('Review title',  validators=[InputRequired()])
    review = TextAreaField('Movie review', validators=[InputRequired()])
    submit = SubmitField('Submit')