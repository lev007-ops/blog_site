from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'cre_date', 'was_published_recently')
    fieldsets = (
        (None, {
            "fields": (
                'title', 'text'
            ),
        }),
        ('Date info', {'fields': ('cre_date',)})
    )

    list_filter = ('cre_date',)
    search_fields = ('title', 'text')


admin.site.register(Post, PostAdmin)
