from admin_auto_filters.filters import AutocompleteFilter


class StudentFilter(AutocompleteFilter):
    title = 'Student'
    field_name = 'student'


class TutorFilter(AutocompleteFilter):
    title = 'Tutor'
    field_name = 'tutor'
