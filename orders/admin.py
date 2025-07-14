from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('get_cost',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'first_name', 'last_name', 'email', 'paid', 'created')
    list_filter = ('paid', 'created', 'store')
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('created', 'updated')
    inlines = [OrderItemInline]
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('store')

admin.site.register(Order, OrderAdmin)
