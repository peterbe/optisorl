optisorl
========

Copyright Peter Bengtsson, mail@peterbe.com, 2015-2016

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

Installation
------------

First, simply `pip install optisorl`.

Then add, in your Django settings::

    THUMBNAIL_BACKEND = 'optisorl.backend.OptimizingThumbnailBackend'

Then review the sections below about being prepared for PNGs, GIFs and JPEGs. 

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


Optimizing JPEGs
----------------

``optisorl`` uses `mozjpeg <https://github.com/mozilla/mozjpeg>`_ to
optimize JPEGs. It's a great fit because it almost never reduces
the quality such that human eyes can notice it. Especially when the
thumbnails are relatively small. The command that we use to execute
``mozjpeg`` looks like this::

    mozjpeg -outfile DESTINATION -optimise SOURCE

You can override where the executable is by setting:

.. code:: python

    # in settings.py or equivalent

    MOZJPEG_LOCATION = '/my/bin/mozjpeg'

For an example of what kind of results you can get with ``mozjpeg``
see this blog post:
`Examples of mozjpeg savings <https://www.peterbe.com/plog/examples-of-mozjpeg-savings>`_.
Also see blog post `mozjpeg installation and sample <https://www.peterbe.com/plog/mozjpeg-installation-and-sample>`_.

Limitations
-----------

Help is most welcome. At the moment...

* Does not support S3 storage

* Unable to NOT optimize images in run-time

* Not possible to override certain ``pngquant`` parameters

* Not possible to override certain ``gifsicle`` parameters

* Not possible to override certain ``mozjpeg`` parameters


.. |Travis| image:: https://travis-ci.org/peterbe/optisorl.png?branch=master
   :target: https://travis-ci.org/peterbe/optisorl
