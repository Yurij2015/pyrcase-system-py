from django.contrib import admin

# Register your models here.
from .models import Tutor, Category, Learnbook


# admin.site.register(Tutor)

class LearnbookInstanceInline(admin.TabularInline):
    model = Learnbook
    extra = 0


# Define the admin class
class TutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'description')
    # fields = ['first_name', 'last_name', ('description')]
    # fieldsets = (
    #     ('Description', {
    #         'fields': ('description', 'last_name')
    #     }),
    # )
    inlines = [LearnbookInstanceInline]


# Register the admin class with the associated model
admin.site.register(Tutor, TutorAdmin)


# admin.site.register(Category)
# Register the Admin class for Category using the decorator
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    # list_display = ('id', 'name')


# admin.site.register(Learnbook)
# Register the Admin class for Category using the decorator
@admin.register(Learnbook)
class LearnbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'display_category')
    list_filter = ('summary', 'tutor_id')
