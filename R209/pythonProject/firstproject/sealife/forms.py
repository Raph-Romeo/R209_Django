from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class LivreForm(ModelForm):
    class Meta:
        model = models.Specie
        fields = ('type',
                  'specie',
                  'date_discovered',
                  'weight',
                  'size',
                  'weight',
                  'lifespan',
                  'depth',
                  'locations',
                  'description',
                  'image')
        labels = {
            'Type': _('type'),
            'Specie': _('specie'),
            'Date discovered (mm/dd/yyyy)': _('date_discovered'),
            'Size': _('size'),
            'Weight': _('weight'),
            'Lifespan (years)': _('lifespan'),
            'Depth (m)': _('depth'),
            'Locations': _('locations'),
            'Description': _('description'),
            'Image': _('image')
        }
