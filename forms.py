from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, FloatField
from wtforms.validators import DataRequired, Length

class EditForm(FlaskForm):
    hidden_id = HiddenField()
    rating = FloatField("Rating", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired(),Length(min=1, max=500, message="review must be less than 500 characters")])
    submit = SubmitField("Done")

class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired(), Length(min=1, max=250)])
    submit = SubmitField("Add Movie")