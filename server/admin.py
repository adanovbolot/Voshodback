from django.contrib import admin
from . import models


@admin.register(models.EvotorUsers)
class TerminalAdmin(admin.ModelAdmin):
    list_display = ['id', 'userId', 'token']


@admin.register(models.EvotorToken)
class EvotorTokenAdmin(admin.ModelAdmin):
    list_display = ['id', 'userId', 'token']


@admin.register(models.Shops)
class ShopsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.EvotorOperator)
class EvotorOperatorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Terminal)
class TerminalAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TerminalUser)
class TerminalUserAdmin(admin.ModelAdmin):
    pass
