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


.. |Travis| image:: https://travis-ci.org/peterbe/optisorl.png?branch=master
   :target: https://travis-ci.org/peterbe/optisorl
