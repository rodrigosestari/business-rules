__version__ = '1.0.16'

import logging
from .engine import run_all, get_value
from .utils import export_rule_data

# Appease pyflakes by "using" these exports
assert run_all
assert export_rule_data

logging.getLogger(__name__).addHandler(logging.NullHandler())
