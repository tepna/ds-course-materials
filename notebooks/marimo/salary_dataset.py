import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    import altair as alt
    from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    from sklearn.linear_model import LinearRegression
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
    from sklearn.neighbors import KNeighborsRegressor
    from xgboost import XGBClassifier, XGBRegressor
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    return (
        DecisionTreeRegressor,
        GradientBoostingRegressor,
        KNeighborsRegressor,
        LabelEncoder,
        LinearRegression,
        OrdinalEncoder,
        Pipeline,
        RandomForestRegressor,
        StandardScaler,
        XGBRegressor,
        go,
        mean_absolute_error,
        mean_squared_error,
        np,
        pd,
        r2_score,
        train_test_split,
    )


@app.cell
def _(mo, pd):
    # Salary Data
    df_salary = pd.read_csv("datasets/salary_data/salary_data.csv")
    df_salary = (
        df_salary[["Age", "Gender", "Education Level", "Years of Experience", "Salary"]]
        .dropna()
        .reset_index(drop=True)
    )
    mo.vstack([mo.md("###Salary Dataset"), mo.ui.table(df_salary, selection=None)])
    return (df_salary,)


@app.cell
def _(df_salary, mo):
    mo.vstack([mo.md("---- \n###Summary statistics"), mo.plain(df_salary.describe().T)])
    return


@app.cell
def _(mo):
    # UI widgets
    model_choice = mo.ui.dropdown(
        options=[
            "LinearRegression",
            "DecisionTreeRegressor",
            "RandomForestRegressor",
            "GradientBoostingRegressor",
            "XGBRegressor",
            "KNeighborsRegressor",
        ],
        value="LinearRegression",
    )

    # Show UI in the notebook
    mo.vstack([mo.md("---- \n###Choose regression model"), model_choice])
    return (model_choice,)


@app.cell
def _(LabelEncoder, OrdinalEncoder, df_salary):
    # Preprocessing: 

    # გარდავქმნათ str სვეტები რიცხვოვან მონაცემებთან categorical -> numerical
    encoder = LabelEncoder()
    df_salary["Gender"] = encoder.fit_transform(df_salary["Gender"])

    enc = OrdinalEncoder(categories=[["Bachelor's", "Master's", "PhD"]], handle_unknown="use_encoded_value", unknown_value=-1)
    df_salary["Education Level"] = enc.fit_transform(df_salary[["Education Level"]]).astype(int)
    return


@app.cell
def _(df_salary, train_test_split):
    # მონაცემების მომზადება მოდელის გასაწვრთნელად
    X = df_salary.drop(columns="Salary")
    y = df_salary["Salary"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_test, X_train, y_test, y_train


@app.cell
def _(
    DecisionTreeRegressor,
    GradientBoostingRegressor,
    KNeighborsRegressor,
    LinearRegression,
    RandomForestRegressor,
    XGBRegressor,
    model_choice,
):
    # Choose model
    model_map = {
    "LinearRegression": LinearRegression(),
    "DecisionTreeRegressor": DecisionTreeRegressor(max_depth=8),
    "RandomForestRegressor": RandomForestRegressor(
       n_estimators=200, max_depth=8, random_state=42
    ),
    "GradientBoostingRegressor": GradientBoostingRegressor(
       n_estimators=200, learning_rate=0.1, max_depth=3, random_state=42
    ),
    "XGBRegressor": XGBRegressor(
       n_estimators=200, learning_rate=0.1, random_state=42
    ),
    "KNeighborsRegressor": KNeighborsRegressor(n_neighbors=5),
    }

    model = model_map[model_choice.value]
    return (model,)


@app.cell
def _(Pipeline, StandardScaler, model, model_choice):
    if model_choice.value in ["KNeighborsRegressor"]:
        pipe = Pipeline([
            ("scale", StandardScaler()),
            ("model", model),
        ])
    else:
        pipe = Pipeline([
            ("model", model),
        ])
    return (pipe,)


@app.cell
def _(X_test, X_train, pipe, y_train):
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    return (y_pred,)


@app.cell
def _(
    go,
    mean_absolute_error,
    mean_squared_error,
    mo,
    np,
    pd,
    r2_score,
    y_pred,
    y_test,
):
    # ევალუაციის მეტრიკები
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    # DataFrame for convenience
    df_plot = pd.DataFrame({
        "Actual": y_test,
        "Predicted": y_pred,
    })

    # y = x reference line
    line_min = min(df_plot["Actual"].min(), df_plot["Predicted"].min())
    line_max = max(df_plot["Actual"].max(), df_plot["Predicted"].max())

    fig = go.Figure()

    # Scatter: Actual vs Predicted
    fig.add_trace(
        go.Scatter(
            x=df_plot["Actual"],
            y=df_plot["Predicted"],
            mode="markers",
            opacity=0.5,
            name="Points",
            hovertemplate="Actual: %{x}<br>Predicted: %{y}<extra></extra>",
        )
    )

    # y = x reference line
    fig.add_trace(
        go.Scatter(
            x=[line_min, line_max],
            y=[line_min, line_max],
            mode="lines",
            line=dict(dash="dash"),
            name="y = x",
        )
    )

    fig.update_layout(
        title="Actual vs Predicted Salary",
        xaxis_title="Actual Values",
        yaxis_title="Predicted Values",
        width=500,
        height=350,
    )

    metrics = pd.DataFrame(
        {
            "MAE": [mae],
            "MSE": [mse],
            "RMSE": [rmse],
            "R2": [r2],
        },
        index=["Value"], 
    ).rename_axis("Metric")


    mo.vstack(
        [
            mo.md("### Model Evaluation"),
            mo.plain(metrics.round(2)),
            fig
        ]
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
