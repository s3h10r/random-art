#!/usr/bin/env python
#coding=utf-8

# === einguteswerkzeug plugin-interface ===
# --- all einguteswerkzeug-plugins (generators, filters) must implement this
import logging
import string

name = "psychedelic"
description = "Random (Psychedelic) Art"
kwargs = {'pixels_per_unit' : 150, 'seed' : None}
args=None
author = "Jeremy Kun http://jeremykun.com/2012/01/01/random-psychedelic-art/"
version = '0.4.0'

def run(**kwargs):
    """
    this is the wrapper around the functionality of the plugin.
    """
    if not kwargs:
        # use default values
        return _generate_image()
    else:
        return _generate_image(**kwargs)

# --- END all einguteswerkzeug-plugins (generators, filters) must implement this

def get_plugin_doc(format='text'):
    """
    """
    if format not in ('txt', 'text', 'plaintext'):
        raise Exception("Sorry. format %s not available. Valid options are ['text']" % format)
    tpl_doc = string.Template("""
    filters.$name - $description
    kwargs  : $kwargs
    args    : $args
    author  : $author
    version : __version__
    """)
    return tpl_doc.substitute({
        'name' : name,
        'description' : description,
        'kwargs' : kwargs,
        'args'    : args,
        'author'  : author,
        'version' : __version__,
        })

if __name__ == '__main__':
    print(get_plugin_doc())

# === END einguteswerkzeug plugin-interface

# --- .. here comes the plugin-specific part to get some work done...
from .randomart import generate_image as _generate_image
