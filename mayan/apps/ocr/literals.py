from django.utils.translation import ugettext_lazy as _

DOCUMENTQUEUE_STATE_STOPPED = 's'
DOCUMENTQUEUE_STATE_ACTIVE = 'a'

DOCUMENTQUEUE_STATE_CHOICES = (
    (DOCUMENTQUEUE_STATE_STOPPED, _(u'stopped')),
    (DOCUMENTQUEUE_STATE_ACTIVE, _(u'active')),
)

QUEUEDOCUMENT_STATE_PENDING = 'p'
QUEUEDOCUMENT_STATE_PROCESSING = 'i'
QUEUEDOCUMENT_STATE_ERROR = 'e'

QUEUEDOCUMENT_STATE_CHOICES = (
    (QUEUEDOCUMENT_STATE_PENDING, _(u'pending')),
    (QUEUEDOCUMENT_STATE_PROCESSING, _(u'processing')),
    (QUEUEDOCUMENT_STATE_ERROR, _(u'error')),
)

DEFAULT_OCR_FILE_FORMAT = u'tiff'
DEFAULT_OCR_FILE_EXTENSION = u'tif'
UNPAPER_FILE_FORMAT = u'ppm'