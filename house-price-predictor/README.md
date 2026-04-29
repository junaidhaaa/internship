# 🏠 HomeValue AI — House Price Prediction App

A fully interactive machine-learning web application that trains a **Random Forest Regressor** on synthetic housing data and lets you predict house prices through a polished dark-themed UI. Every line of code is heavily commented for learning.

---

## 📸 What You'll See

| Tab | Contents |
|---|---|
| **Predict a Price** | Sidebar with sliders & dropdowns → live price estimate with confidence range |
| **Model Performance** | Actual vs Predicted scatter, Feature Importance bar, Residual plot, Error histogram |
| **Data Explorer** | Price distribution, neighborhood box plots, living-area scatter, raw data table |

---

## ⚙️ Prerequisites

### Python Version
> **Use Python 3.10 or 3.11.**  
> These versions are fully compatible with all required libraries.  
> Python 3.12+ may have minor compatibility issues with older NumPy builds.

Check your version:
```bash
python --version
# or
python3 --version
```

Download Python: https://www.python.org/downloads/

---

## 🚀 Quickstart

### Step 1 — Clone or download this project

Place these files in a single folder, e.g. `house-price-app/`:

```
house-price-app/
├── app.py                    ← Main Streamlit application
├── housing_synthetic.csv     ← Dataset (must be in same folder as app.py)
├── requirements.txt          ← Python dependencies
└── README.md                 ← This file
```

---

### Step 2 — Create a virtual environment (recommended)

A virtual environment isolates this project's dependencies from your system Python, preventing version conflicts.

**macOS / Linux:**
```bash
cd house-price-app
python3 -m venv venv
source venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
cd house-price-app
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
cd house-price-app
python -m venv venv
venv\Scripts\Activate.ps1
```

Your prompt will change to show `(venv)` when the environment is active.

---

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

This installs:

| Package | Version | Purpose |
|---|---|---|
| `streamlit` | ≥ 1.32.0 | Web UI framework |
| `pandas` | ≥ 2.0.0 | Data loading & manipulation |
| `numpy` | ≥ 1.26.0 | Numerical operations |
| `scikit-learn` | ≥ 1.4.0 | Random Forest model, preprocessing, metrics |
| `plotly` | ≥ 5.19.0 | Interactive charts |

---

### Step 4 — Run the app

```bash
streamlit run app.py
```

Streamlit will print something like:
```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Open `http://localhost:8501` in your browser. The app will load, train the model (~5–10 seconds the first time), and display the dashboard.

---

## 🗂️ Project Structure & Code Walkthrough

```
app.py  (single-file application)
│
├── Section 1  — Imports
├── Section 2  — Page config & CSS theme
├── Section 3  — load_data()         ← reads CSV into DataFrame
├── Section 4  — preprocess()        ← encodes categories, scales features
├── Section 5  — train_model()       ← splits data, fits Random Forest, evaluates
├── Section 6  — predict_price()     ← applies saved transforms to user input
├── Section 7  — chart_*() helpers   ← Plotly figures for each chart
└── Section 8  — main()              ← Streamlit layout & UI logic
```

### Key ML Concepts in the Code

| Concept | Where | Why |
|---|---|---|
| `train_test_split` | `train_model()` | Evaluate on data the model never saw |
| `LabelEncoder` | `preprocess()` | Convert text categories → integers |
| `StandardScaler` | `preprocess()` | Normalise feature magnitudes |
| `RandomForestRegressor` | `train_model()` | Ensemble of 200 decision trees |
| `feature_importances_` | `chart_feature_importance()` | See which features matter most |
| MAE / RMSE / R² | `train_model()` | Measure prediction accuracy |
| `@st.cache_data` | Multiple functions | Prevent re-running expensive code on every UI change |

---

## 📊 Dataset (`housing_synthetic.csv`)

| Column | Type | Description |
|---|---|---|
| `neighborhood` | categorical | Area type (Downtown, Suburbs, Rural, etc.) |
| `sqft_living` | integer | Interior living area in square feet |
| `sqft_lot` | integer | Total lot size in square feet |
| `bedrooms` | integer | Number of bedrooms |
| `bathrooms` | integer | Number of bathrooms |
| `floors` | float | Number of floors |
| `has_basement` | 0/1 | Whether the house has a basement |
| `basement_sqft` | integer | Basement area (0 if none) |
| `garage_cars` | integer | Garage capacity in cars |
| `has_pool` | 0/1 | Pool present |
| `year_built` | integer | Construction year |
| `house_age_years` | integer | Age of property |
| `renovated` | 0/1 | Recently renovated |
| `condition_score` | 1–10 | Overall condition |
| `quality_grade` | 1–5 | Build quality |
| `school_rating` | float | Local school quality (1–5) |
| `crime_rate_per_1000` | float | Crimes per 1,000 residents |
| `dist_city_center_km` | float | Distance to city centre |
| `dist_school_km` | float | Distance to nearest school |
| `dist_hospital_km` | float | Distance to nearest hospital |
| `property_tax_rate_pct` | float | Annual property tax rate |
| `hoa_monthly_usd` | integer | Monthly HOA fee |
| `market_trend` | categorical | Rising / Stable / Declining |
| **`price_usd`** | integer | **Target — house price** |

---

## 🛠️ Troubleshooting

### Port already in use
```bash
streamlit run app.py --server.port 8502
```

### Dataset not found
Make sure `housing_synthetic.csv` is in the **same directory** as `app.py`.

### `ModuleNotFoundError`
Ensure your virtual environment is activated (you should see `(venv)` in your prompt), then re-run `pip install -r requirements.txt`.

### Fonts not loading
The UI uses Google Fonts (Playfair Display & DM Sans). These load from the internet. If you're offline, Streamlit will fall back to system fonts — the app still works, but the typography will differ.

### Slow first load
The first run compiles and trains 200 decision trees. After that, Streamlit's `@st.cache_data` caches the result in memory, so subsequent interactions are instant.

---

## 🎓 Learning Extensions

Once you're comfortable with the code, try these modifications:

1. **Swap the model** — Replace `RandomForestRegressor` with `GradientBoostingRegressor` or `XGBRegressor` (requires `pip install xgboost`). Compare R² scores.
2. **Cross-validation** — Use `cross_val_score` from `sklearn.model_selection` for a more robust accuracy estimate.
3. **Hyperparameter tuning** — Try `GridSearchCV` or `RandomizedSearchCV` to find the best `n_estimators` and `max_depth`.
4. **SHAP values** — Install `shap` and add per-prediction explanations to the sidebar.
5. **Save the model** — Use `joblib.dump(model, "model.pkl")` to persist the trained model so you don't need to retrain on startup.

---

## 📦 Tested Environment

```
OS          : macOS 14 / Ubuntu 22.04 / Windows 11
Python      : 3.10.14 / 3.11.9
streamlit   : 1.32.2
pandas      : 2.2.1
numpy       : 1.26.4
scikit-learn: 1.4.1
plotly      : 5.19.0
```
