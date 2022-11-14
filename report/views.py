from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
from django.db import connection
from report.models import *

from django.db import connection

# Create your views here.
from django.http import JsonResponse

# def index(request):
#     invoice_no = request.GET.get('inv','')
#     dataReport = dict()
#     dataReport['invoice'] = list(Invoice.objects.filter(invoice_no=invoice_no).values())
#     dataReport['invoice_line_item'] = list(InvoiceLineItem.objects.filter(invoice_no=invoice_no).values())
#     #dataReport['payment_method'] = list(PaymentMethod.objects.filter(PaymentMethod=PaymentMethod).values())
#     #return JsonResponse(dataReport)
#     return render(request, 'report_data.html', dataReport)

#list(Invoice.objects.filter(invoice_no=invoice_no).select_related('customer_code').values('customer_code__name'))
#'invoice_no', 'date', 'customer_code_id', 'customer_code__name','due_date','total','vat','amount_due

def Category(request):
#     dataReport = dict()
#     dataReport['data'] = list(Data.objects.all().values())
#     return JsonResponse(dataReport)
    return render(request, 'category.html')

def about(request):
    return render(request, 'about.html')

def Food(request):

    # cursor = connection.cursor()
    # cursor.execute ('SELECT name_food as "Name Food", urls_food as "URLs_Food" '
    #                 ' FROM food '
    #                 )
    # dataReport = dict()
    # columns = [col[0] for col in cursor.description]
    # data = cursor.fetchall()
    # dataReport['column_name'] = columns
    # dataReport['data'] = CursorToDict(data,columns)

    return render(request, 'food.html')

def ReportListAllProducts(request):

    dataReport = dict()
    data = list(Product.objects.all().values())
    columns = ("Code", "Name", "Units", "Product Type")
    dataReport['column_name'] = columns
    dataReport['data'] = data

    return render(request, 'report_list_all_products.html', dataReport)

def ReportListAllInvoices(request):
    cursor = connection.cursor()
    cursor.execute ('SELECT i.invoice_no as "Invoice No", i.date as "Date" '
                             ' , i.customer_code as "Customer Code", c.name as "Customer Name" '
                             ' , i.due_date as "Due Date", i.total as "Total", i.vat as "VAT", i.amount_due as "Amount Due" '
                             ' , ili.product_code as "Product Code", p.name as "Product Name" '
                             ' , ili.quantity as "Quantity", ili.unit_price as "Unit Price", ili.product_total as "Extended Price" '
                             ' FROM invoice i JOIN customer c ON i.customer_code = c.customer_code '
                             '  JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                             '  JOIN product p ON ili.product_code = p.code '
                             ' ')
    dataReport = dict()
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    dataReport['column_name'] = columns
    dataReport['data'] = CursorToDict(data,columns)

    return render(request, 'report_list_all_invoices.html', dataReport)

def ReportProductsSold(request):

    cursor = connection.cursor()
    cursor.execute ('SELECT ili.product_code as "Product Code", p.name as "Product Name" '
                    ' , SUM(ili.quantity) as "Total Quantity Sold", SUM(ili.product_total) as "Total Value Sold" '
                    ' FROM invoice i JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                    '   JOIN product p ON ili.product_code = p.code '
                    ' GROUP BY p.code, ili.product_code, p.name '
                    ' ')
    dataReport = dict()
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    dataReport['column_name'] = columns
    dataReport['data'] = CursorToDict(data,columns)

    return render(request, 'report_products_sold.html', dataReport)

def CursorToDict(data,columns):
    result = []
    fieldnames = [name.replace(" ", "_").lower() for name in columns]
    for row in data:
        rowset = []
        for field in zip(fieldnames, row):
            rowset.append(field)
        result.append(dict(rowset))
    return result


def ReportListAllReceipts(request):

    cursor = connection.cursor()
    cursor.execute ('SELECT receipt_no as "Receipt No", date as "Date", customer_code as"Customer Code" '
                    ' , payment_method as "Payment Method", payment_reference as "Payment Reference", total_received as "Total Received", remarks as "Remarks '
                    ' FROM receipt '
                    )
    dataReport = dict()
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    dataReport['column_name'] = columns
    dataReport['data'] = CursorToDict(data,columns)

    return render(request, 'report_list_all_receipt.html', dataReport)

# def payment_method(request):
#     cursor = connection.cursor()
#     cursor.execute ('SELECT  payment_method as "Payment Method", description as "Description" '
#                     ' FROM payment_method '
#                     )
#     dataReport = dict()
#     columns = [col[0] for col in cursor.description]
#     data = cursor.fetchall()
#     dataReport['column_name'] = columns
#     dataReport['data'] = CursorToDict(data,columns)
#     return render(request, 'report_data.html', dataReport)

#     invoice_no = request.GET.get('inv','')
#     dataReport = dict()
#     dataReport['invoice'] = list(Invoice.objects.filter(invoice_no=invoice_no).values())
#     dataReport['invoice_line_item'] = list(InvoiceLineItem.objects.filter(invoice_no=invoice_no).values())
#     #return JsonResponse(dataReport)
#     return render(request, 'report_data.html', dataReport)

    