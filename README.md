# Car Price Prediction

A car resale price prediction project with a FastAPI backend and a Streamlit interface. The API uses a pre-trained model and feature-column list stored in the project directory.

## Requirements

- Python 3.11 or later
- Packages listed in [`requirements.txt`](./requirements.txt)

The virtual environment is kept in the parent project directory at `..\.venv`.

## Setup

From the `CarPredictionAPI` directory, activate the environment and install dependencies:

```powershell
..\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the API

From the `CarPredictionAPI` directory:

```powershell
python -m uvicorn main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive API documentation is at `http://127.0.0.1:8000/docs`.

### Endpoints

- `GET /` — basic service check.
- `POST /predict` — predicts a car's selling price.

Example request:

```json
{
  "Car_Name": "ritz",
  "Year": 2015,
  "Present_Price": 5.47,
  "Kms_Driven": 27000,
  "Fuel_Type": "Petrol",
  "Seller_Type": "Dealer",
  "Transmission": "Manual",
  "Owner": 0
}
```

The prediction response has the shape:

```json
{
  "prediction_price": 3.25
}
```

Accepted values for `Fuel_Type` are `Petrol`, `Diesel`, and `CNG`; for `Seller_Type`, `Dealer` and `Individual`; and for `Transmission`, `Manual` and `Automatic`. `Owner` must be an integer from 0 to 3.

## Run the Streamlit interface

In a separate terminal, from the `CarPredictionAPI` directory:

```powershell
python -m streamlit run streamlit.py
```

The interface currently targets the hosted API URL configured in `streamlit.py`. To use a local API instead, change `API_URL` there to `http://127.0.0.1:8000/predict` while the API is running.

## Project files

- `main.py` — FastAPI application and routes.
- `schema.py` — request and response models.
- `model.py` — model loading, input preprocessing, and prediction.
- `streamlit.py` — Streamlit user interface.
- `cardekho_data.csv` — car data.
- `random_forest_model.pkl` and `feature_columns.pkl` — trained model and expected feature columns.
