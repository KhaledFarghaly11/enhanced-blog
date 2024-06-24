from django.contrib import admin
from blog.models import AboutPage, ContactPage, HomePage

admin.site.register(HomePage)
admin.site.register(AboutPage)
admin.site.register(ContactPage)

