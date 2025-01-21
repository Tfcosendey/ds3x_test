from google.cloud import bigquery
import os

def load_csv_to_bigquery(csv_file_path, destination_table):
    """
    Loads a CSV file into a BigQuery table.

    Args:
        csv_file_path (str): The file path of the CSV file to be loaded.
        credentials_path (str): The file path of the Google Cloud credentials JSON.
        destination_table (str): The BigQuery destination table in the format `project.dataset.table`.

    Raises:
        FileNotFoundError: If the CSV file or the credentials file is not found.
        Exception: For any other errors that occur during the loading process.

    Returns:
        None: This function doesn't return any value. It raises exceptions in case of failure.
    """
    try:
        # Initialize a BigQuery client
        client = bigquery.Client()

        # Configure the load job
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            autodetect=True,
        )

        # Load the CSV file into BigQuery
        with open(csv_file_path, "rb") as source_file:
            job = client.load_table_from_file(
                source_file, destination_table, job_config=job_config
            )

        # Wait for the job to complete
        job.result()

        print(f"Loaded {job.output_rows} rows into {destination_table}.")

    except FileNotFoundError as e:
        print(f"Error: The file {csv_file_path} was not found.")
        raise e
    except Exception as e:
        print(f"An error occurred while loading CSV to BigQuery: {e}")
        raise e


def execute_sql_script(sql_file_path, project_id=None):
    """
    Executes an SQL script on Google BigQuery.

    Args:
        credentials_path (str): The file path of the Google Cloud credentials JSON.
        sql_file_path (str): The file path of the SQL script to be executed.
        project_id (str, optional): The Google Cloud project ID. If None, the default project will be used.

    Raises:
        FileNotFoundError: If the SQL file or the credentials file is not found.
        Exception: For any other errors that occur during the execution of the script.

    Returns:
        google.cloud.bigquery.table.RowIterator: The result of the executed query.
    """
    try:
        # Read the content of the SQL script from the file
        with open(sql_file_path, 'r') as sql_file:
            sql_script = sql_file.read()

        # Initialize a BigQuery client
        client = bigquery.Client(project=project_id)

        # Run the SQL query
        query_job = client.query(sql_script)

        # Wait for the job to complete
        result = query_job.result()

        print(f"{sql_file_path.split('/')[-1]} script executed successfully.")

        return result

    except FileNotFoundError as e:
        print(f"Error: The SQL file {sql_file_path} was not found.")
        raise e
    except Exception as e:
        print(f"An error occurred while executing the SQL script: {e}")
        raise e
