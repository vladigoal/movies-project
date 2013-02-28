================
Developer readme
================


Local deploy
============

Create virtualenv as usual. Then run::
  pip install -r requirements/dev.txt 
  cp Makefile.def.default Makefile.def
  cp movies/settings/local.py.default movies/settings/local.py
  make initproject

Settings also need to know where virtualenvironment is located, so edit file $PROJ_NAME/settings/local.py::
     
     ENV_PATH = proj('.env2.6') # this leads to $PROJ_ROOT/.env2.6, you may need another path, you can also use full path as string
     PYTHON_PATHNAME = 'python2.6'
     # assuming you have python 2.6. But you may use 2.7 too


to work with spatial data you will need spatialite for sqlite or PostGIST for PostgreSQL. MySQL database may not work.


Forcing js recollection on every request
========================================

1. add 'IS_DEV = True' to your settings
2. Run development server with command run_collecting (or just `make run`) 


Rules
=====

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

You can use some django template tags in css and js. But I do not recomend doing this. Better place some JS in base.html::

  {% load url from future %}
  {% load ifsetting_tag %}
   me = "{{ STATIC_URL}}"
  
  window.AW_DEBUG = false;
  {% ifsetting DEBUG %}
  window.AW_DEBUG = true;
  {% endifsetting %}
  
  window.debug_log = function debug_log(){
      if (window.AW_DEBUG){
          console.log(arguments)
      }
  }
  
  ajax_url = "{% url 'linkedin_experience' %}"


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

