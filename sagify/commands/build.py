# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import sys

import click

from sagify.api import build as api_build
from sagify.commands import ASCII_LOGO
from sagify.log import logger

click.disable_unicode_literals_warning = True


@click.command()
@click.option(u"-d", u"--dir", required=False, default='.', help="Path to sagify module")
@click.option(u"-r", u"--requirements-dir", required=True, help="Path to requirements.txt file")
def build(dir, requirements_dir):
    """
    Command to build SageMaker app
    """
    logger.info(ASCII_LOGO)
    logger.info("Started building SageMaker Docker image. It will take some minutes...\n")

    try:
        api_build.build(dir=dir, requirements_dir=requirements_dir)

        logger.info("Docker image built successfully!")
    except ValueError:
        logger.info("This is not a sagify directory: {}".format(dir))
        sys.exit(-1)
    except Exception as e:
        logger.info("{}".format(e))
        return
