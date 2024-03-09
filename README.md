
# Netflix Data ETL

This Python project implements an Extract, Transform, Load (ETL) system designed to cleanse raw Netflix data.
</br>Obs: The data used in this project was created for study purposes and is not official from Netflix.

<div align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge" height="35" alt="python logo"  />
  <img width="5" />
  <img src="https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white&style=for-the-badge" height="35" alt="pandas logo"  />
</div>

## Features

### Extract
The system retrieves raw Netflix data. </br>

### Transform
The ETL system cleanses and transforms the extracted data to prepare it for analysis. </br>
Dealing with inconsistencies: Address inconsistencies in data formats, units, or naming conventions </br>
Create new features from existing data to enhance analysis.

### Load
The transformed data is loaded into a xmlx.

## Installation
- Install Python. (This project was made with Python 3.11.6)
- Create a virtual environment to isolate project dependencies (recommended):

```
  python -m venv venv
  venv/bin/activate  # Windows: venv\Scripts\activate
```
- Install required dependencies using pip:

```
  pip install -r requirements.txt
```

## Running
```
  python src/scripts/main.py
```

## Contributing
Feel free to contribute, report issues, or suggest improvements.
