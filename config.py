#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
ASSETS_DEBUG = False

CACHE_TYPE = 'memcached'
CACHE_KEY_PREFIX = 'emulator_dev'

ADMINS = frozenset(['matteson@obstructures.org'])
SECRET_KEY = 'REPLACEME'