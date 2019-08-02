#!/usr/bin/env python3
#coding=utf-8
import logging
import random
import string
import sys
from PIL import Image, ImageDraw
from einguteswerkzeug.plugins import EGWPluginGenerator

# --- configure logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.StreamHandler() # console-handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
# ---

meta = {
    "name" : "psychedelic",
    "version" : "0.4.1",
    "description" : "Random (Psychedelic) Art",
    "author" : "Jeremy Kun http://jeremykun.com/2012/01/01/random-psychedelic-art/"
}

class Psychedelic(EGWPluginGenerator):
    def __init__(self, **kwargs):
        super().__init__(**meta)
        # defining mandatory kwargs (addionals to the mandatory of the base-class)
        add_plugin_kwargs = { 'pixels_per_unit' : 150,
                              'seed' : random.randrange(sys.maxsize) }
        self._define_mandatory_kwargs(self, **add_plugin_kwargs)
        self.kwargs = kwargs

    def _generate_image(self):
        return _create_psychedelic(**self.kwargs)


generator = Psychedelic()
assert isinstance(generator,EGWPluginGenerator)

# --- .. here comes the plugin-specific part to get some work done...

from .randomart import generate_image as _create_psychedelic
