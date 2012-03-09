# -*- coding: utf-8 -*-
"""
welcome.views
"""
import logging

from werkzeug import Response
from kay.utils import render_to_response

# Create your views here.

def index(request):
    return render_to_response('welcome/index.html', {'message': 'Hello'})

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

    def makepdf_using_pisa():

        import os
        from kay.conf import settings
        import cStringIO as StringIO

        from reportlab.pdfgen import canvas
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont

        import xhtml2pdf.pisa as pisa

        result = StringIO.StringIO()
        pdf = pisa.pisaDocument(u'<b>aaaaaaaaあ</b>', result)

        return result.getvalue()


    def makepdf_using_xml2pdf():
        import os
        from kay.conf import settings
        import cStringIO as StringIO

        from reportlab.pdfgen import canvas
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont


        result = StringIO.StringIO()
        fontname = "IPA Gothic"
        #フォントファイルを指定して、フォントを登録
        pdfmetrics.registerFont(TTFont('IPA Gothic', os.path.join(settings.STATIC_FONTS_DIR, 'ipamp.ttf')))
        c = canvas.Canvas(result)
        c.setFont(fontname, 10)
        c.drawString(100, 675, u"日本語でこんにちは！")
        c.showPage()
        c.save()

        return result.getvalue()

    return Response(makepdf_using_pisa(), status=200, content_type='application/pdf')
