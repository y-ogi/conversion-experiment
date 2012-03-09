# -*- coding: utf-8 -*-
"""
welcome.views
"""
import logging

from werkzeug import Response
from kay.utils import render_to_response


# Create your views here.

def test_conversion():
    from google.appengine.api import conversion

    asset = conversion.Asset('text/html', '<b>some data</b>', 'index.html')
    conversion_obj = conversion.Conversion(asset, 'image/png')

    rpc = conversion.create_rpc()
    conversion.make_convert_call(rpc,  conversion_obj)

    result = rpc.get_result()
    if result.assets:
        return result.assets[0].data
    else:
        raise 

def index(request):
    return render_to_response('welcome/index.html', {'message': 'Hello'})

def makepdf(request):
    return Response(test_conversion(), status=200)