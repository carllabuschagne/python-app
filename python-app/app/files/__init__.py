# -*- encoding: utf-8 -*-
"""
Copyright (c) 2025 - CustomData
"""

from flask import Blueprint

blueprint = Blueprint(
    'files_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)
