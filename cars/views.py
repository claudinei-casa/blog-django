from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from .models import Cars, Brands, Opt
from django.views.decorators.http import require_http_methods
from .forms import CreateCar
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        forms = CreateCar(request.POST)
        if forms.is_valid():
            forms.save()
        else:
            return render(request, "create.html", context={'form': forms})
    return render(request, "create.html", context={'form': CreateCar})


@login_required(login_url="/login/")
def delete_car(request, pk):
    user = request.user
    car = Cars.objects.get(pk=pk)
    if user == car.usr:
        car.delete()
    return HttpResponseRedirect('/cars/')


def read(request):
    cars = Cars.objects.all()
    # .values('id', 'brand', 'model', 'year', 'color', 'price', 'usr')
    # return JsonResponse({'cars': list(cars)})
    return render(request, "cars_list.html", context={'cars': cars})


@login_required(login_url='/login/')
def cars_detail(request, id):
    car = Cars.objects.get(id=id)
    opts = Cars.objects.get(id=id).opt.all()
    return render(request, "cars_detail.html", context={'car': car, 'opts': opts})


@login_required(login_url="/login/")
def update(request, pk):
    transaction = Cars.objects.get(pk=pk)
    forms = CreateCar(request.POST or None, instance=transaction)
    if forms.is_valid():
        forms.save()
        return render(request, "create.html", context={'form': CreateCar})
    else:
        return render(request, "create.html", context={'form': forms})


@login_required(login_url="/login/")
def create_brand(request):
    if request.method == 'POST':
        brand = Brands(brand=request.POST['brand'])
        brand.save()
    return render(request, "create_brand.html")


def create_opt(request):
    if request.method == 'POST':
        opt = request.POST.get('opt')
        Opt.objects.create(
            opt=opt,
        )
    return render(request, "create_opt.html")

# @login_required(login_url="/login/")
# def update(request, id):
#     id = request.GET.get('id')
#     data = {}
#     if id:
#         data['car'] = Cars.objects.get(id=id)
#         return render(request, "update.html", data)


# pegando dados sem form
# def create(request):
#     if request.method == "POST":
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         image = request.POST.get('image')
#         color = request.POST.get('color')
#         year = request.POST.get('year')
#         Cars.object.create(
#             title=title,
#             description=description,
#             price=price, image=image,
#             color=color,
#             year=year
#         )
#         return HttpResponseRedirect('/cars/')
