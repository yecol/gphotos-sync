#!/bin/env python
# -*- coding: utf-8 -*-
import os,time,datetime,sys
import shutil
import logging
from pathlib import Path

from gphotos.LocalFilesMedia import LocalFilesMedia

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

try:
     path = Path("../photostream/photos/2022-03/_dsc0624.jpg")
     lf = LocalFilesMedia(path)
     logger.info("indexed local file: %s %s %s %s, desc=%s %s",
                    lf.relative_folder,
                    lf.filename,
                    lf.camera_model,
                    lf.uid,
                    lf.description,
                    lf.exif,
                )
except Exception:
        logger.error("file %s could not be made into a media obj", path, exc_info=True)
# local_file = LocalFilesMedia("")
