import logging
import time
import subprocess
import os

from django.conf import settings

from sorl.thumbnail.base import ThumbnailBackend


logger = logging.getLogger('optisorl')


class OptimizingThumbnailBackend(ThumbnailBackend):

    def _create_thumbnail(
        self,
        source_image,
        geometry_string, options,
        thumbnail
    ):
        """override so we have an opportunity to first optimize the
        resulting thumbnail before it gets saved."""
        super(OptimizingThumbnailBackend, self)._create_thumbnail(
            source_image,
            geometry_string, options,
            thumbnail
        )
        image_path = os.path.join(settings.MEDIA_ROOT, thumbnail.name)
        if os.path.isfile(image_path):
            if image_path.lower().endswith('.png'):
                self.optimize_png(image_path)
            elif image_path.lower().endswith('.gif'):
                self.optimize_gif(image_path)
            elif image_path.lower().endswith('.jpg'):
                self.optimize_jpg(image_path)

    def optimize_png(self, path):
        binary_location = getattr(
            settings,
            'PNGQUANT_LOCATION',
            'pngquant'
        )
        if not binary_location:
            # it's probably been deliberately disabled
            return
        tmp_path = path.lower().replace('.png', '.tmp.png')
        size_before = os.stat(path).st_size
        command = [
            binary_location,
            '-o', tmp_path,
            '--skip-if-larger',
            '--',
            path,
        ]
        time_before = time.time()
        out, err = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).communicate()
        time_after = time.time()
        # Because we use --skip-if-larger, when you resize an already
        # small PNG the resulting one might not be any smaller so you
        # can't guarantee that the new file was created.
        if not os.path.isfile(tmp_path):
            return
        os.rename(tmp_path, path)
        size_after = os.stat(path).st_size
        logger.info(
            'Reduced %s from %d to %d (took %.4fs)' % (
                os.path.basename(path),
                size_before,
                size_after,
                time_after - time_before
            )
        )

    def optimize_gif(self, path):
        binary_location = getattr(
            settings,
            'GIFSICLE_LOCATION',
            'gifsicle'
        )
        if not binary_location:
            # it's probably been deliberately disabled
            return
        tmp_path = path.lower().replace('.gif', '.tmp.gif')
        size_before = os.stat(path).st_size
        command = [
            binary_location,
            '-O3', path,
            '-o', tmp_path,
        ]
        time_before = time.time()
        out, err = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).communicate()
        time_after = time.time()
        if not os.path.isfile(tmp_path):
            return
        os.rename(tmp_path, path)
        size_after = os.stat(path).st_size
        logger.info(
            'Reduced %s from %d to %d (took %.4fs)' % (
                os.path.basename(path),
                size_before,
                size_after,
                time_after - time_before
            )
        )

    def optimize_jpg(self, path):
        binary_location = getattr(
            settings,
            'MOZJPEG_LOCATION',
            'mozjpeg'
        )
        if not binary_location:
            # it's probably been deliberately disabled
            return
        tmp_path = path.lower().replace('.jpg', '.tmp.jpg')
        size_before = os.stat(path).st_size
        command = [
            binary_location,
            '-outfile', tmp_path,
            '-optimise', path,
        ]
        time_before = time.time()
        out, err = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        ).communicate()
        time_after = time.time()
        if not os.path.isfile(tmp_path):
            return
        os.rename(tmp_path, path)
        size_after = os.stat(path).st_size
        logger.info(
            'Reduced %s from %d to %d (took %.4fs)' % (
                os.path.basename(path),
                size_before,
                size_after,
                time_after - time_before
            )
        )
