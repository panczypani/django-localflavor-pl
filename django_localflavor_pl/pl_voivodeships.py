"""
Polish voivodeship as in http://en.wikipedia.org/wiki/Poland#Administrative_division
"""

from django.utils.translation import ugettext_lazy as _

VOIVODESHIP_CHOICES = (
    ('lower_silesian', _('Lower Silesian')),
    ('kuyavia-pomeranian', _('Kuyavia-Pomeranian')),
    ('lublin', _('Lublin')),
    ('lubusz', _('Lubusz')),
    ('lodz', _('Lodz')),
    ('lesser_poland', _('Lesser Poland')),
    ('masovian', _('Masovian')),
    ('opole', _('Opole')),
    ('subcarpatian', _('Subcarpatian')),
    ('podlasie', _('Podlasie')),
    ('pomeranian', _('Pomeranian')),
    ('silesia', _('Silesian')),
    ('swietokrzyskie', _('Swietokrzyskie')),
    ('warmia-masurian', _('Warmia-Masurian')),
    ('greater_poland', _('Greater Poland')),
    ('west_pomeranian', _('West Pomeranian')),
)
