# -*- coding: utf-8 -*-
# welcome.urls
# 

# Following few lines is an example urlmapping with an older interface.

from kay.routing import (
    ViewGroup, Rule
)

view_groups = [
    ViewGroup(
        Rule('/', endpoint='index', view='welcome.views.index'),
        Rule('/create', endpoint='create', view='welcome.views.create'),
        Rule('/makepdf_with_conversion', endpoint='makepdf_with_conversion', view='welcome.views.makepdf_with_conversion'),
        Rule('/makepdf_with_pisa', endpoint='makepdf_with_pisa', view='welcome.views.makepdf_with_pisa'),
    )
]

