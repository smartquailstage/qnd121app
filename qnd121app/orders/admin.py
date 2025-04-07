import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from .models import Order, OrderItem
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.db.models import Count
from django.views.generic import ListView

from django.contrib.postgres.fields import ArrayField
from django.db import models
#from parler.admin import TranslatableAdmin
#from wagtail_modeladmin.options import ModelAdmin, modeladmin_register,ModelAdminGroup
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import ArrayWidget, WysiwygWidget



def order_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(
        reverse('orders:admin_order_detail', args=[obj.id])))

 
def export_to_csv(modeladmin, request, queryset): 
    opts = modeladmin.model._meta 
    response = HttpResponse(content_type='text/csv') 
    response['Content-Disposition'] = 'attachment;' \
        'filename={}.csv'.format(opts.verbose_name) 
    writer = csv.writer(response) 
     
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many] 
    # Write a first row with header information 
    writer.writerow([field.verbose_name for field in fields]) 
    # Write data rows 
    for obj in queryset: 
        data_row = [] 
        for field in fields: 
            value = getattr(obj, field.name) 
            if isinstance(value, datetime.datetime): 
                value = value.strftime('%d/%m/%Y') 
            data_row.append(value) 
        writer.writerow(data_row) 
    return response 
export_to_csv.short_description = 'Export to CSV' 


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    readonly_fields = ['price','quantity','order','product']


def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('orders:admin_order_pdf', args=[obj.id])))
order_pdf.short_description = 'Invoice'

def whatsapp(obj):
     return mark_safe('<a href="https://api.whatsapp.com/send?phone={}"><i><i class="fa fa-phone"></i></a>'.format(obj.phone))
whatsapp.short_description = 'Send Mail'

def email(obj):
     return mark_safe('<a href="mailto:{}" target="_blank" ><i class="fa fa-envelope"></i></a>'.format(obj.email))
whatsapp.short_description = 'Whatsapp'


class OrderListView(ListView):
    paginate_by = 2
    model = Order



@admin.register(Order)
class OrderAdminClass(ModelAdmin):
    # Display fields in changeform in compressed mode
    list_display = [ 'full_name', 
                    'arrival_date_time','departure_date_time', 'paid','total_cost',
                   email,whatsapp ]
    list_filter = ['arrival_date_time','departure_date_time','paid', 'created', 'updated']
    date_hierarchy = 'arrival_date_time'
    readonly_fields = ['first_name','last_name','arrival_date_time','departure_date_time','paid','email','total','discount','agree_term','coupon','braintree_id']
    list_per_page = 10

    compressed_fields = True  # Default: False
    inlines = [OrderItemInline]
    actions = [export_to_csv]

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }

    # Display submit button in filters
    list_filter_submit = False

    # Display changelist in fullwidth
    list_fullwidth = False

    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = True

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    # Changeform templates (located inside the form)
    #change_form_before_template = "some/template.html"
    #change_form_after_template = "some/template.html"

    # Located outside of the form
    #change_form_outer_before_template = "some/template.html"
    #change_form_outer_after_template = "some/template.html"

    # Display cancel button in submit line in changeform
    change_form_show_cancel_button = True # show/hide cancel button in changeform, default: False

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        }
    } 

    def total_cost(self, obj):
        return obj.total

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(total_cost=Count("total"))
        return queryset

