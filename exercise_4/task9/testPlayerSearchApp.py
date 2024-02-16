from contextlib import redirect_stdout
import unittest
from unittest.mock import patch
from io import StringIO
from playerSearchApp import HockeyStats

class TestHockeyStats(unittest.TestCase):
    def setUp(self):
        self.stats = HockeyStats('part.json')

    @patch('builtins.input', return_value='Andy Greene')
    @patch('builtins.print')
    def test_search_for_player_WITH_MOCK(self, mock_print, mock_input):
        self.stats.search_for_player('Andy Greene')
        mock_print.assert_called()
        player = {'name': 'Andy Greene', 'team': 'NYI', 'goals': 2, 'assists': 12} 
        expected_output = (
            f"{player['name']:<20} "
            f"{player['team']:>3} "
            f"{player['goals']:>2} + "
            f"{player['assists']:>2} = "
            f"{player['goals'] + player['assists']:>2}"
        )

        # [0] the first element is a tuple of positional arguments passed into mock_print
        # [0] contains stings that were printed, [0][0] the first one is taken
        # [1] and the second element is a dictionary of keyword arguments
        actual_output = mock_print.call_args[0][0]
        self.assertEqual(expected_output, actual_output)

    def test_search_for_player_WITH_IO(self):
        player = {'name': 'Andy Greene', 'team': 'NYI', 'goals': 2, 'assists': 12} 
        expected_output = (
            f"{player['name']:<20} "
            f"{player['team']:>3} "
            f"{player['goals']:>2} + "
            f"{player['assists']:>2} = "
            f"{player['goals'] + player['assists']:>2}\n"  # Add newline at the end 
                # because the print function adds a newline at the end of its output
        )

        with patch('builtins.input', return_value='Andy Greene'), StringIO() as buf, redirect_stdout(buf):
            self.stats.search_for_player('Andy Greene')
            actual_output = buf.getvalue()

        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()