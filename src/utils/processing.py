import pandas as pd

def icc_processing(original_file_path, processed_file_path):
    """
    Processes the second sheet of an Excel file by removing blank rows, stripping column names,
    adding a 'load_timestamp' column, and saving the processed DataFrame as a CSV.

    Args:
        original_file_path (str): The file path of the original Excel file to process.
        processed_file_path (str): The file path where the processed CSV will be saved.

    Raises:
        FileNotFoundError: If the original Excel file is not found.
        Exception: For any other errors that occur during processing.

    Returns:
        str: The file path of the processed CSV file.
    """
    try:
        # Read the second sheet (index 1) into a pandas DataFrame and skip blank rows
        df = pd.read_excel(original_file_path, sheet_name=1, skiprows=1)

        # Strip leading and trailing spaces from column names
        df.columns = df.columns.str.strip()

        # Add a 'load_timestamp' column with the current datetime
        df['load_timestamp'] = pd.to_datetime('now', utc=True)

        # Save the processed DataFrame as a CSV file
        df.to_csv(processed_file_path, index=False)

        print('ICC processing completed successfully.')

        return processed_file_path

    except FileNotFoundError as e:
        print(f"Error: The file {original_file_path} was not found.")
        raise e
    except Exception as e:
        print(f"An error occurred during ICC processing: {e}")
        raise e


def icf_processing(original_file_path, processed_file_path):
    """
    Processes the second sheet of an Excel file by removing blank rows, stripping column names,
    adding a 'load_timestamp' column, and saving the processed DataFrame as a CSV.

    Args:
        original_file_path (str): The file path of the original Excel file to process.
        processed_file_path (str): The file path where the processed CSV will be saved.

    Raises:
        FileNotFoundError: If the original Excel file is not found.
        Exception: For any other errors that occur during processing.

    Returns:
        str: The file path of the processed CSV file.
    """
    try:
        # Read the second sheet (index 1) into a pandas DataFrame and skip blank rows
        df = pd.read_excel(original_file_path, sheet_name=1)

        # Strip leading and trailing spaces from column names
        df.columns = df.columns.str.strip()

        # Add a 'load_timestamp' column with the current datetime
        df['load_timestamp'] = pd.to_datetime('now', utc=True)

        # Save the processed DataFrame as a CSV file
        df.to_csv(processed_file_path, index=False)

        print('ICF processing completed successfully.')

        return processed_file_path

    except FileNotFoundError as e:
        print(f"Error: The file {original_file_path} was not found.")
        raise e
    except Exception as e:
        print(f"An error occurred during ICF processing: {e}")
        raise e
