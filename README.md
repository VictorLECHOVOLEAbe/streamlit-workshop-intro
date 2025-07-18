# streamlit-workshop-intro

# streamlit-intro-workshop
https://intro-workshop-bp.streamlit.app/


# Instalation of local setup
## Summary - Commands
python --version
python -m venv env
env\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt


# Folder Structure
```bash
local_oop_folders/
    app.py                      # Main entry point, runs the app
    config/
        table_config.py         # Contains TABLE_CONFIG and related config
    db/
        snowflake_db.py         # SnowflakeDB class and DB logic
    forms/
        survey_form.py          # SurveyForm class and form logic
    utils/
        validation.py           # validate_name, validate_email, and other helpers
    assets/
        about.md                # Markdown files and other static assets
        workshop_requirements.md
```