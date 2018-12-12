#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests helper methods."""

from __future__ import print_function
from __future__ import with_statement
import unittest
import nose

from google.modules.utils import _get_search_url


class UtilsTestCase(unittest.TestCase):

    """Tests for helper methods."""
    def test_get_search_url(self):
        url = _get_search_url("apple", 0, 10, "en", "jp")
        exp_url = "http://www.google.co.jp/search?q=apple&start=0&num=10&hl=en"
        self.assertEqual(url, exp_url)

    """Tests site functionality for helper methods."""
    def test_extend_get_search_url(self):
        url = _get_search_url("apple", 0, 10, "en", ncr=True, site="apple.ch")
        exp_url = "http://www.google.ch/search?q=apple+site%3Aapple.ch&start=0&num=10&hl=en&gl=us&pws=0&gws_rd=cr"
        self.assertEqual(url, exp_url)


if __name__ == '__main__':
    nose.run(defaultTest=__name__)
