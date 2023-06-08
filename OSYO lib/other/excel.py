import sqlite3
import pandas as pd

data = pd.read_excel(
    'project/Catalogue.xlsx', 
    sheet_name='Sheet1',
    header=0)

db_conn = sqlite3.connect("project/data.db")

c = db_conn.cursor()

c.execute(
    """
    CREATE TABLE data(
        ID INTEGER,
        ComposerLAST TEXT,
        ComposerFIRST TEXT,
        ArrangerEditorLAST Text,
        ArrangerEditorFIRST TEXT,
        Title TEXT NOT NULL,
        MultipleEnvelopes INTEGER,
        Level REAL,
        Ensemble TEXT,
        ConductorScore TEXT,
        Parts TEXT,
        CompleteParts TEXT,
        CheckedOut TEXT,
        Publisher TEXT,
        Source TEXT,
        Xmas TEXT,
        PurchasePrice REAL,
        PurchaseDate TEXT,
        Comments TEXT,
        PRIMARY KEY(ID)
        );
    """
)

data.to_sql('data', db_conn, if_exists='append', index=False)