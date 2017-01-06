#!/usr/bin/python

from unittest import TestCase
from faker import Faker

import flask_testing
from hamcrest import *
from google.appengine.api.datastore_errors import BadValueError


class MasterDatastoreTest(TestCase):
    """
    This is the Master Class for all test suites.
    """

    def setUp(self):
        # your test setup.
        pass

    def tearDown(self):
        pass

# Utils
#
#
fake = Faker()


# Exports
#
#
__all__ = [
    'MasterDatastoreTest',
    # ndb imports here:
    'BadValueError',
    # Hamcrest imports here:
    #
    'calling',
    'not_',
    'assert_that',
    'is_',
    'equal_to',
    'instance_of',
    'raises',
    'has_key',
    # Utility imports here:
    #
    'fake',
    'flask_testing',

]
