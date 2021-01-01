# DepremNeredeOldu: The earthquakes visualization

For this project, I used **Python** on the backend (**Flask RESTful API**). The goal is to visualize the earthquakes in Turkey on map with [MapBox](https://www.mapbox.com). The project is deployed on [depremneredeoldu.com](https://depremneredeoldu.com)

# Requirements

##### Create a new virtual environment
    python3 -m venv venv

###### And then,

    pip install -r requirements.txt

# Initialize the database

    python initialize_db.py

# To run

    python app.py

# Automate your data extraction

If you want to update the earthquake data automatically, you can configure a **Cron Job** to automate this processus by executing **initialize_db.py** script every minute.


## Data

The data comes from **Kandilli Observatory and Earthquake Research Institute** and cannot be used for commercial purposes in any way without the written permission and approval of **Boğaziçi University**.


## Contact

    Alican Yüksel - alicanyuksel@outlook.com