from utils.scrapper import scrapper
from utils.processing import icc_processing, icf_processing
from utils.big_query import load_csv_to_bigquery, execute_sql_script

def main():
    # URLs for the ICC and ICF indices
    icc_url  ='https://www.fecomercio.com.br/pesquisas/indice/icc'
    icf_url = 'https://www.fecomercio.com.br/pesquisas/indice/icf'

    # Scrape the data and save it to an Excel file
    icc_xlsx = scrapper(icc_url, 'data/icc.xlsx')
    icf_xlsx = scrapper(icf_url, 'data/icf.xlsx')

    # Process the Excel files and save them as CSV files
    icc_csv = icc_processing(icc_xlsx, 'data/raw/icc_raw.csv')
    icf_csv = icf_processing(icf_xlsx, 'data/raw/icf_raw.csv')

    # Load the CSV files into BigQuery
    load_csv_to_bigquery(icc_csv, 'ps-eng-dados-ds3x.thalescosendey.icc_raw')
    load_csv_to_bigquery(icf_csv,'ps-eng-dados-ds3x.thalescosendey.icf_raw')

    # Execute the SQL scripts to refine the data
    execute_sql_script('sql/trusted.sql', 'ps-eng-dados-ds3x')
    execute_sql_script('sql/icf_icc_refined.sql', 'ps-eng-dados-ds3x')

if __name__ == '__main__':
    main()
