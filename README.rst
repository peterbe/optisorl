optisorl
========

Copyright Peter Bengtsson, mail@peterbe.com, 2015

|Travis|

License: BSD

About optisorl
--------------

`sorl-thumbnail <https://pypi.python.org/pypi/sorl-thumbnail>`_ is a
great Django library that takes your stored images and automatically
convert them into desired sized thumbnails and store them with nice
names in the ``MEDIA_ROOT``. The problem is that the engines that do
the resizing often doesn't do an amazing job of optimizing them.
Usually optimizing an image means carefully deleting things the human
eye can't notice anyway. This becomes incredibly relevant when the
thumbnail you create is so small in resolution that the user really
stands very little chance to notice.

This package, is a pluggable backend to ``sorl-thumbnail`` that
attempts to do a good job of optimizing the generated thumbnail just
right after it has been written to disk.


Optimizing PNGs
---------------

``optisorl`` uses a binary called `pngquant <https://pngquant.org/>`_
which is a command line tool that do lossy compression of PNG images
and supports alpha transparency. ``pngquant`` is
BSD licensed. It's easy to install on most systems. For example
``brew install pngquant`` or ``apt-get install pngquant``.

What happens is that when ``optisorl`` notices that a thumbnail was
created it (and stored in ``MEDIA_ROOT``) it then takes that file and
executes ``pngquant`` something like this:

::

    pngquant -o /path/file.tmp.png --skip-if-larger -- /path/file.png

Note the ``--skip-if-larger`` which means that if the thumbnail is really
really small already the resulting optimization might not be any better
and it thus omits doing an optimization.

If you want to override the location of the executable ``pngquant`` you
can set this setting for example:

.. code:: python

    # in settings.py or equivalent

    PNGQUANT_LOCATION = '/opt/special/bin/pngquant2.0'


Optimizing GIFs
---------------

``optisorl`` uses `gifsicle <http://www.lcdf.org/gifsicle/>`_ with
level 3 optimization. ``gifsicle`` is GPL licensed but use is not
restricted by a license. To install it use ``brew install gifsicle``
or ``apt-get install gifsicle``.

To override where the ``gifsicle`` executable is located you can set
in your settings:

.. code:: python

    # in settings.py or equivalent

    GIFSICLE_LOCATION = '/opt/special/bin/gifsicle'


If you want to disable all optimization of GIFs just set
``GIFSICLE_LOCATION`` (in your ``settings.py``) to ``None`` or ``False``.

Limitations
-----------

Help is most welcome. At the moment...

* Does not support S3 storage

* Unable to NOT optimize images

* Not possible to override certain ``pngquant`` parameters

* Only able to optimize ``.png`` thumbnails


.. |Travis| image:: https://travis-ci.org/peterbe/optisorl.png?branch=master
   :target: https://travis-ci.org/peterbe/optisorl
