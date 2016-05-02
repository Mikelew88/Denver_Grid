import pymysql
import sys
import csv
import pandas as pd

dbServer = 'localhost'
dbSchema = 'mrislistings'
dbUser = 'root'


if __name__ == '__main__':
    dbQuery = "SELECT * FROM z_listings;"

    conn = pymysql.connect(host=dbServer, user=dbUser, passwd='', db=dbSchema)

    df = pd.read_sql(dbQuery, con=conn)

    df.to_csv("../data/mrislistings.csv", index=False)
    print "exported mrislistings to csv"

    conn.close()
