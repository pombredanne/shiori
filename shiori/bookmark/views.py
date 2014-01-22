# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('bookmark/index.html',
                              {'is_authenticated':
                               request.user.is_authenticated()},
                              context_instance=RequestContext(request))


def profile(request):
    return render_to_response('bookmark/profile.html',
                              {'is_authenticated':
                               request.user.is_authenticated()},
                              context_instance=RequestContext(request))


def categories(request):
    return render_to_response('bookmark/categories.html',
                              {'is_authenticated':
                               request.user.is_authenticated()},
                              context_instance=RequestContext(request))


def category(request, category_id):
    return render_to_response('bookmark/category.html',
                              {'is_authenticated':
                               request.user.is_authenticated()},
                              context_instance=RequestContext(request))


def tags(request):
    return render_to_response('bookmark/tags.html',
                              {'is_authenticated':
                               request.user.is_authenticated()},
                              context_instance=RequestContext(request))


def tag(request, tag_id):
    return render_to_response('bookmark/tag.html',
                              {'is_authenticated':
                               request.user.is_authenticated()},
                              context_instance=RequestContext(request))
