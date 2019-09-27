import json
import os
import sys
import subprocess
from distutils.version import StrictVersion

sys.path.insert(0, '.github/workflow')
import config


def test_manifest():

    manifest_location = os.path.join(config.SRC, 'manifest.json')
    with open(manifest_location, 'r') as f:
        manifest = json.load(f)

    base_ref = os.environ['BASE_REF']
    prev_manifest  = '__prev_manifest.json'
    subprocess.run(f"git show origin/{base_ref}:{manifest_location} > {prev_manifest}", shell=True)
    with open(prev_manifest, 'r') as f:
        prev_manifest = json.load(f)

    assert StrictVersion(manifest['version']) > StrictVersion(prev_manifest['version'])
