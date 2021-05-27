# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


@apphook_pool.register  # register the application
class UsersApp(CMSApp):

    app_name = 'users'

    name = _('Users')

    def get_urls(self, page=None, language=None, **kwargs):
        return ["ahighschooledu.apps.users.urls"]

