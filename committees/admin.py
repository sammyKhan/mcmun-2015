from django.contrib import admin

from committees.models import *


class CommitteeAssignmentAdmin(admin.ModelAdmin):
    list_display = ('school', 'committee', 'assignment', 'position_paper')
    search_fields = ('school__school_name', 'committee__name', 'assignment')


class DelegateAssignmentAdmin(admin.ModelAdmin):
    list_display = ('school', 'committee', 'committee_assignment', 'delegate_name')
    search_fields = (
        'committee_assignment__school__school_name',
        'committee_assignment__committee__name',
        'committee_assignment__assignment',
        'delegate_name'
    )

    def school(self, obj):
        return "%s" % obj.committee_assignment.school
    school.short_description = 'School'
    school.admin_order_field  = 'committee_assignment__school'

    def committee(self, obj):
        return "%s" % obj.committee_assignment.committee
    committee.short_description = 'Committee'
    committee.admin_order_field = 'committee_assignment__committee'


class CommitteeAssignmentInline(admin.StackedInline):
    model = CommitteeAssignment
    extra = 5
    exclude = ('position_paper',)


class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class AwardAssignmentAdmin(admin.ModelAdmin):
    list_display = ('position', 'award', 'committee', 'school')
    list_per_page = 112  # show all the awards on one page

    def school(self, obj):
        if obj.position:
            return "%s" % obj.position.school
        else:
            return "(None)"
    school.short_description = 'School'
    school.admin_order_field  = 'position__school'

admin.site.register(Category)
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(AdHocApplication)
admin.site.register(NcaaApplication)
admin.site.register(NintendoApplication)
admin.site.register(CriminalCourtApplication)
admin.site.register(EnronApplication)
admin.site.register(CommitteeAssignment, CommitteeAssignmentAdmin)
admin.site.register(DelegateAssignment, DelegateAssignmentAdmin)
admin.site.register(Award)
admin.site.register(AwardAssignment, AwardAssignmentAdmin)
