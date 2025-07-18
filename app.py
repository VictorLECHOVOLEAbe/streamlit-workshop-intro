
# Run the app with the command:
# streamlit run app.py

import streamlit as st              # For building the web app
import pandas as pd                 # For data manipulation
    
import snowflake.connector          # For connecting to Snowflake
from sqlalchemy import create_engine  # For SQLAlchemy connection   

from typing import Any, Dict         # For type hinting

from config.table_config import TABLE_CONFIG
from db.snowflake_db import SnowflakeDB  # Importing the SnowflakeDB class
from forms.survey_form import SurveyForm  # Importing the SurveyForm class  
from utils.validation import validate_name, validate_email  # Importing validation functions


# --- OOP Application class ---
class App:
    """
    Main application class for the Streamlit survey app.
    """
    def __init__(self) -> None:
        """Initializes the App and configures the page."""
        self.configure_page()

    def configure_page(self) -> None:
        """Sets the Streamlit page configuration."""
        st.set_page_config(
            page_title="Survey: Your Experience with Python and SQL",
            page_icon="🎓"
            # layout="wide"   
        )

    def show_markdown(self, file_path: str) -> None:
        """Displays markdown content from a file in the Streamlit app.
        Args:
            file_path (str): Path to the markdown file.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                st.markdown(content, unsafe_allow_html=True)
        except FileNotFoundError:
            st.error(f"File {file_path} was not found.")
        except Exception as e:
            st.error(f"Error reading file: {e}")

    def run(self) -> None:
        """Runs the main app logic."""
        self.show_markdown("assets/about.md")
        self.show_markdown("assets/workshop_requirements.md")
        form = SurveyForm(TABLE_CONFIG)
        form.show()

def main() -> None:
    """
    Main entry point for the Streamlit app.
    """
    app = App()
    app.run()

if __name__ == "__main__":
    main()