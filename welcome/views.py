# -*- coding: utf-8 -*-
"""
welcome.views
"""
import logging

from werkzeug import (
    Response, redirect
)

from kay.utils import (
    render_to_response, url_for
)
from welcome.forms import DocForm

def index(request):

    form = DocForm()

    return render_to_response('welcome/index.html', {
        'form': form.as_widget(),
    })


def create(request):

    form = DocForm()
    if request.method == 'POST' and form.validate(request.form):

        from common.utils import pdfcreator
        return Response(pdfcreator.create(form['doc']), status=200, content_type='application/pdf')

    else:
        return redirect(url_for('welcome/index'))


def makepdf_with_conversion(request):

    def test_conversion():
        from google.appengine.api import conversion

        asset = conversion.Asset('text/html', u'<html><head><meta charset=\'utf-8\'></head><body>testtest<br/>てすと</body></head></html>'.encode('utf-8'), 'index.html')
        conversion_obj = conversion.Conversion(asset, 'application/pdf')

        # async
        #rpc = conversion.create_rpc()
        #conversion.make_convert_call(rpc,  conversion_obj)
        #result = rpc.get_result()

        result = conversion.convert(conversion_obj)
        if result.assets:
            return result.assets[0].data
        else:
            raise 

    return Response(test_conversion(), status=200, content_type='application/pdf')


def makepdf_with_pisa(request):

    doc = u"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
    </head>
    <body>
        <h1>あいうえお</h1>
        <hr/>
        <div style="border-color: black">aaaaaaaaaa</div>
    </body>
</html>
    """

    from common.utils import pdfcreator
    return Response(pdfcreator.create(doc), status=200, content_type='application/pdf')
