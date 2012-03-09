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
        Rule('/makepdf', endpoint='makepdf', view='welcome.views.makepdf'),
    )
]

