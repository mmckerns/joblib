#!/bin/sh
# Do a local install of dill.

pip install --target=. dill
rm -rf *.egg-info
find dill -name "*.py" | xargs sed -i.bak "s/from dill\(\.\)\{0,1\}/from ./"
find dill -name "*.bak" | xargs rm
