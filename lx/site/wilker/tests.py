# -*- coding: utf-8 -*-
import unittest
import doctest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase.layer import onsetup

import lx.site.wilker

@onsetup
def setup_product():
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml',
                     lx.site.wilker)
    fiveconfigure.debug_mode = False
    ztc.installPackage('lx.site.wilker')

setup_product()

ptc.setupPloneSite(extension_profiles=['lx.site.wilker:default'])

class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):

        @classmethod
        def tearDown(cls):
            pass



def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='lx.site.wilker',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='lx.site.wilker.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'README.txt', package='lx.site.wilker.docs',
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | 
                         doctest.NORMALIZE_WHITESPACE | 
                         doctest.ELLIPSIS,
            test_class=TestCase),

        ztc.FunctionalDocFileSuite(
            'browser.txt', 
            package='lx.site.wilker.docs',
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | 
                        doctest.NORMALIZE_WHITESPACE | 
                        doctest.ELLIPSIS,
            test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
