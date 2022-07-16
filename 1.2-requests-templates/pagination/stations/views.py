from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

import pagination.settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_stations = []
    with open(pagination.settings.BUS_STATION_CSV, 'r', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        for line in file_reader:
            dict_write = {}
            for key, val in line.items():
                if key in ['Name', 'Street', 'District']:
                    dict_write[key] = val
            bus_stations.append(dict_write)
    paginator = Paginator(bus_stations, 25)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    context = {
            'page': page,
            'bus_stations': bus_stations,
            'title': 'Пагинация',
    }
    return render(request, 'stations/index.html', context)
