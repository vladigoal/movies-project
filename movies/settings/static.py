from .utils import proj

STATIC_ROOT = proj('static_media', 'static_root')
STATIC_URL = '/media/static/'

STATICFILES_DIRS = (
    proj('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
)
