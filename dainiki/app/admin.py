from django.contrib import admin

# Register your models here.

from .models import Post,Banner,Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
  list_display = ("title",)
  prepopulated_fields = {"slug": ("title",)}
admin.site.register(Post,PostAdmin)
admin.site.register(Banner)
admin.site.register(Category)
