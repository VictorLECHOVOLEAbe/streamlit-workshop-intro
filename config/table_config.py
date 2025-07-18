from typing import Any, Dict
from utils.validation import validate_name, validate_email

TABLE_CONFIG: Dict[str, Any] = {
    "table_name": "survey_responses_app_test1500",
    "columns": {
        "Full Name": {
            "db_name": "name",
            "type": "STRING",
            "validate": lambda v: validate_name(v),
            "placeholder": "Enter your name here",
            "help": "This field is required!",
            "label_question": "Full Name:"
        },
        # "Nick Name": {
        #     "db_name": "nick_name",
        #     "type": "STRING",
        #     "validate": lambda v: validate_name(v),
        #     "placeholder": "Enter your nick name here",
        #     "help": "This field is required!",
        #     "label_question": "Nick Name:"
        # },
        # "Email": {
        #     "db_name": "email",
        #     "type": "STRING",
        #     "validate": lambda v: validate_email(v),
        #     "placeholder": None,
        #     "help": "This field is required!",
        #     "label_question": "Your Email:"
        # },
        # "Developer Hours": {
        #     "db_name": "developer_hours",
        #     "type": "INT",
        #     "validate": lambda v: v >= 0,
        #     "placeholder": None,
        #     "help": None,
        #     "label_question": "How many hours have you spent developing in any programming language?"
        # },
        # "Python Hours": {
        #     "db_name": "python_hours",
        #     "type": "INT",
        #     "validate": lambda v: v >= 0,
        #     "placeholder": None,
        #     "help": None,
        #     "label_question": "How many hours have you spent coding in Python?"
        # },
        # "Libraries": {
        #     "db_name": "libraries",
        #     "type": "STRING",
        #     "validate": None,
        #     "options": ["NumPy", "Pandas", "Matplotlib", "Seaborn", "Flask", "Django", "Streamlit", "Other library", "None"],
        #     "help": None,
        #     "label_question": "Select all python libraries you have used."
        # },
        # "File Types": {
        #     "db_name": "file_types",
        #     "type": "STRING",
        #     "validate": None,
        #     "options": [".csv", ".json", ".xlsx", ".sql", ".txt", ".xml", "Other type"],
        #     "help": None,
        #     "label_question": "Select all file types you have worked with."
        # },
        # "SQL Hours": {
        #     "db_name": "sql_hours",
        #     "type": "INT",
        #     "validate": lambda v: v >= 0,
        #     "placeholder": None,
        #     "help": None,
        #     "label_question": "How many hours have you spent writing SQL?"
        # },
        "Workshop Proposed Time": {
            "db_name": "workshop_proposed_time",
            "type": "STRING",
            "validate": None,
            "options": ["Friday 09:00-12:00", "Friday 13:00-16:00", "Not available this Friday anymore"],
            "help": None,
            "label_question": "Choose your preferred time slot for the Workshop."
        }
    }
}