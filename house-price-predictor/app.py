# =============================================================================
# HOUSE PRICE PREDICTION - STREAMLIT APPLICATION
# =============================================================================
#
# PURPOSE:
#   This application trains a Random Forest regression model on synthetic
#   housing data and provides an interactive web UI for predicting house
#   prices. It is designed to be a learning reference, so every major step
#   is explained in detail through comments.
#
# KEY CONCEPTS COVERED:
#   1. Data Loading & Exploration
#   2. Feature Engineering & Preprocessing (Label Encoding, Scaling)
#   3. Model Training (Random Forest Regressor)
#   4. Model Evaluation (MAE, RMSE, R²)
#   5. Visualization (Feature Importance, Actual vs Predicted)
#   6. Interactive UI (Streamlit)
#
# =============================================================================

# ── Standard library ──────────────────────────────────────────────────────────
import os               # Used for file path operations
import warnings         # Suppress noisy runtime warnings
warnings.filterwarnings("ignore")  # Keep the console clean during training

# ── Data manipulation ─────────────────────────────────────────────────────────
import pandas as pd     # DataFrame operations – loading, cleaning, transforming
import numpy as np      # Numerical computing – array math, statistics

# ── Machine Learning – Scikit-learn ───────────────────────────────────────────
from sklearn.ensemble import RandomForestRegressor   # Our prediction model
from sklearn.model_selection import train_test_split # Split data into train/test sets
from sklearn.preprocessing import (
    LabelEncoder,        # Converts text categories → integers (e.g. "Suburb" → 2)
    StandardScaler       # Standardizes numerical features to mean=0, std=1
)
from sklearn.metrics import (
    mean_absolute_error,      # Average absolute prediction error
    mean_squared_error,       # Penalises large errors more heavily than MAE
    r2_score                  # Proportion of variance explained (1.0 = perfect)
)

# ── Visualisation ─────────────────────────────────────────────────────────────
import plotly.express as px           # High-level chart API (scatter, bar, etc.)
import plotly.graph_objects as go     # Low-level chart API for custom figures

# ── Web UI ────────────────────────────────────────────────────────────────────
import streamlit as st   # Turns Python scripts into shareable web apps


# =============================================================================
# 1.  PAGE CONFIGURATION
# =============================================================================
# st.set_page_config MUST be the very first Streamlit call in the script.
# It sets the browser tab title, the layout width and the sidebar default state.

st.set_page_config(
    page_title="HomeValue AI",          # Browser tab title
    page_icon="🏠",                     # Favicon shown in the tab
    layout="wide",                      # Use the full browser width
    initial_sidebar_state="expanded"    # Open the sidebar on load
)


# =============================================================================
# 2.  CUSTOM CSS – VISUAL THEME
# =============================================================================
# Streamlit lets you inject raw CSS with st.markdown(unsafe_allow_html=True).
# We define CSS variables (--primary, --bg, etc.) at the :root level so that
# every rule below can reference them, making theme changes trivial.

st.markdown("""
<style>
/* ── Google Fonts ─────────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── CSS Design Tokens (variables) ───────────────────────────────────────── */
:root {
    --bg-deep:    #0a0c10;   /* darkest background */
    --bg-card:    #12151c;   /* card/panel surface  */
    --bg-raised:  #1a1f2e;   /* slightly elevated surface */
    --border:     #2a3045;   /* subtle divider lines */
    --primary:    #e8a838;   /* amber gold accent    */
    --primary-dim:#b07820;   /* muted accent          */
    --text-hi:    #f0ece4;   /* high-contrast text    */
    --text-mid:   #9aa3b8;   /* secondary text        */
    --text-lo:    #4a5268;   /* muted / placeholder   */
    --green:      #3ecf8e;   /* positive / success    */
    --red:        #e8534a;   /* negative / error      */
    --font-head:  'Playfair Display', Georgia, serif;
    --font-body:  'DM Sans', system-ui, sans-serif;
}

/* ── Global Reset ────────────────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: var(--font-body);
    background-color: var(--bg-deep);
    color: var(--text-hi);
}

/* ── App wrapper ─────────────────────────────────────────────────────────── */
.stApp { background: var(--bg-deep); }

/* ── Main content padding ────────────────────────────────────────────────── */
.main .block-container { padding: 2rem 3rem 4rem 3rem; max-width: 1400px; }

/* ── Hero header ─────────────────────────────────────────────────────────── */
.hero-header {
    background: linear-gradient(135deg, #12151c 0%, #1a1f2e 50%, #0d1020 100%);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 3rem 3.5rem;
    margin-bottom: 2.5rem;
    position: relative;
    overflow: hidden;
}
.hero-header::before {          /* decorative ambient glow */
    content: "";
    position: absolute;
    top: -60px; right: -60px;
    width: 260px; height: 260px;
    background: radial-gradient(circle, rgba(232,168,56,0.12) 0%, transparent 70%);
    pointer-events: none;
}
.hero-title {
    font-family: var(--font-head);
    font-size: 3rem;
    font-weight: 900;
    color: var(--text-hi);
    line-height: 1.1;
    margin: 0 0 .5rem 0;
}
.hero-title span { color: var(--primary); }
.hero-sub {
    font-size: 1.05rem;
    color: var(--text-mid);
    font-weight: 300;
    letter-spacing: .02em;
}

/* ── Section heading ─────────────────────────────────────────────────────── */
.section-title {
    font-family: var(--font-head);
    font-size: 1.45rem;
    font-weight: 700;
    color: var(--text-hi);
    border-left: 4px solid var(--primary);
    padding-left: .85rem;
    margin: 2rem 0 1.2rem 0;
}

/* ── Metric cards ────────────────────────────────────────────────────────── */
.metric-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.4rem 1.6rem;
    text-align: center;
    transition: border-color .2s;
}
.metric-card:hover { border-color: var(--primary-dim); }
.metric-label {
    font-size: .75rem;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: var(--text-mid);
    margin-bottom: .4rem;
}
.metric-value {
    font-family: var(--font-head);
    font-size: 2rem;
    font-weight: 700;
    color: var(--primary);
}
.metric-note { font-size: .78rem; color: var(--text-lo); margin-top: .25rem; }

/* ── Prediction result box ────────────────────────────────────────────────── */
.prediction-box {
    background: linear-gradient(135deg, #1a1f2e, #12151c);
    border: 2px solid var(--primary);
    border-radius: 16px;
    padding: 2.5rem;
    text-align: center;
    box-shadow: 0 0 40px rgba(232,168,56,0.12);
    animation: fadeSlideUp .5s ease both;
}
.prediction-label {
    font-size: .85rem;
    letter-spacing: .15em;
    text-transform: uppercase;
    color: var(--text-mid);
    margin-bottom: .6rem;
}
.prediction-price {
    font-family: var(--font-head);
    font-size: 3.2rem;
    font-weight: 900;
    color: var(--primary);
    line-height: 1;
}
.prediction-range {
    font-size: .9rem;
    color: var(--text-mid);
    margin-top: .6rem;
}

/* ── Info / tip box ──────────────────────────────────────────────────────── */
.info-box {
    background: rgba(232,168,56,0.07);
    border-left: 3px solid var(--primary);
    border-radius: 0 8px 8px 0;
    padding: .9rem 1.2rem;
    font-size: .88rem;
    color: var(--text-mid);
    margin: 1rem 0;
}

/* ── Sidebar ─────────────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: var(--bg-card) !important;
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] .stSlider > div > div > div { background: var(--primary) !important; }

/* ── Streamlit widget overrides ──────────────────────────────────────────── */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: var(--bg-raised) !important;
    border: 1px solid var(--border) !important;
    color: var(--text-hi) !important;
    border-radius: 8px !important;
}
.stButton > button {
    background: var(--primary) !important;
    color: #0a0c10 !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    border: none !important;
    border-radius: 10px !important;
    padding: .75rem 2rem !important;
    letter-spacing: .04em !important;
    transition: opacity .15s !important;
    width: 100%;
}
.stButton > button:hover { opacity: .85 !important; }

/* ── Tab strip ───────────────────────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-card);
    border-radius: 10px;
    padding: 4px;
    gap: 4px;
    border: 1px solid var(--border);
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: var(--text-mid);
    border-radius: 8px;
    padding: .5rem 1.2rem;
    font-weight: 500;
}
.stTabs [aria-selected="true"] {
    background: var(--primary) !important;
    color: #0a0c10 !important;
    font-weight: 700;
}

/* ── Divider ─────────────────────────────────────────────────────────────── */
hr { border-color: var(--border) !important; }

/* ── Animation keyframes ─────────────────────────────────────────────────── */
@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0);    }
}
</style>
""", unsafe_allow_html=True)


# =============================================================================
# 3.  DATA LOADING
# =============================================================================
# @st.cache_data is a Streamlit decorator that caches the function's return
# value.  The first time it runs it will execute normally; on every subsequent
# call (e.g. when the user changes a widget) Streamlit skips re-execution and
# returns the cached result instantly.  This is critical for performance when
# loading and preprocessing large datasets.

@st.cache_data
def load_data(filepath: str) -> pd.DataFrame:
    """
    Load the CSV dataset from disk into a pandas DataFrame.

    Parameters
    ----------
    filepath : str
        Absolute or relative path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Raw dataset, exactly as read from the file.
    """

    # pd.read_csv infers column types automatically.
    # It will detect int64, float64 and object (string) columns.
    df = pd.read_csv(filepath)

    return df


# =============================================================================
# 4.  PREPROCESSING PIPELINE
# =============================================================================
# Raw data typically cannot be fed directly into a ML model:
#   • Categorical text columns must be converted to numbers.
#   • Numerical columns with very different scales (e.g. sqft vs. tax rate)
#     should be standardised so no single feature dominates the loss.
#   • The target column (price_usd) must be separated from the features.
#
# We encapsulate all of this in one function so it can be called once and
# the fitted transformers (encoder, scaler) reused at prediction time.

@st.cache_data
def preprocess(df: pd.DataFrame):
    """
    Encode categorical columns, separate target, and standardise features.

    Parameters
    ----------
    df : pd.DataFrame
        Raw dataset returned by load_data().

    Returns
    -------
    X_scaled : np.ndarray          – Scaled feature matrix (all numeric)
    y         : pd.Series          – Target variable (price_usd)
    feature_names : list[str]      – Column names after encoding
    label_encoders : dict          – Fitted LabelEncoder per categorical column
    scaler        : StandardScaler – Fitted scaler (needed to transform new inputs)
    """

    # ── 4a. Separate target from features ────────────────────────────────────
    # The target is the value we want to predict.  We remove it from the
    # feature matrix so the model cannot "cheat" by seeing the answer.

    TARGET_COLUMN = "price_usd"
    y = df[TARGET_COLUMN]                       # Series of house prices
    X = df.drop(columns=[TARGET_COLUMN])        # DataFrame without price column

    # ── 4b. Identify categorical vs. numerical columns ───────────────────────
    # pandas dtype "object" usually means the column contains strings.
    # We treat those as categorical and everything else as numerical.

    categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
    # e.g. ["neighborhood", "market_trend"]

    numerical_cols   = X.select_dtypes(exclude=["object"]).columns.tolist()
    # e.g. ["sqft_living", "sqft_lot", "bedrooms", ...]

    # ── 4c. Label-encode categorical columns ─────────────────────────────────
    # LabelEncoder assigns a unique integer to each category:
    #   "Downtown" → 0,  "Rural" → 1,  "Suburbs" → 2,  etc.
    # We store each fitted encoder in a dict so we can apply the same mapping
    # to new user inputs later (at prediction time).

    label_encoders: dict = {}

    for col in categorical_cols:
        le = LabelEncoder()
        # fit_transform: learns the mapping AND applies it in one step
        X[col] = le.fit_transform(X[col])
        label_encoders[col] = le   # save for reuse

    # ── 4d. Feature names (after encoding, all columns are numeric) ──────────
    feature_names = X.columns.tolist()

    # ── 4e. Standardise numerical features ───────────────────────────────────
    # StandardScaler transforms each column to have mean ≈ 0 and std ≈ 1:
    #   z = (x - mean) / std
    # This prevents features with large magnitudes (e.g. sqft_living ≈ 2000)
    # from drowning out small-magnitude features (e.g. floors ≈ 1–3).
    # Note: Random Forests are actually scale-invariant, but scaling is shown
    # here as a best-practice pattern used by other algorithms (SVM, KNN, etc.).

    scaler = StandardScaler()
    # fit_transform on the whole DataFrame – learns mean & std from training data
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, feature_names, label_encoders, scaler


# =============================================================================
# 5.  MODEL TRAINING & EVALUATION
# =============================================================================
# We use a Random Forest Regressor – an ensemble of decision trees.
# Key ideas:
#   • Each tree is trained on a random BOOTSTRAP sample of the training data.
#   • At every split, only a random SUBSET of features is considered.
#   • The final prediction is the AVERAGE of all trees' predictions.
# This reduces over-fitting compared to a single deep decision tree.

@st.cache_data
def train_model(X_scaled: np.ndarray, y: pd.Series):
    """
    Split data, train a Random Forest, and return evaluation metrics.

    Parameters
    ----------
    X_scaled : np.ndarray   Feature matrix (standardised).
    y        : pd.Series    Target values (house prices).

    Returns
    -------
    model     : RandomForestRegressor  – Trained estimator
    X_test    : np.ndarray             – Held-out feature matrix
    y_test    : pd.Series              – Held-out true prices
    y_pred    : np.ndarray             – Model's predictions on X_test
    metrics   : dict                   – MAE, RMSE, R² scores
    """

    # ── 5a. Train / Test split ────────────────────────────────────────────────
    # We reserve 20 % of rows for testing.  The model NEVER sees these during
    # training, so they give an honest estimate of real-world performance.
    # random_state=42 makes the split reproducible (same seed → same split).

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y,
        test_size=0.20,     # 20 % held out
        random_state=42     # fixed seed for reproducibility
    )

    # ── 5b. Instantiate and fit the model ─────────────────────────────────────
    # Hyperparameters:
    #   n_estimators  – number of trees (more = better, slower)
    #   max_depth     – maximum depth per tree (None = grow fully)
    #   min_samples_split – min samples required to split a node (regularisation)
    #   n_jobs=-1     – use all available CPU cores for parallel training

    model = RandomForestRegressor(
        n_estimators=200,       # 200 decision trees in the ensemble
        max_depth=None,         # let trees grow until leaves are pure
        min_samples_split=4,    # a node needs ≥ 4 samples to be split
        random_state=42,        # reproducible tree building
        n_jobs=-1               # parallelise across all CPU cores
    )

    # .fit() is where all the learning happens.
    # The model scans training data, builds 200 trees, and stores them.
    model.fit(X_train, y_train)

    # ── 5c. Generate predictions on the test set ──────────────────────────────
    # .predict() feeds X_test through every tree and averages the outputs.
    y_pred = model.predict(X_test)

    # ── 5d. Compute evaluation metrics ────────────────────────────────────────
    # MAE  – Mean Absolute Error: average dollar distance from truth
    # RMSE – Root Mean Squared Error: punishes large errors more
    # R²   – Coefficient of Determination: 1.0 = perfect, 0.0 = baseline mean

    mae  = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2   = r2_score(y_test, y_pred)

    metrics = {"MAE": mae, "RMSE": rmse, "R²": r2}

    return model, X_test, y_test, y_pred, metrics


# =============================================================================
# 6.  PREDICTION HELPER
# =============================================================================
# When a user fills in the sidebar form and clicks "Predict", we receive raw
# inputs (strings, floats, ints).  We must apply the SAME transformations that
# were applied to the training data before calling model.predict().

def predict_price(
    raw_input: dict,
    model: RandomForestRegressor,
    label_encoders: dict,
    scaler: StandardScaler,
    feature_names: list
) -> float:
    """
    Transform raw user input into a scaled feature vector and return the
    predicted house price.

    Parameters
    ----------
    raw_input      : dict  – {column_name: raw_value} from the UI
    model          : RandomForestRegressor
    label_encoders : dict  – encoders fitted during preprocessing
    scaler         : StandardScaler – scaler fitted during preprocessing
    feature_names  : list  – ordered list of feature columns

    Returns
    -------
    float : predicted price in USD
    """

    # Build a single-row DataFrame in the exact column order used for training.
    # This is important – the model expects features in the same order every time.
    input_df = pd.DataFrame([raw_input], columns=feature_names)

    # Apply label-encoding to categorical columns using the SAVED encoder.
    # We must use transform() (not fit_transform()) so we use the original mapping.
    for col, le in label_encoders.items():
        if col in input_df.columns:
            # .transform() maps the string label → integer
            input_df[col] = le.transform(input_df[col])

    # Apply the SAVED scaler (same mean & std as training data).
    input_scaled = scaler.transform(input_df)

    # model.predict returns a numpy array; [0] extracts the single value.
    predicted = model.predict(input_scaled)[0]

    return predicted


# =============================================================================
# 7.  CHART HELPERS
# =============================================================================
# All charts use Plotly, which renders as interactive HTML inside Streamlit.
# We define a shared layout template so every chart matches our dark theme.

# A reusable Plotly layout dictionary for the dark theme
PLOT_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",  # transparent outer background
    plot_bgcolor ="#12151c",        # dark inner plot area
    font         =dict(family="DM Sans", color="#9aa3b8"),
    title_font   =dict(family="Playfair Display", color="#f0ece4"),
    xaxis        =dict(gridcolor="#2a3045", linecolor="#2a3045", tickfont=dict(color="#9aa3b8")),
    yaxis        =dict(gridcolor="#2a3045", linecolor="#2a3045", tickfont=dict(color="#9aa3b8")),
    margin       =dict(l=20, r=20, t=50, b=20),
)


def chart_actual_vs_predicted(y_test, y_pred) -> go.Figure:
    """
    Scatter plot: actual prices (x-axis) vs. predicted prices (y-axis).
    A perfect model would place all points on the diagonal y = x line.
    """

    fig = go.Figure()

    # ── Scatter points ────────────────────────────────────────────────────────
    fig.add_trace(go.Scatter(
        x=y_test, y=y_pred,
        mode="markers",
        marker=dict(color="#e8a838", opacity=0.55, size=6),
        name="Predictions",
        hovertemplate="Actual: $%{x:,.0f}<br>Predicted: $%{y:,.0f}<extra></extra>"
    ))

    # ── Perfect-fit diagonal line ─────────────────────────────────────────────
    # If every prediction were exact, every point would lie on this line.
    price_range = [int(min(y_test.min(), y_pred.min())),
                   int(max(y_test.max(), y_pred.max()))]

    fig.add_trace(go.Scatter(
        x=price_range, y=price_range,
        mode="lines",
        line=dict(color="#3ecf8e", width=2, dash="dash"),
        name="Perfect Fit"
    ))

    fig.update_layout(
        **PLOT_LAYOUT,
        title="Actual vs. Predicted Prices",
        xaxis_title="Actual Price (USD)",
        yaxis_title="Predicted Price (USD)",
        legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor="#2a3045")
    )

    return fig


def chart_feature_importance(model, feature_names, top_n=15) -> go.Figure:
    """
    Horizontal bar chart of the top-N most important features.

    Random Forests measure feature importance as the average decrease in
    node impurity (Gini / variance) a feature causes across all trees.
    Higher importance → the feature is more useful for prediction.
    """

    # Extract importance scores from the fitted model
    importances = model.feature_importances_   # shape: (n_features,)

    # Pair each feature name with its importance score, then sort descending
    fi_df = (
        pd.DataFrame({"feature": feature_names, "importance": importances})
        .sort_values("importance", ascending=True)   # ascending for horizontal bar
        .tail(top_n)                                 # keep top N features
    )

    fig = px.bar(
        fi_df,
        x="importance",
        y="feature",
        orientation="h",
        color="importance",
        color_continuous_scale=[[0, "#2a3045"], [0.4, "#b07820"], [1, "#e8a838"]],
        labels={"importance": "Importance Score", "feature": "Feature"},
        title=f"Top {top_n} Feature Importances"
    )

    fig.update_layout(**PLOT_LAYOUT, coloraxis_showscale=False)
    fig.update_traces(hovertemplate="%{y}: %{x:.4f}<extra></extra>")

    return fig


def chart_residuals(y_test, y_pred) -> go.Figure:
    """
    Residual plot: predicted price (x) vs. residual (y_test - y_pred).
    Residual = actual − predicted.
    • A good model has residuals randomly scattered around 0 (no pattern).
    • Patterns (e.g. funnel shape) indicate the model is systematically wrong
      for certain price ranges – a sign of heteroscedasticity.
    """

    residuals = np.array(y_test) - y_pred

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=y_pred, y=residuals,
        mode="markers",
        marker=dict(color="#9aa3b8", opacity=0.50, size=5),
        name="Residual",
        hovertemplate="Predicted: $%{x:,.0f}<br>Residual: $%{y:,.0f}<extra></extra>"
    ))

    # Horizontal reference line at y = 0 (zero error)
    fig.add_hline(y=0, line_color="#e8534a", line_dash="dash", line_width=2)

    fig.update_layout(
        **PLOT_LAYOUT,
        title="Residual Plot (Error Distribution)",
        xaxis_title="Predicted Price (USD)",
        yaxis_title="Residual (Actual − Predicted)"
    )

    return fig


def chart_error_distribution(y_test, y_pred) -> go.Figure:
    """
    Histogram of prediction errors as a percentage of the actual price.
    Shows how concentrated or spread the model's mistakes are.
    """

    pct_errors = (np.array(y_test) - y_pred) / np.array(y_test) * 100

    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=pct_errors,
        nbinsx=40,
        marker_color="#e8a838",
        opacity=0.8,
        name="% Error"
    ))

    fig.update_layout(
        **PLOT_LAYOUT,
        title="Distribution of Prediction Errors (%)",
        xaxis_title="Error (%)",
        yaxis_title="Count"
    )

    return fig


def chart_price_distribution(df) -> go.Figure:
    """Histogram of the target variable (house prices)."""

    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=df["price_usd"],
        nbinsx=50,
        marker_color="#3ecf8e",
        opacity=0.8
    ))

    fig.update_layout(
        **PLOT_LAYOUT,
        title="Price Distribution in Dataset",
        xaxis_title="Price (USD)",
        yaxis_title="Number of Houses"
    )

    return fig


# =============================================================================
# 8.  MAIN APPLICATION LAYOUT
# =============================================================================
# Everything below builds the actual Streamlit page.
# Streamlit executes top-to-bottom on every interaction; cached functions
# prevent redundant re-computation.

def main():

    # ── 8a. Load and preprocess data ──────────────────────────────────────────
    DATA_PATH = os.path.join(os.path.dirname(__file__), "housing_synthetic.csv")

    if not os.path.exists(DATA_PATH):
        st.error(
            f"Dataset not found at **{DATA_PATH}**.  "
            "Place `housing_synthetic.csv` in the same folder as `app.py`."
        )
        st.stop()   # Halt execution – nothing can work without the data

    df = load_data(DATA_PATH)

    # Unpack the five return values of preprocess()
    X_scaled, y, feature_names, label_encoders, scaler = preprocess(df)

    # ── 8b. Train model ───────────────────────────────────────────────────────
    model, X_test, y_test, y_pred, metrics = train_model(X_scaled, y)

    # ── 8c. Hero header ───────────────────────────────────────────────────────
    st.markdown("""
    <div class="hero-header">
        <div class="hero-title">HomeValue <span>AI</span></div>
        <div class="hero-sub">
            Random Forest · 2,000 properties · 23 features &nbsp;|&nbsp;
            Predict, explore, and understand house price drivers
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── 8d. Metric row – model performance summary ────────────────────────────
    # Display MAE, RMSE, R² and dataset stats as at-a-glance KPI cards.
    col1, col2, col3, col4, col5 = st.columns(5)

    kpis = [
        (col1, "R² Score",         f"{metrics['R²']:.3f}",    "Variance explained"),
        (col2, "MAE",              f"${metrics['MAE']:,.0f}",  "Avg absolute error"),
        (col3, "RMSE",             f"${metrics['RMSE']:,.0f}", "Root mean sq. error"),
        (col4, "Training Rows",    f"{int(len(y)*0.8):,}",     "80 % of dataset"),
        (col5, "Test Rows",        f"{int(len(y)*0.2):,}",     "20 % held-out"),
    ]

    for col, label, value, note in kpis:
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-note">{note}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── 8e. Tab navigation ────────────────────────────────────────────────────
    # Tabs keep the UI clean – each logical section lives in its own tab.

    tab_predict, tab_perf, tab_data = st.tabs([
        "🏡  Predict a Price",
        "📊  Model Performance",
        "🔍  Data Explorer",
    ])


    # =========================================================================
    # TAB 1 – PREDICT A PRICE
    # =========================================================================
    with tab_predict:

        st.markdown('<div class="section-title">Configure Your Property</div>', unsafe_allow_html=True)
        st.markdown('<div class="info-box">Adjust the sliders and dropdowns in the sidebar, then click <strong>Predict Price</strong> to get an AI-powered estimate.</div>', unsafe_allow_html=True)

        # ── Sidebar – user input controls ─────────────────────────────────────
        with st.sidebar:
            st.markdown("## 🏠 Property Details")
            st.markdown("---")

            # ── Categorical inputs (dropdowns) ────────────────────────────────
            # We extract the unique categories directly from the dataset so
            # the dropdown always matches what the model was trained on.

            neighborhood_opts = sorted(df["neighborhood"].unique().tolist())
            neighborhood = st.selectbox("📍 Neighborhood", neighborhood_opts,
                                        help="The neighborhood type affects price significantly.")

            market_opts = sorted(df["market_trend"].unique().tolist())
            market_trend = st.selectbox("📈 Market Trend", market_opts,
                                        help="Current market direction in the area.")

            st.markdown("---")
            st.markdown("**🏗️ Size & Structure**")

            # ── Numerical inputs (sliders) ─────────────────────────────────────
            # We infer min/max from the dataset so sliders stay within realistic bounds.

            sqft_living = st.slider("Living Area (sqft)",
                                    int(df.sqft_living.min()), int(df.sqft_living.max()),
                                    int(df.sqft_living.median()))

            sqft_lot = st.slider("Lot Size (sqft)",
                                 int(df.sqft_lot.min()), int(df.sqft_lot.max()),
                                 int(df.sqft_lot.median()))

            bedrooms   = st.slider("Bedrooms",  int(df.bedrooms.min()),  int(df.bedrooms.max()),  3)
            bathrooms  = st.slider("Bathrooms", int(df.bathrooms.min()), int(df.bathrooms.max()), 2)
            floors     = st.slider("Floors",    1, int(df.floors.max()), 2)

            st.markdown("---")
            st.markdown("**🏠 Features**")

            has_basement  = st.checkbox("Has Basement",  value=True)
            basement_sqft = st.slider("Basement Area (sqft)", 0, int(df.basement_sqft.max()), 500,
                                      disabled=not has_basement)
            garage_cars   = st.slider("Garage Capacity (cars)", 0, int(df.garage_cars.max()), 2)
            has_pool      = st.checkbox("Has Pool", value=False)

            st.markdown("---")
            st.markdown("**📅 Age & Condition**")

            year_built       = st.slider("Year Built", int(df.year_built.min()), 2024, 2000)
            house_age_years  = 2024 - year_built   # derived automatically from year_built
            renovated        = st.checkbox("Recently Renovated", value=False)
            condition_score  = st.slider("Condition Score (1–10)", 1, 10, 7)
            quality_grade    = st.slider("Quality Grade (1–5)",    1, 5,  3)

            st.markdown("---")
            st.markdown("**📍 Location Metrics**")

            school_rating        = st.slider("School Rating",           1.0, 5.0, 3.5, 0.1)
            crime_rate_per_1000  = st.slider("Crime Rate (per 1,000)",  0.0, 20.0, 5.0, 0.1)
            dist_city_center_km  = st.slider("Distance to City (km)",   0.0, 80.0, 15.0, 0.5)
            dist_school_km       = st.slider("Distance to School (km)", 0.0, 20.0, 5.0, 0.5)
            dist_hospital_km     = st.slider("Distance to Hospital (km)", 0.0, 35.0, 10.0, 0.5)

            st.markdown("---")
            st.markdown("**💰 Financial Details**")

            property_tax_rate_pct = st.slider("Property Tax Rate (%)", 0.5, 2.0, 1.0, 0.01)
            hoa_monthly_usd       = st.slider("HOA Monthly Fee (USD)", 0, 600, 0, 10)

            st.markdown("---")

            # ── Predict button ────────────────────────────────────────────────
            predict_clicked = st.button("🔮  Predict Price")

        # ── Assemble raw input dict ────────────────────────────────────────────
        # This mirrors the exact column names in the training data.
        raw_input = {
            "neighborhood":           neighborhood,
            "sqft_living":            sqft_living,
            "sqft_lot":               sqft_lot,
            "bedrooms":               bedrooms,
            "bathrooms":              bathrooms,
            "floors":                 float(floors),
            "has_basement":           int(has_basement),
            "basement_sqft":          basement_sqft if has_basement else 0,
            "garage_cars":            garage_cars,
            "has_pool":               int(has_pool),
            "year_built":             year_built,
            "house_age_years":        house_age_years,
            "renovated":              int(renovated),
            "condition_score":        condition_score,
            "quality_grade":          quality_grade,
            "school_rating":          school_rating,
            "crime_rate_per_1000":    crime_rate_per_1000,
            "dist_city_center_km":    dist_city_center_km,
            "dist_school_km":         dist_school_km,
            "dist_hospital_km":       dist_hospital_km,
            "property_tax_rate_pct":  property_tax_rate_pct,
            "hoa_monthly_usd":        hoa_monthly_usd,
            "market_trend":           market_trend,
        }

        # ── Prediction output ──────────────────────────────────────────────────
        if predict_clicked:
            price = predict_price(raw_input, model, label_encoders, scaler, feature_names)

            # Compute a simple ±10 % confidence interval.
            # Random Forests don't natively output confidence intervals; this
            # is a heuristic approximation based on model RMSE.
            lower = price * 0.90
            upper = price * 1.10

            st.markdown(f"""
            <div class="prediction-box">
                <div class="prediction-label">Estimated Market Value</div>
                <div class="prediction-price">${price:,.0f}</div>
                <div class="prediction-range">Confidence Range: ${lower:,.0f} — ${upper:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)

            # ── Two-column context block ────────────────────────────────────
            st.markdown("<br>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)

            with c1:
                # How does this prediction compare to the dataset average?
                avg_price = df["price_usd"].mean()
                delta_pct  = (price - avg_price) / avg_price * 100
                arrow      = "↑" if delta_pct >= 0 else "↓"
                color      = "#3ecf8e" if delta_pct >= 0 else "#e8534a"
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">vs. Dataset Average</div>
                    <div class="metric-value" style="color:{color}">
                        {arrow} {abs(delta_pct):.1f}%
                    </div>
                    <div class="metric-note">Average: ${avg_price:,.0f}</div>
                </div>
                """, unsafe_allow_html=True)

            with c2:
                # What price-per-sqft does this correspond to?
                ppsf = price / sqft_living
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">Price per Sq Ft</div>
                    <div class="metric-value">${ppsf:,.0f}</div>
                    <div class="metric-note">{sqft_living:,} sqft × ${ppsf:,.0f}/sqft</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            # Placeholder before user clicks Predict
            st.markdown("""
            <div style="text-align:center; padding:3rem; color:#4a5268;">
                <div style="font-size:3rem;">🏡</div>
                <div style="font-size:1.1rem; margin-top:.8rem;">
                    Configure your property in the sidebar, then click
                    <strong style="color:#e8a838;">Predict Price</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)


    # =========================================================================
    # TAB 2 – MODEL PERFORMANCE
    # =========================================================================
    with tab_perf:

        st.markdown('<div class="section-title">Model Evaluation</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="info-box">
        These charts evaluate how well the Random Forest generalises to <strong>unseen data</strong>.
        All metrics are computed on the 20% test split that was withheld during training.
        </div>
        """, unsafe_allow_html=True)

        # Row 1 – Actual vs Predicted  &  Feature Importance
        r1c1, r1c2 = st.columns(2)

        with r1c1:
            st.plotly_chart(chart_actual_vs_predicted(y_test, y_pred),
                            use_container_width=True)

        with r1c2:
            st.plotly_chart(chart_feature_importance(model, feature_names),
                            use_container_width=True)

        # Row 2 – Residuals  &  Error distribution
        r2c1, r2c2 = st.columns(2)

        with r2c1:
            st.plotly_chart(chart_residuals(y_test, y_pred),
                            use_container_width=True)

        with r2c2:
            st.plotly_chart(chart_error_distribution(y_test, y_pred),
                            use_container_width=True)

        # ── Interpretation guide ───────────────────────────────────────────────
        st.markdown('<div class="section-title">How to Read These Charts</div>', unsafe_allow_html=True)

        ic1, ic2 = st.columns(2)

        with ic1:
            st.markdown("""
            <div class="info-box">
            <strong>Actual vs Predicted</strong><br>
            Each dot is a test house.  The closer all dots cluster around the
            dashed green diagonal, the more accurate the model is.  Dots above
            the line mean the model over-predicted; below = under-predicted.
            </div>
            <div class="info-box">
            <strong>Feature Importance</strong><br>
            Longer bars = more influential.  The model assigns a score to each
            feature based on how much it reduces prediction error across all
            trees.  Use this to understand which factors drive price most.
            </div>
            """, unsafe_allow_html=True)

        with ic2:
            st.markdown("""
            <div class="info-box">
            <strong>Residual Plot</strong><br>
            Residual = Actual − Predicted.  A well-calibrated model should
            show residuals randomly scattered around zero with no obvious
            pattern or funnel shape.
            </div>
            <div class="info-box">
            <strong>Error Distribution</strong><br>
            A tight, symmetric bell curve centred near 0% means errors are
            small and unbiased.  A wide or skewed histogram indicates the
            model struggles in certain price ranges.
            </div>
            """, unsafe_allow_html=True)


    # =========================================================================
    # TAB 3 – DATA EXPLORER
    # =========================================================================
    with tab_data:

        st.markdown('<div class="section-title">Dataset Overview</div>', unsafe_allow_html=True)

        # ── Summary stats ──────────────────────────────────────────────────────
        dc1, dc2, dc3, dc4 = st.columns(4)
        stats = [
            (dc1, "Rows",     f"{len(df):,}",                      "Total properties"),
            (dc2, "Features", f"{len(df.columns)-1}",              "Input columns"),
            (dc3, "Min Price",f"${df.price_usd.min():,.0f}",       "Cheapest house"),
            (dc4, "Max Price",f"${df.price_usd.max():,.0f}",       "Most expensive"),
        ]
        for col, label, val, note in stats:
            with col:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{val}</div>
                    <div class="metric-note">{note}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Price distribution ─────────────────────────────────────────────────
        ec1, ec2 = st.columns(2)

        with ec1:
            st.plotly_chart(chart_price_distribution(df), use_container_width=True)

        with ec2:
            # Box plot: price by neighborhood
            fig_box = px.box(
                df, x="neighborhood", y="price_usd",
                color="neighborhood",
                color_discrete_sequence=["#e8a838","#3ecf8e","#9aa3b8","#e8534a","#6c8ebf"],
                title="Price by Neighborhood",
                labels={"price_usd": "Price (USD)", "neighborhood": ""}
            )
            fig_box.update_layout(**PLOT_LAYOUT, showlegend=False)
            st.plotly_chart(fig_box, use_container_width=True)

        # ── Scatter: sqft_living vs price, coloured by market_trend ────────────
        fig_scatter = px.scatter(
            df, x="sqft_living", y="price_usd",
            color="market_trend",
            opacity=0.55,
            color_discrete_map={
                "Rising":   "#3ecf8e",
                "Stable":   "#e8a838",
                "Declining":"#e8534a"
            },
            title="Living Area vs. Price (coloured by Market Trend)",
            labels={"sqft_living": "Living Area (sqft)", "price_usd": "Price (USD)"}
        )
        fig_scatter.update_layout(**PLOT_LAYOUT)
        st.plotly_chart(fig_scatter, use_container_width=True)

        # ── Raw data table ─────────────────────────────────────────────────────
        with st.expander("📋 View Raw Data (first 100 rows)"):
            st.dataframe(
                df.head(100),
                use_container_width=True,
                height=400
            )


# =============================================================================
# 9.  ENTRY POINT
# =============================================================================
# Python convention: this block runs only when the file is executed directly
# (not when imported as a module).

if __name__ == "__main__":
    main()
