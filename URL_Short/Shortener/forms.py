from django import forms

HOSTS = (
    ('Bitly', 'Bit.ly'),
    ('Cuttly', 'cutt.ly'),
    ('Clckru', 'clck.ru'),
    ('Chilpit', 'chilp.it'),
    ('Dagd', 'da.gd'),
    ('Isgd', 'Is.gd'),
    ('NullPointer', '0x0.st'),
    ('Osdb', 'Osdb.link	'),
    ('Qpsru', 'Qps.ru	'),
    ('Tinyurl', 'Tinyurl')
)


class Urlform(forms.Form):
    url = forms.CharField(initial='http://', required=True)
    host = forms.ChoiceField(choices=HOSTS)
