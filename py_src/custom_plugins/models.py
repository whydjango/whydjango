from filer.fields.image import FilerImageField
from cms.models import CMSPlugin

class FeatureImagePlugin(CMSPlugin):
    image = FilerImageField()
