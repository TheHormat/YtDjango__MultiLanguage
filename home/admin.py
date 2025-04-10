from django.contrib import admin
from .models import Book
from modeltranslation.admin import TranslationAdmin


@admin.register(Book)
class BookAdmin(TranslationAdmin):

    group_fieldsets = True

    list_display = ("name",)

    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }
