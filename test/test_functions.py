import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import unittest
from unittest.mock import patch, mock_open, MagicMock
from utils.processing import icc_processing, icf_processing
from utils.big_query import execute_sql_script


class TestFunctions(unittest.TestCase):
    @patch('builtins.open', mock_open(read_data="SELECT * FROM table;"))
    @patch('google.cloud.bigquery.Client')
    def test_execute_sql_script(self, MockBigQueryClient):
        # Arrange
        mock_client = MagicMock()
        MockBigQueryClient.return_value = mock_client
        mock_query_job = MagicMock()
        mock_client.query.return_value = mock_query_job
        mock_query_job.result.return_value = "result"

        sql_file_path = "sql/trusted.sql"
        project_id = "ps-eng-dados-ds3x"

        # Act
        result = execute_sql_script(sql_file_path, project_id)

        # Assert
        mock_client.query.assert_called_once_with("SELECT * FROM table;")
        mock_query_job.result.assert_called_once()
        self.assertEqual(result, "result")

    @patch('pandas.read_excel')
    @patch('builtins.open', mock_open())
    def test_icc_processing(self, mock_read_excel):
        # Arrange
        mock_df = MagicMock()
        mock_df.to_csv.return_value = None
        mock_read_excel.return_value = mock_df

        original_file_path = "data/icc.xlsx"
        processed_file_path = "data/raw/icc_raw.csv"

        # Act
        result = icc_processing(original_file_path, processed_file_path)

        # Assert
        mock_read_excel.assert_called_once_with(original_file_path, sheet_name=1, skiprows=1)
        mock_df.to_csv.assert_called_once_with(processed_file_path, index=False)
        self.assertEqual(result, processed_file_path)

    @patch('pandas.read_excel')
    @patch('builtins.open', mock_open())
    def test_icf_processing(self, mock_read_excel):
        # Arrange
        mock_df = MagicMock()
        mock_df.to_csv.return_value = None
        mock_read_excel.return_value = mock_df

        original_file_path = "data/icf.xlsx"
        processed_file_path = "data/raw/icf_raw.csv"

        # Act
        result = icf_processing(original_file_path, processed_file_path)

        # Assert
        mock_read_excel.assert_called_once_with(original_file_path, sheet_name=1)
        mock_df.to_csv.assert_called_once_with(processed_file_path, index=False)
        self.assertEqual(result, processed_file_path)

if __name__ == '__main__':
    unittest.main()
