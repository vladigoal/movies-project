================
Developer readme
================

.. include:: REQUIREMENTS.rst

Local deploy
============

1. Install all requirements on system as described in REQUIREMENTS.rst.

2. Clone project to some dir::

     mkdir -p some/path
     cd some/path
     git clone git@github.com:42cc/movies-project.git

3. Create virtualenv::

     virtualenv --no-site-packages -p python2.7 .env

4. Run following commands::

     pip install -r requirements/dev.txt 
     cp Makefile.def.default Makefile.def
     cp movies/settings/local.py.default movies/settings/local.py
     make initproject

.. note::
   If you have chosen different name for virtualenv directory or using python other than 2.7
   then you should modify file movies/settings/local.py and set correct values for variables ENV_PATH and PYTHON_PATHNAME

5. To run server on localhost:8000::

     make run


Rules
=====

This rules are for real production projects. You may follow them if you like. This rules contain both python and html/css/js rules.

* Write administration info in README.rst
* use i18n everywhere. use trans in templates and views and gettext in JS
* use relative imports where possible
* do not use {% url viewname obj.pk %} . Instead setup get_absolute_url for model::
    def get_absolute_url(self):
        return ('movies.apps.core.views.profile', [unicode(self.user.username)])

* templates should be placed in apps: appname/templates/appname/yourfiles
* less
* bootstrap (less version)
* django-bootstrap-form
* Pagination sugar:  http://pypi.python.org/pypi/django-pagination/1.0.7
* autocomplete:  https://github.com/crucialfelix/django-ajax-selects or there will be custom implemintation using bootstrap js library. Еще не решено
* minification with django-compressor (наверное последний). Минификатор использовать обязательно, т.к. он будет на продакшене, и при минификации возможны проблемы (всякие глобальные переменные и прочее).
* do not use '{{ STATIC_URL }}/path' instead use tag 'static'::
  {% load static from staticfiles %}
  {% static "path" %}
* navbar menu item classes can be populated from core.context_processors


Usefull helpers
===============

cache_utils2:

  from cache_utils2 import cached, invalidate
  
  @cached(60)
  def foo(x, y=0):
      print 'foo is called'
          return x+y

Template tags
=============

libs
----

* bootstraping forms;

  {% load bootstrap %}
  {{ form|bootstrap }}
  {{ form.FIELDNAME|bootstrap }}}


Autocomplete
============

ajax_selects is used. 

HTML and CSS
============

* .centerer — text-align: center, .centerer * — text-align: left;
* .inline-block
* .offset0

Bootstrap
---------

default bootstrap classes, mixins and variables::

  .clearfix
  .center-block
  .size(@height, @width)
  .square(@size)
  .placeholder(@color: @placeholderText) 
  .hide-text
  .border-radius(@radius)
  .box-shadow(@shadow)
  .transition(@transition)
  #gradient > .vertical(@startColor: #555, @endColor: #333)
  #gradient > .horizontal(@startColor: #555, @endColor: #333)
  
  @baseFontSize
  @baseLineHeight


URLs in js
----------

You can use some django template tags in css and js. But I do not recomend doing this. Better place JS that requires django context in some django template::

  {% load url from future %}
  {% load ifsetting_tag %}
   me = "{{ STATIC_URL}}"
  
  window.MOVIES = {};
  window.MOVIES.DEBUG = false;
  {% ifsetting DEBUG %}
  window..MOVIES.DEBUG = true;
  {% endifsetting %}
  
  window.debug_log = function debug_log(){
      if (window.MOVIES.DEBUG){
          console.log(arguments)
      }
  }
  
  ajax_url = "{% url 'some_view_name' %}"


Local problems with minification and js debugging
=================================================

To disable js minification but keep django tags substitution you can add this to settings/local.py::
  COMPRESS_CSS_FILTERS = [
      'compressor.filters.template.TemplateFilter',
      'compressor.filters.css_default.CssAbsoluteFilter',
  ]
  
  COMPRESS_JS_FILTERS = [
      'compressor.filters.template.TemplateFilter',
  ]

You an also have problems with `make run`. Debug and fix this problem or run `make runserver` instead. But with `make runserver` you will need to run `make compress` on every js/css change

Makefile
========

* make fast_test — disables compression in tests.

