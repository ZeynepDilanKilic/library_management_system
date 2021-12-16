from django.contrib import admin
from .models import Book,CustomerExtra,IssuedBook
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)

class CustomerExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(CustomerExtra, CustomerExtraAdmin)


class IssuedBookAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook, IssuedBookAdmin)
