# my_setings

#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os
from django.core.wsgi import get_wsgi_application

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webface.settings")

application = get_wsgi_application()
