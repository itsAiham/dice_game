#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import sys
import io

from histogram import Histogram
from player import Player


class TestHistogram(unittest.TestCase):
    """Test Histogram Class."""

    def test_print_histogram(self):
        """Test print_histogram."""
        histogram = Histogram()
        player1 = Player("name1", False)
        player2 = Player("name2", False)

        res = player1.get_name()
        catch_output = io.StringIO()
        sys.stdout = catch_output

        histogram.print_histogram(player1, player2)

        sys.stdout = sys.__stdout__
        output = catch_output.getvalue()

        self.assertIn(str(res), output)

        self.assertIn(player1.get_name(), output)
        self.assertIn(player2.get_name(), output)

    def test_create_asterisk(self):
        exp = 2
        ast = ' * '
        res = ' *  * '
        self.assertEqual(exp * ast, res)

