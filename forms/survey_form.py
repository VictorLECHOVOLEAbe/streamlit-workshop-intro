import streamlit as st
import pandas as pd
from typing import Any, Dict
from db.snowflake_db import SnowflakeDB


# --- OOP SurveyForm class ---

class SurveyForm:
    """
    Handles the survey form logic and user interaction in the Streamlit app.
    """
    def __init__(self, config: Dict[str, Any]) -> None:
        """Initializes the SurveyForm with configuration."""
        self.config = config
        self.data = {col: None for col in config["columns"]}
        self.db = SnowflakeDB(config)

    def validate_field(self, validator: Any, val: Any) -> Any:
        """
        Validates a field value using the provided validator function.
        Args:
            validator (callable): Validation function.
            val (Any): Value to validate.
        Returns:
            Any: The validated value.
        """
        if validator:
            if isinstance(val, list):
                val = ", ".join(val)
            if not validator(val):
                st.stop()
        return val

    def show(self) -> None:
        """
        Displays the survey form in the Streamlit app and handles user input.
        """
        st.markdown("---")
        st.header("#Let's get to know each other better")
        for col, meta in self.config["columns"].items():
            validator = meta.get("validate")
            label = meta.get("label_question", col)
            placeholder = meta.get("placeholder", None)
            help_text = meta.get("help", None)
            options = meta.get("options", None)
            if options and isinstance(options, list):
                if col == "Workshop Proposed Time":
                    val = st.radio(label, options, help=help_text)
                elif col == "Libraries" or col == "File Types":
                    val = st.multiselect(label, options, help=help_text)
                else:
                    val = st.selectbox(label, options, help=help_text)
            elif meta["type"] == "INT":
                val = st.number_input(label, min_value=0, step=1, help=help_text)
            else:
                val = st.text_input(label, placeholder=placeholder, help=help_text)
            self.data[col] = self.validate_field(validator, val)

        if st.button("Submit response"):
            self.submit()

    def submit(self) -> None:
        """
        Prepares and submits the survey response to the database.
        """
        row = {}
        for col, meta in self.config["columns"].items():
            val = self.data[col]
            if isinstance(val, list):
                val = ", ".join(val)
            row[col] = val
        response = pd.DataFrame([row])
        self.db.insert_response(response)
        self.db.get_workshop_votes()