from ..randomart import generate_image as _generate_image
# --- all polaroidme-plugins (generators, filters) must implement this
name = "psychedelic"
description = "Random (Psychedelic) Art"
kwargs = {'pixels_per_unit' : 150, 'seed' : None}
args=None
author = "Jeremy Kun http://jeremykun.com/2012/01/01/random-psychedelic-art/"
version = '0.2.0'

def run(**kwargs):
    """
    this is the wrapper around the functionality of the plugin.
    """
    if not kwargs:
        # use default values
        return _generate_image()
    else:
        return _generate_image(**kwargs)
# --- END all polaroidme-plugins (generators, filters) must implement this
