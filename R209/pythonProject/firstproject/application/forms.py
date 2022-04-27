from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class LivreForm(ModelForm):
    class Meta:
        model = models.Specie
        fields = ('type', 'specie', 'date_discovered','weight','size','weight','lifespan','depth','locations','description')
        labels = {
        'type' : _('type'),
        'specie' : _('specie'),
        'date_discovered' : _('date_discovered'),
        'size' : _('size'),
        'weight': _('weight'),
        'lifespan' : _('lifespan'),
        'depth' : _('depth'),
        'locations' : _('locations'),
        'description' : _('description')
        }