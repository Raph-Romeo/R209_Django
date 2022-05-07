from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class AnimalForm(ModelForm):
    class Meta:
        model = models.Animal
        fields = ('category',
                  'species',
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
            'category': _('Animal'),
            'species': _('Species'),
            'image': _('Image'),
            'date_discovered': _('Date discovered (yyyy-mm-dd)'),
            'size': _('Size (cm)'),
            'weight': _('Weight (kg)'),
            'lifespan': _('Lifespan (years)'),
            'depth': _('Depth (m)'),
            'locations': _('Locations'),
            'description': _('Description')
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