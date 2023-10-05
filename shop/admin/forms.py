from wtforms import Form, BooleanField, StringField, PasswordField, validators, TelField

class RegistrationForm(Form):
    name = StringField('Imię',[validators.Length(min=4, max=25)], render_kw={"placeholder": "Imię"})
    username = StringField('Nazwisko',[validators.Length(min=4, max=25)], render_kw={"placeholder": "Nazwisko"})
    email = StringField('E-mail',[validators.Length(min=4, max=25)], render_kw={"placeholder": "E-mail"})
    password = PasswordField('Hasło', [validators.DataRequired(),validators.EqualTo('confirm', message="Hasło musi być takie samo")])
    confirm =  PasswordField('Powtórz Hasło')