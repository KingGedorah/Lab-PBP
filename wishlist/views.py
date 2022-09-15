from tkinter import N
from xml.dom import NotFoundErr
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Naufal',
    }
    return render(request, "wishlist.html", context)
    
    
def show_xml(request):
    data = BarangWishlist.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangWishlist.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = BarangWishlist.objects.filter(pk=id)

    if (id == 1) :
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    elif (id == 2) :
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    elif (id == 3) :
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = BarangWishlist.objects.filter(pk=id)

    if (id == 1) :
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    elif (id == 2) :
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    elif (id == 3) :
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
