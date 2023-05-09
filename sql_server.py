import pyodbc
import pandas as pd
import json

# Add your connection details
database = 'ICU_sepsis'
PORT = '1433'

# # Ubuntu server 20.04
# DRIVER ='{ODBC Driver 17 for SQL Server}'
# conn_string = f'DRIVER={DRIVER};SERVER={HOST},{PORT};DATABASE={database};UID={USER};PWD={PASSWORD}'

# Ubuntu server 22.04
DRIVER ='{ODBC Driver 18 for SQL Server}'
TRUST = 'TrustServerCertificate=yes'
conn_string = f'DRIVER={DRIVER};SERVER={HOST},{PORT};DATABASE={database};UID={USER};PWD={PASSWORD};{TRUST}'

conn = pyodbc.connect(conn_string)

tableName = "sepsis_philips"
cursor = conn.cursor()
try:
    tsql = """
    IF EXISTS (SELECT * FROM sepsis_philips WHERE Pno = ? AND Caseno = ? AND showtime = ?)
        UPDATE sepsis_philips
        SET Icuadmdate = ?,
            chart_philips_HR = ?,
            chart_philips_RR = ?,
            chart_philips_SBP = ?
        WHERE Pno = ? AND Caseno = ? AND showtime = ?
    ELSE
        INSERT INTO sepsis_philips (Pno, Caseno, showtime, Icuadmdate, chart_philips_HR, chart_philips_RR, chart_philips_SBP)
        VALUES (?, ?, ?, ?, ?, ?, ?);
    """
    with conn:
        for index, row in vitalsign_8.iterrows():
            try:
                ""
                # Convert dictionaries to JSON strings and ensure other columns are strings
                row_str = row.apply(lambda x: json.dumps(x) if isinstance(x, dict) else str(x))
                params_update = tuple(row_str)[:3] + tuple(row_str)[3:] + tuple(row_str)[:3]
                params_insert = tuple(row_str)
                params = params_update + params_insert

                params = ('Pno', 'Caseno', '2023-05-07 15:30:0000000', 'Icuadmdate', '{"2023-03-23": 39, "2023-03-25": 46}', '39, 58, 36', '-1, 52, 49, -1')
                temp = conn.execute(tsql, params)
            except pyodbc.DataError as e:
                print(f"Error at index {index}: {row}")
                print(e)

except ValueError as vx:
    print(vx)
except Exception as ex:
    print(ex)
else:
    print(f"Table {tableName} updated successfully.")
finally:
    pass