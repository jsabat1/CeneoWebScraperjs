from wtforms import Form, StringField, validators, SubmitField

class ProductIdForm(Form):
    product_id = StringField('Product ID', name="product_id", validators=[
        validators.DataRequired(message="Product ID is required"),
        validators.Length(min=6, max=10, message="Product ID must be between 6 and 10 characters"),
        validators.Regexp(regex='^[0-9]*$', message="Product ID must be numeric")
    ])
    submit = SubmitField('Extract')