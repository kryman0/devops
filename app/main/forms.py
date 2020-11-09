"""
Contains form for main purpose of application
"""
from flask import current_app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, Length, DataRequired
from app.models import User



class PostForm(FlaskForm):
    """
    Form for posting to system
    """
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')



class EditProfileForm(FlaskForm):
    """
    Form for editing user profile
    """
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        # Added my own pylint disablement.
        #pylint: disable=refactoring
        super(EditProfileForm, self).__init__(*args, **kwargs)
        #pylint: enable=refactoring
        self.original_username = original_username

    def validate_username(self, username):
        """
        Check if username already exsits
        """
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                current_app.logger.debug("Username already exist. {}".format(user))
                raise ValidationError('Please use a different username.')
