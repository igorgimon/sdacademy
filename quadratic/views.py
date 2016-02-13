# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render
import math


def quadratic_results(request):

    def check(argument):
        if argument == '':
            return 'коэффициент не определен'
        try:
            int(argument)
        except ValueError:
            return 'коэффициент не целое число'

    a = request.GET['a']
    errmessage_a = check(a)
    if a == '0':
        errmessage_a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
             
    b = request.GET['b']
    errmessage_b = check(b)

    c = request.GET['c']
    errmessage_c = check(c)
    
    discr = None
    x1 = None
    x2 = None
    message_discr = None
    if a != '0':
        try:
            discr = int(b)*int(b) - 4*int(a)*int(c)
            if discr < 0:
                message_discr = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            elif discr == 0:
                x1 = -int(b)/(2*int(a))
                message_discr = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень x = %d:' % x1
            else:
                x1 = (-int(b) + math.sqrt(discr))/(2*int(a))
                x2 = (-int(b) - math.sqrt(discr))/(2*int(a))
                message_discr = 'Квадратное уравнение имеет два действительных корня: x1 = %d, x2 = %d' % (x1, x2)
        except ValueError:
            pass
    return render(request, 'results.html', {
        'a' : a,
        'b' : b,
        'c' : c,
        'errmessage_a': errmessage_a,
        'errmessage_b': errmessage_b,
        'errmessage_c': errmessage_c,
        'discr': discr,
        'message_discr': message_discr,
        'x1': x1,
        'x2': x2,
        })
        
      


