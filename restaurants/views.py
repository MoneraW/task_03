from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    mylist = [{ 'restaurant_name': 'ovo',
    'food_type': 'vegan'
    },
    { 'restaurant_name': 'table otto',
    'food_type': 'fancy'
    },
    { 'restaurant_name': 'joa',
    'food_type': 'sushi'
    }]

    context = { 'rest': mylist
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    myobject = {'restaurant_name': 'joa',
        'food_type': 'sushi',
        'desc': 'california roll'}
    context = { 'rest': myobject

    }
    return render(request, 'detail.html', context)
