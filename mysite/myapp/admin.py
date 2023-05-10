from django.contrib import admin
from .models import CSVData

admin.site.site_header="UNEXPECTED IMPORT"
admin.site.index_title = "USER DATA "
class CSVDataAdmin(admin.ModelAdmin):
    
    list_display = ('Index','M2_Declaration_Number','CIF_Value','unit_price','Test','Test2')
    search_fields = ('Index','M2_Declaration_Number',) #search bar 
    fields = ('Index','M2_Declaration_Number','Test','Test2') #display only required field 
admin.site.register(CSVData,CSVDataAdmin)