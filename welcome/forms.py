# -*- coding: utf-8 -*-
from kay.utils import forms

class DocForm(forms.Form):
    doc = forms.TextField(widget=forms.Textarea, required=True)

