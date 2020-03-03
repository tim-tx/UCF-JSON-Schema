import unittest
import json
import jsonschema
from glob import glob
from os import getcwd
from os.path import basename
from .meta_test import TestFileMeta, get_json_file_contents


__author__ = 'Timothy S. Jones <jonests@bu.edu>, Densmore Lab, BU'
__license__ = 'GPL3'


class TestInputSensorFileSyntax(unittest.TestCase, metaclass=TestFileMeta):

    def get_test_args():
        files = glob("files/v2/input/**/*.input.json", recursive=True)
        for f in files:
            yield (basename(f), f)

    def _test_syntax(self, f):
        schema = get_json_file_contents("schemas/v2/input_sensor_file.schema.json")
        resolver = jsonschema.RefResolver("file://" + getcwd() + "/schemas/v2/", "")
        validator = jsonschema.Draft7Validator(schema, resolver=resolver)
        with open(f) as isf_file:
            isf = json.load(isf_file)
        validator.validate(isf)


if __name__ == '__main__':
    unittest.main()
