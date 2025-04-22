# Gather some data from redshift

from relayridespy3 import RedshiftConnection


def fetch_data_from_redshift(str_sql_file, start_date=None, end_date=None):

    """
    Takes in the file that contains the query that will be used to fetch the utilization data.

    Args:
        str_sql_file (string): the name of the file with the sql query from which we are fetching the data
        start_date (string): the start date from which we want to query the data
        end_date (string): the end date from where we want to stop querying the data
    Returns:
        df_training (pandas data frame): contains the data that will be used in the process of creating the training set
    """

    with open(str_sql_file, 'r') as f:
        if start_date and end_date:
            str_qry = f.read().format(start_date, end_date)
        else:
            str_qry = f.read()
        con = RedshiftConnection(ssh=True)
        df_raw = con.fetch_data(str_qry)

        return df_raw
