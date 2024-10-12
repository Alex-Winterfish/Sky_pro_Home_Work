from unittest.mock import patch
from unittest.mock import Mock
from src.main import main
import unittest

@patch('src.main.user_search_word')
@patch('src.main.user_sorting')
@patch('src.main.user_sort_option')
@patch('src.main.user_state_select')
@patch('src.main.user_file_select')
def test_main(mock_file_select, mock_state_select, mock_sort_option, mock_sorting, mock_user_search_word):
    mock_file_select.return_value = '2'
    mock_state_select.return_value = 'CANCALED'
    mock_sort_option.return_value = 'ДА'
    mock_sorting.return_value = 'ПО ВОЗРАСТАНИЮ'
    mock_user_search_word.return_value = 'НА КАРТУ'
    assert main() == []
"""
def test_main():
    mock_file_select = Mock(return_value = '2')
    mock_stat_select = Mock(return_value = 'CANCALED')
    mock_sort_option = Mock(return_value = 'ДА')
    mock_user_search_word = Mock(return_value='НА КАРТУ')
    user_file_select = mock_file_select
    user_stat_select = mock_stat_select
    user_sort_option = mock_sort_option
    user_search_word = mock_user_search_word

    assert main() == []

class Main(unittest.TestCase):

    @patch('input.inputs', side_effect = ['2','CANCELED', 'ДА', 'НА КАРТУ'])
    def test_main(self, mock_input):
        result = main()
        self.assertEqual(result, '2')

        result = main()
        self.assertEqual(result, 'CANCELED')

        result = main()
        self.assertEqual(result, 'ДА')

        result = main()
        self.assertEqual(result, 'НА КАРТУ')"""