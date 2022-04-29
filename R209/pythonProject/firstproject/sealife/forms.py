from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class AnimalForm(ModelForm):
    class Meta:
        model = models.Animal
        fields = ('type',
                  'specie',
                  'image',
                  'date_discovered',
                  'weight',
                  'size',
                  'weight',
                  'lifespan',
                  'depth',
                  'locations',
                  'description')
        labels = {
            'Type': _('type'),
            'Specie': _('specie'),
            'Image': _('Image'),
            'Date discovered (mm/dd/yyyy)': _('date_discovered'),
            'Size': _('size'),
            'Weight': _('weight'),
            'Lifespan (years)': _('lifespan'),
            'Depth (m)': _('depth'),
            'Locations': _('locations'),
            'Description': _('description')
        }
        localized_fields = ('date_discovered',)

class CategoryForm(ModelForm):
    class Meta:
        model = models.Categories
        fields = ('name',
                  'description',
                  'image')
        labels = {
            'Type': _('name'),
            'Specie': _('description'),
            'image': _('image'),
        }