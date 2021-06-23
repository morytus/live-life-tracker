import os
import sys
import time
import datetime
import csv
import click

@click.command()
def cli():
    llt()
    click.echo('LLT')

def llt():
    pass

def read_tsv(filename):
    data = []
    idx = 0
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            data.append(row)
    return data

def write_record(filename, record):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(record)

def validate_file():
    pass

def start_task():
    pass

def stop_task():
    pass

def restart_task():
    pass

def calc_duration():
    pass

def what_time():
    now = datetime.datetime.now()
    return f"{now:%Y-%m-%d %H:%M:%S}"

def echo_message():
    pass

def add_category():
    pass

def add_project():
    pass

def add_tag():
    pass

def validate_file(filename):
    ## True
    # 存在しない
    # 最終レコードを除く全レコードのカラム数が7
    # 最終レコードのカラム数が5，または7
    ## False
    # 上記のいずれでもない
    pass

def count_cols():
    pass

def count_rows():
    pass

def create_header():
    pass

def is_debug(debug_flag):
    if debug_flag:
        return True

#CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
#
#if __name__ == "__main__":
#    data = read_tsv(CURRENT_DIR + '/../test/2021-06-15.tsv')
#    print(data)

