import os
import tempfile
import shutil

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
sample_png_path = os.path.join(
    os.path.dirname(__file__),
    'joyofcoding.png'
)
sample_gif_path = os.path.join(
    os.path.dirname(__file__),
    'video.gif'
)


class TestOptimizingThumbnailBackend(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestOptimizingThumbnailBackend, cls).setUpClass()
        cls.tmp_directory = tempfile.mkdtemp()
        settings.MEDIA_ROOT = cls.tmp_directory

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp_directory)
        super(TestOptimizingThumbnailBackend, cls).tearDownClass()

    def test_create_thumbnail_with_pngquant_location(self):
        thumbnail = ImageFile(
            os.path.basename(sample_png_path),
            default.storage
        )
        size_before = os.stat(sample_png_path).st_size

        with self.settings(PNGQUANT_LOCATION=fake_pngquant_path):
            with open(sample_png_path, 'rb') as source:
                source_image = default.engine.get_image(source)
            backend = OptimizingThumbnailBackend()
            backend._create_thumbnail(
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

    def test_create_thumbnail_with_gifsicle_location(self):
        thumbnail = ImageFile(
            os.path.basename(sample_gif_path),
            default.storage
        )
        size_before = os.stat(sample_gif_path).st_size

        with self.settings(GIFSICLE_LOCATION=fake_gifsicle_path):
            with open(sample_gif_path, 'rb') as source:
                source_image = default.engine.get_image(source)
            backend = OptimizingThumbnailBackend()
            backend._create_thumbnail(
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
