# -*- coding: utf-8 -*-
import os
from kay.conf import settings
import cStringIO as StringIO

def create(doc):

    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    import xhtml2pdf.pisa as pisa


    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(doc, result)

    return result.getvalue()


"""
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
"""
