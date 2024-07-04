from django.contrib import admin
from django.utils.html import format_html
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

from tutor_app.models import Tutor, Review
from tutor_app.filters import TutorFilter, StudentFilter


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['get_first_name', 'get_last_name', 'city', 'get_average_rating', 'display_photo']
    autocomplete_fields = ['user']
    list_filter = (('city', DropdownFilter),
                   ('subject', DropdownFilter))
    list_per_page = 25
    search_fields = ['city']
    fieldsets = (
        (None, {'fields': ('user', ('city', 'address'), 'description', 'subject', 'month_price', 'photo')}),)

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

    def get_average_rating(self, obj):
        return obj.average_rating
    get_average_rating.short_description = 'Average Rating'
    # get_average_rating.admin_order_field = 'get_average_rating'

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height: 150px;"/>', obj.photo.url)
        return "-"
    display_photo.short_description = 'Photo'

    def get_queryset(self, request):
        qs = super(TutorAdmin, self).get_queryset(request).select_related('user')
        return qs


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('student', 'tutor', 'rating')
    list_filter = [StudentFilter, TutorFilter]
    autocomplete_fields = ['student', 'tutor']
    readonly_fields = ['created_at']
    list_per_page = 25
    fieldsets = (
        (None, {'fields': (('student', 'tutor'), 'rating', 'created_at')}),)

    def get_queryset(self, request):
        qs = super(ReviewAdmin, self).get_queryset(request).select_related('student', 'tutor__user')
        return qs
