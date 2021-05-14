import sqlite3
import datetime


def insert_data(t, h):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    date = str(datetime.datetime.today())[8:10]
    time = str(datetime.datetime.today())[11:19]
    month = str(datetime.datetime.today())[5:7]
    year = str(datetime.datetime.today())[0:4]
    cursor.execute(

        f"""
        insert into wed_data values('{t}', '{h}','{time}','{date}', '{month}', '{year}');

        """
    )
    conn.commit()
    cursor.close()
    conn.close()


def create_data_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        create table wed_data (temp varchar2, humidity varchar2, time varchar2,dte varchar2, month varchar2, year varchar2);       
        """

    )
    conn.commit()
    cursor.close()
    conn.close()


def get_data_by_month(m, y):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""
        select * from wed_data where month='{m}' and year='{y}'
        
        """

    )

    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data


def clear_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        delete from wed_data;
        """

    )
    conn.commit()
    cursor.close()
    conn.close()

