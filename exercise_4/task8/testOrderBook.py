# File: testOrderBook.py
# Author: Kirill Nikolaev
# Description: test orderBook class

import unittest
from unittest.mock import patch
from io import StringIO
from orderBookApp import OrderBookApplication

class TestOrderBookApplication(unittest.TestCase):
    @patch('builtins.input', side_effect=['description', 'programmer 10'])
    @patch('builtins.print')
    def test_add_order(self, mock_print, mock_input):
        app = OrderBookApplication()
        app.add_order()
        mock_print.assert_called_with('added!')

    @patch('builtins.input', side_effect=['description', ''])
    @patch('builtins.print')
    def test_add_order_no_programmer(self, mock_print, mock_input):
        app = OrderBookApplication()
        app.add_order()
        mock_print.assert_called_with('erroneous input')

    @patch('builtins.input', side_effect=['description', 'programmer -10'])
    @patch('builtins.print')
    def test_add_order_negative_workload(self, mock_print, mock_input):
        app = OrderBookApplication()
        app.add_order()
        mock_print.assert_called_with('erroneous input')

if __name__ == '__main__':
    unittest.main()