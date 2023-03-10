import encodings

from pyreportjasper import PyReportJasper
from platform import python_version
import logging
import psycopg2


def advanced_example_using_database():
    input_file = 'jasper_test_file.jrxml'
    output_file = 'hello_world'
    conn = {
        'driver': 'postgres',
        'username': 'my_proj',
        'password': 'my_proj',
        'host': 'localhost',
        'database': 'my_proj_dev',
        'port': '5455',
        'jdbc_dir': 'C:\\Program Files\\Java\\jdk-19',
        'jdbc_driver': 'org.postgresql.Driver',
    }
    pyreportjasper = PyReportJasper()
    pyreportjasper.config(
        input_file=input_file,
        output_file=output_file,
        db_connection=conn,
        output_formats=["pdf"],
        parameters={'python_version': python_version()},
        locale='ru_RU',
    )
    pyreportjasper.process_report()


advanced_example_using_database()