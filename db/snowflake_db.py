import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text
from typing import Any, Dict
import snowflake.connector          # For connecting to Snowflake

class SnowflakeDB:
    def __init__(self, config):
        self.conn = None
        self.config = config
        self.engine = None

    def connect(self):
        self.conn = snowflake.connector.connect(
            user=st.secrets["snowflake"]["user"],
            password=st.secrets["snowflake"]["password"],
            account=st.secrets["snowflake"]["account"],
            warehouse=st.secrets["snowflake"]["warehouse"],
            database=st.secrets["snowflake"]["database"],
            schema=st.secrets["snowflake"]["schema"]
        )
        return self.conn

    def get_engine(self):
        if not self.engine:
            user = st.secrets["snowflake"]["user"]
            password = st.secrets["snowflake"]["password"]
            account = st.secrets["snowflake"]["account"]
            warehouse = st.secrets["snowflake"]["warehouse"]
            database = st.secrets["snowflake"]["database"]
            schema = st.secrets["snowflake"]["schema"]
            conn_str = (
                f"snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}"
            )
            self.engine = create_engine(conn_str)
        return self.engine

    def create_table_if_not_exists(self):
        conn = self.connect()
        cursor = conn.cursor()
        columns_sql = []
        for col in self.config["columns"].values():
            columns_sql.append(f'{col["db_name"]} {col["type"]}')
        columns_sql_str = ",                    ".join(columns_sql)
        table_name = self.config["table_name"]
        try:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    {columns_sql_str}
                )
            """)
        finally:
            cursor.close()
            conn.close()

    def insert_response(self, df):
        try:
            self.create_table_if_not_exists()
            conn = self.connect()
            cursor = conn.cursor()
            table_name = self.config["table_name"]
            db_columns = [col["db_name"] for col in self.config["columns"].values()]
            placeholders = ", ".join(["%s"] * len(db_columns))
            columns_str = ", ".join(db_columns)
            for _, row in df.iterrows():
                cursor.execute(f"""
                    INSERT INTO {table_name} ({columns_str})
                    VALUES ({placeholders})
                """, tuple(row))
            cursor.close()
            conn.close()
            st.success("✅ Your response has been successfully saved in Snowflake. Thank you!")
            st.balloons()
        except Exception as e:
            st.error(f"Error saving to Snowflake: {e}")

    # def get_workshop_votes(self):
    #     try:
    #         conn = self.connect()
    #         table_name = self.config["table_name"]
    #         db_col = self.config["columns"]["Workshop Proposed Time"]["db_name"]
    #         df = pd.read_sql(f"SELECT {db_col} FROM {table_name}", conn)
    #         conn.close()
    #         vote_counts = df[db_col.upper()].value_counts().reset_index()
    #         vote_counts.columns = ["Interval", "Votes Number"]
    #         vote_counts.set_index("Interval", inplace=True)
    #         st.subheader("📊Votes distribution for the workshop")
    #         st.bar_chart(vote_counts, horizontal=True)
    #     except Exception as e:
    #         st.error(f"Error retrieving data from Snowflake: {e}")
        
    def get_workshop_votes(self):
        try:
            engine = self.get_engine()
            table_name = self.config["table_name"]
            db_col = self.config["columns"]["Workshop Proposed Time"]["db_name"]
            df = pd.read_sql(f"SELECT {db_col} FROM {table_name}", engine)
            vote_counts = df[db_col].value_counts().reset_index()
            vote_counts.columns = ["Interval", "Votes Number"]
            vote_counts.set_index("Interval", inplace=True)
            st.subheader("📊Votes distribution for the workshop")
            st.bar_chart(vote_counts, horizontal=True)
        except Exception as e:
            st.error(f"Error retrieving data from Snowflake: {e}")



# # --- OOP SnowflakeDB class ---

# # from typing import Any, Dict

# class SnowflakeDB:
#     """
#     Handles Snowflake database operations for the survey app.
#     """
#     def __init__(self, config: Dict[str, Any]) -> None:
#         """Initializes the SnowflakeDB with configuration."""
#         self.conn = None
#         self.config = config
#         self.engine = None

#     # def connect(self) -> Any:
#     #     """Establishes a connection to Snowflake using credentials from Streamlit secrets."""
#     #     self.conn = snowflake.connector.connect(
#     #         user=st.secrets["snowflake"]["user"],
#     #         password=st.secrets["snowflake"]["password"],
#     #         account=st.secrets["snowflake"]["account"],
#     #         warehouse=st.secrets["snowflake"]["warehouse"],
#     #         database=st.secrets["snowflake"]["database"],
#     #         schema=st.secrets["snowflake"]["schema"]
#     #     )
#     #     return self.conn

#     def get_engine(self) -> Any:
#         """Returns a SQLAlchemy engine for Snowflake connection."""
#         if not self.engine:
#             user = st.secrets["snowflake"]["user"]
#             password = st.secrets["snowflake"]["password"]
#             account = st.secrets["snowflake"]["account"]
#             warehouse = st.secrets["snowflake"]["warehouse"]
#             database = st.secrets["snowflake"]["database"]
#             schema = st.secrets["snowflake"]["schema"]
#             conn_str = (
#                 f"snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}"
#             )
#             self.engine = create_engine(conn_str)
#         return self.engine

#     def create_table_if_not_exists(self) -> None:
#         """
#         Creates the survey table in Snowflake if it does not exist using SQLAlchemy engine.
#         """
#         engine = self.get_engine()
#         columns_sql = []
#         for col in self.config["columns"].values():
#             columns_sql.append(f'"{col["db_name"]}" {col["type"]}')
#         columns_sql_str = ",                    ".join(columns_sql)
#         table_name = self.config["table_name"]
#         create_sql = f"""
#             CREATE TABLE IF NOT EXISTS "{table_name}" (
#                 {columns_sql_str}
#             )
#         """
#         with engine.connect() as conn:
#             conn.execute(text(create_sql))

#     def insert_response(self, df: pd.DataFrame) -> None:
#         """
#         Inserts a survey response into the Snowflake table using SQLAlchemy and pandas to_sql.
#         Args:
#             df (pd.DataFrame): DataFrame containing the response row.
#         """
#         try:
#             self.create_table_if_not_exists()
#             engine = self.get_engine()
#             table_name = self.config["table_name"]
#             # Ensure columns match DB columns
#             db_columns = [meta["db_name"] for col, meta in self.config["columns"].items()]
#             df = df.rename(columns={col: meta["db_name"] for col, meta in self.config["columns"].items()})
#             df = df[db_columns]
#             # Use quoted table name for Snowflake
#             df.to_sql(table_name, engine, if_exists='append', index=False, method='multi', schema=None)
#             st.success("✅ Your response has been successfully saved in Snowflake. Thank you!")
#             st.balloons()
#         except Exception as e:
#             st.error(f"Error saving to Snowflake: {e}")

#     def get_workshop_votes(self) -> None:
#         """Retrieves and displays the distribution of workshop time slot votes from Snowflake."""
#         try:
#             engine = self.get_engine()
#             table_name = self.config["table_name"]
#             db_col = self.config["columns"]["Workshop Proposed Time"]["db_name"]
#             # Use quoted table and column names for Snowflake
#             df = pd.read_sql(f'SELECT "{db_col}" FROM "{table_name}"', engine)
#             vote_counts = df[db_col].value_counts().reset_index()
#             vote_counts.columns = ["Interval", "Votes Number"]
#             vote_counts.set_index("Interval", inplace=True)
#             st.subheader("📊Votes distribution for the workshop")
#             st.bar_chart(vote_counts, horizontal=True)
#         except Exception as e:
#             st.error(f"Error retrieving data from Snowflake: {e}")
