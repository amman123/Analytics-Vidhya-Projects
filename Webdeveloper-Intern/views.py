from django.shortcuts import render

# Create your views here.

def index(request):
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
         )
def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) 
    writer.writerow([
        smart_str(u"Serial_id"),
        smart_str(u"mail"),
        smart_str(u"name"),
        smart_str(u"Phonenumber"),
        smart_str(u"Curent_location"),
        smart_str(u"Experience"),
        smart_str(u"skills"),
 
     
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
             smart_str(obj.Serial_id"),
        smart_str(obj.mail),
        smart_str(obj.name),
        smart_str(obj.Phonenumber),
        smart_str(obj.Curent_location),
        smart_str(obj.Experience),
        smart_str(obj.skills), ])
    return response
export_csv.short_description = u"Export CSV"
