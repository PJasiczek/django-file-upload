from django.contrib import admin

from .models import Order, Document

class DocumentAdmin(admin.StackedInline):
    model = Document

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email_address',)
    inlines = [DocumentAdmin]

    class Meta:
       model = Order

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('order', 'documents',)
    list_filter = ('order',)
    pass