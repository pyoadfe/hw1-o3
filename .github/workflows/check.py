#!/usr/bin/env python3

import json
import sys
from numpy.testing import assert_almost_equal

with open(sys.argv[1]) as json_file:
    data = json.load(json_file)

    assert_almost_equal(data['coordinates'][0], 69.66, 2)
    assert_almost_equal(data['coordinates'][1], 18.96, 2)
    assert_almost_equal(data['jan']['min'], 232.0, 0)
    assert_almost_equal(data['jan']['max'], 273.0, 0)
    assert_almost_equal(data['jan']['mean'], 252.75, 0)
    assert_almost_equal(data['jul']['min'], 258.0, 0)
    assert_almost_equal(data['jul']['max'], 287.0, 0)
    assert_almost_equal(data['jul']['mean'], 273.7, 0)
    assert_almost_equal(data['all']['min'], 226.0, 0)
    assert_almost_equal(data['all']['max'], 295.0, 0)
    assert_almost_equal(data['all']['mean'], 264.9, 0)
