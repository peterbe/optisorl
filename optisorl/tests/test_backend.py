import os
import tempfile
import shutil
import random

import mock

from django.conf import settings
from django.test import TestCase

from sorl.thumbnail.images import ImageFile
from sorl.thumbnail import default

from optisorl.backend import OptimizingThumbnailBackend


fake_pngquant_path = os.path.join(
    os.path.dirname(__file__),
    'fake-pngquant.py'
)
fake_gifsicle_path = os.path.join(
    os.path.dirname(__file__),
    'fake-gifsicle.py'
)
fake_mozjpeg_path = os.path.join(
    os.path.dirname(__file__),
    'fake-mozjpeg.py'
)
sample_png_path = os.path.join(
    os.path.dirname(__file__),
    'joyofcoding.png'
)
sample_gif_path = os.path.join(
    os.path.dirname(__file__),
    'video.gif'
)
sample_jpg_path = os.path.join(
    os.path.dirname(__file__),
    'peterbe.jpg'
)


def get_temp_dir():
    # The reason we can't use `tempfile.mkdtemp()` is because of Travis.
    # Locally, on my OSX, when I create a directory with tempfile.mkdtemp
    # it is accessible to the user who runs the subprocess command.
    # This is not the case for Travis for Python 2.7. Not sure why.
    # Using just plain `tempfile.gettempdir()` is problematic because
    # then we can't do something like `shutil.rmtree()` in the tear down
    # because we'd instead need to know each file name that was created
    # there.
    # Making our own tempdir with plain old `os.mkdir()` is a safe
    # compromise.

    def rand_str(L):
        pool = list('abcdefghijlkmnopqrstuvwxyz')
        random.shuffle(pool)
        return ''.join(pool[:L])

    name = os.path.join(
        os.path.dirname(__file__),
        'tempdir-' + rand_str(10)
    )
    os.mkdir(name)
    return name


class TestOptimizingThumbnailBackend(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestOptimizingThumbnailBackend, cls).setUpClass()
        cls.tmp_directory = get_temp_dir()
        settings.MEDIA_ROOT = cls.tmp_directory

    @classmethod
    def tearDownClass(cls):
        super(TestOptimizingThumbnailBackend, cls).tearDownClass()
        shutil.rmtree(cls.tmp_directory)

    @mock.patch('optisorl.backend.logger')
    def test_create_thumbnail_with_pngquant_location(self, logger):
        thumbnail = ImageFile(
            os.path.basename(sample_png_path),
            default.storage
        )
        size_before = os.stat(sample_png_path).st_size

        with self.settings(PNGQUANT_LOCATION=fake_pngquant_path):
            with open(sample_png_path, 'rb') as source:
                source_image = default.engine.get_image(source)
            backend = OptimizingThumbnailBackend()
            assert backend._create_thumbnail(
                source_image,
                '100x100',
                OptimizingThumbnailBackend.default_options,
                thumbnail
            )

        destination = os.path.join(
            settings.MEDIA_ROOT,
            os.path.basename(sample_png_path)
        )
        size_after = os.stat(destination).st_size
        self.assertTrue(size_after < size_before)

        message, = [x[0][0] for x in logger.info.call_args_list]
        self.assertTrue(message.startswith(
            u'Reduced joyofcoding.png '
        ), message)

    @mock.patch('optisorl.backend.logger')
    def test_create_thumbnail_with_gifsicle_location(self, logger):
        thumbnail = ImageFile(
            os.path.basename(sample_gif_path),
            default.storage
        )
        size_before = os.stat(sample_gif_path).st_size

        with self.settings(GIFSICLE_LOCATION=fake_gifsicle_path):
            with open(sample_gif_path, 'rb') as source:
                source_image = default.engine.get_image(source)
            backend = OptimizingThumbnailBackend()
            assert backend._create_thumbnail(
                source_image,
                '100x100',
                OptimizingThumbnailBackend.default_options,
                thumbnail
            )

        destination = os.path.join(
            settings.MEDIA_ROOT,
            os.path.basename(sample_gif_path)
        )
        size_after = os.stat(destination).st_size
        self.assertTrue(size_after < size_before)

        message, = [x[0][0] for x in logger.info.call_args_list]
        self.assertTrue(message.startswith(
            u'Reduced video.gif '
        ), message)

    @mock.patch('optisorl.backend.logger')
    def test_create_thumbnail_with_mozjpeg_location(self, logger):
        thumbnail = ImageFile(
            os.path.basename(sample_jpg_path),
            default.storage
        )
        size_before = os.stat(sample_jpg_path).st_size

        with self.settings(MOZJPEG_LOCATION=fake_mozjpeg_path):
            with open(sample_jpg_path, 'rb') as source:
                source_image = default.engine.get_image(source)
            backend = OptimizingThumbnailBackend()
            assert backend._create_thumbnail(
                source_image,
                '100x100',
                OptimizingThumbnailBackend.default_options,
                thumbnail
            )

        destination = os.path.join(
            settings.MEDIA_ROOT,
            os.path.basename(sample_jpg_path)
        )
        size_after = os.stat(destination).st_size
        self.assertTrue(size_after < size_before)

        message, = [x[0][0] for x in logger.info.call_args_list]
        self.assertTrue(message.startswith(
            u'Reduced peterbe.jpg '
        ), message)
