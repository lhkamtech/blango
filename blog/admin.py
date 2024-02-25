from django.contrib import admin

# Register your models here.

from blog.models import Tag, Post, Comment, AuthorProfile
admin.site.register(Tag)

# Custom approach (configure how the admin site behaves)
class PostAdmin(admin.ModelAdmin):
    # "Slugify" the title field into the slug field whenever the title
    # field changes (inserts some JavaScript to do this)
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "slug", "published_at"]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(AuthorProfile)
