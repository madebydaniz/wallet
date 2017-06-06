# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from web.models import Expense, Income

admin.site.register(Expense)
admin.site.register(Income)
