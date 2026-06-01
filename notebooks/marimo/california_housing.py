import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import plotly.express as px
    import seaborn as sns
    import shap

    from sklearn.compose import ColumnTransformer
    from sklearn.impute import SimpleImputer
    from sklearn.linear_model import LinearRegression
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
    from sklearn.neighbors import KNeighborsRegressor
    from sklearn.svm import LinearSVR, SVR
    from xgboost import XGBRegressor
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    return (
        ColumnTransformer,
        DecisionTreeRegressor,
        GradientBoostingRegressor,
        KNeighborsRegressor,
        LinearRegression,
        OneHotEncoder,
        Pipeline,
        RandomForestRegressor,
        SVR,
        SimpleImputer,
        StandardScaler,
        XGBRegressor,
        mean_absolute_error,
        mean_squared_error,
        mo,
        np,
        pd,
        plt,
        px,
        r2_score,
        sns,
        train_test_split,
    )


@app.cell
def _():
    import warnings
    warnings.filterwarnings("ignore")
    return


@app.cell
def _(mo):
    mo.md(r"""
    # The California housing dataset
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ამ ნოუთბუქში ეტაპობრივად გავივლით მანქანური სწავლების სრულ პროცესს
    **California Housing** მონაცემების გამოყენებით.

    განვიხილავთ:

    - მონაცემების ჩატვირთვას
    - პრობლემის დასმა და ამოცანის ტიპის განსაზღვრას
    - მონაცემთა კვლევით ანალიზს (EDA)
    - მონაცემების დამუშავებას
    - Feature Engineering-ს
    - Feature Encoding-სა და Feature Scaling-ს
    - მანქანური სწავლების მოდელს
    - შედეგების შეფასებასა და ახსნას

    ------------------------------------------------
    """)
    return


@app.cell
def _(mo):
    mo.image(
        "notebooks/Additional Resources/public/cycle.png",
        width=700
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## **1. მონაცემების ჩატვირთვა**
    """)
    return


@app.cell
def _(pd):
    df_housing = pd.read_csv("datasets/house_prices/california_housing.csv")
    df_housing.head()
    return (df_housing,)


@app.cell
def _(mo):
    mo.md(r"""
    სვეტების აღწერა:

    | სვეტი             | მნიშვნელობა                                                                                         |
    | ------------------ | --------------------------------------------------------------------------------------------------- |
    | **MedInc**         | მოსახლეობის საშუალო შემოსავალი მოცემულ რეგიონში                                    |
    | **HouseAge**       | რეგიონში არსებული სახლების საშუალო ასაკი                                               |
    | **TotalRooms**     | საცხოვრებელ ერთეულებში არსებული ოთახების საერთო რაოდენობა                                          |
    | **TotalBedrms**    | საცხოვრებელ ერთეულებში არსებული საძინებლების საერთო რაოდენობა                                    |
    | **Population**     | მოცემულ რეგიონში მცხოვრები მოსახლეობის საერთო რაოდენობა                                            |
    | **Households**     | რეგიონში არსებული ოჯახების რაოდენობა                                              |
    | **Latitude**       | რეგიონის გეოგრაფიული განედი                            |
    | **Longitude**      | რეგიონის გეოგრაფიული გრძედი                        |
    | **MedHouseVal**    | სახლების საშუალო ღირებულება მოცემულ რეგიონში |
    | **OceanProximity** | აღწერს რამდენად ახლოს არის რეგიონი ოკეანესთან                      |

    ------------------------------------------------
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## **2. ამოცანის განსაზღვრა**
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    მოცემული რაიონის მახასიათებლების მიხედვით, როგორიცაა მოსახლეობის შემოსავალი, მდებარეობა, რა შეიძლება იყოს ამ რაიონში სახლების საშუალო ღირებულება?

    ჩვენი მიზანია **სახლების საშუალო ღირებულების** (`MedHouseVal`) პროგნოზი.

    - **supervised learning** ამოცანა, რადგან გვაქვს სამიზნე ცვლადი
    - **regression** ამოცანა, რადგან სამიზნე არის რიცხვითი მნიშვნელობა

    ------------------------------------------------
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## **3. მონაცემების საწყისი დათვალიერება**

    მოდელის აგებამდე მნიშვნელოვანია გავიგოთ:

    - რა ტიპის მონაცემებია თითოეულ სვეტში
    - არის თუ არა გამოტოვებული მნიშვნელობები (None/missing values)
    - როგორია რიცხვითი ცვლადების განაწილება
    """)
    return


@app.cell
def _(df_housing):
    df_housing.info()
    return


@app.cell
def _(df_housing):
    print(df_housing.duplicated().sum())
    return


@app.cell
def _(df_housing):
    df_housing.isnull().sum()
    return


@app.cell
def _(df_housing, np):
    df_housing.drop(columns=["Longitude", "Latitude"]).describe(include=np.number)
    return


@app.cell
def _(df_housing):
    print(df_housing["OceanProximity"].unique())
    return


@app.cell
def _(mo):
    mo.md(r"""
    ------------------------------------------------
    ## **4. მონაცემთა კვლევითი ანალიზი (EDA)**
    """)
    return


@app.cell
def _(df_housing, px):
    _fig = px.scatter_map(
        df_housing,
        lat="Latitude",
        lon="Longitude",
        color="MedHouseVal",
        size="Population",
        zoom=5,
        height=600,
        map_style="carto-positron",
        color_continuous_scale="Turbo",
        labels={"MedHouseVal": "Median House Value"}
    )
    _fig.update_layout(
        title="California Housing Prices by Location",
        margin={"r":0,"t":40,"l":0,"b":0}
    )
    _fig
    return


@app.cell
def _(df_housing, np, plt, sns):
    features = df_housing.drop(columns=["Longitude", "Latitude"]).columns
    cols = 3
    rows = int(np.ceil(len(features) / cols))
    _fig, _axes = plt.subplots(rows, cols, figsize=(16, rows * 4))
    _axes = _axes.flatten()
    for i, col in enumerate(features):
        sns.histplot(
            df_housing[col],
            bins=40,
            kde=True,
            ax=_axes[i],
            color="steelblue"
        )
        _axes[i].set_title(col, fontsize=11)
        _axes[i].grid(alpha=0.2)
    for j in range(i + 1, len(_axes)):
        _axes[j].set_visible(False)
    _fig.suptitle("Feature Distributions", fontsize=18)
    plt.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md(r"""
    - `MedInc` მონაცემი არის ათასობით დოლარში / tens of thousands USD.
    - `MedHouseVal` არის capped (`x > 500000 → 500000`)
        * ზოგიერთ რაიონში რეალური ფასი შეიძლება უფრო მაღალი იყოს
        * მოდელმა შეიძლება ისწავლოს: `ფასი არ აჭარბებს 500000`
    - მახასიათებლებს განსხვავებული scale აქვთ
    - ბევრი მახასიათებელს skewed distribution აქვს
    """)
    return


@app.cell
def _(df, plt, sns):
    corr = df.drop(["Latitude", "Longitude", "OceanProximity"], axis=1).corr(numeric_only=True)

    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(df_housing):
    df = df_housing[df_housing["MedHouseVal"] < 500000]
    return (df,)


@app.cell
def _(df, plt):
    _fig, _ax = plt.subplots(figsize=(8, 6))
    _ax.scatter(
        df["MedInc"],
        df["MedHouseVal"],
        alpha=0.25,
        color="steelblue",
        edgecolors="none"
    )
    _ax.set_title("Median Income vs Median House Value", fontsize=14)
    _ax.set_xlabel("Median Income")
    _ax.set_ylabel("Median House Value")
    _ax.grid(True, linestyle="--", alpha=0.3)
    _fig
    return


@app.cell
def _(mo):
    mo.md(r"""
    საწყისი ანალიზიდან ჩანს, რომ:

    - გეოგრაფიული მდებარეობა მნიშვნელოვან როლს თამაშობს. სანაპიროსთან ახლოს მდებარე რეგიონებში სახლების ფასები მნიშვნელოვნად მაღალია.
    - `MedHouseVal` დამოკიდებულია `MedInc` მახასიათებელზე, რაც უფრო მაღალია რაიონის საშუალო შემოსავალი, მით უფრო მაღალია სახლების საშუალო ღირებულება.

    -------------------------------------------------------
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## **5. Feature Engineering**

    ამ ეტაპზე შევქმნით შემდეგ ინფორმაციულ მახასიათებლებს:

    - `RoomsPerHousehold` - საშუალოდ რამდენი ოთახი მოდის ერთ ოჯახზე
    - `BedrmsPerRoom` - საძინებლების წილს მთლიან ოთახების რაოდენობასთან შედარებით
    - `PopPerHousehold` - საშუალოდ რამდენი ადამიანი ცხოვრობს ერთ ოჯახში
    """)
    return


@app.cell
def _(df):
    df["RoomsPerHousehold"] = df["TotalRooms"] / df["Households"]
    df["BedrmsPerRoom"] = df["TotalBedrms"] / df["TotalRooms"]
    df["PopPerHousehold"] = df["Population"] / df["Households"]

    df.head()
    return


@app.cell
def _(df):
    corr_matrix = df.drop("OceanProximity", axis=1).corr()
    corr_matrix["MedHouseVal"].sort_values(ascending=False)[1:]
    return


@app.cell
def _(mo):
    mo.md(r"""
    ------------------------------------------------
    ## **6. მახასიათებლებისა და სამიზნე ცვლადის გამოყოფა**

    ახლა მონაცემები ორ ნაწილად უნდა გავყოთ:

    - `X` input მახასიათებლები (Features)
    - `y` - სამიზნე ცვლადი (Target - `MedHouseVal`)
    """)
    return


@app.cell
def _(df):
    X = df.drop(columns=["MedHouseVal"])
    y = df["MedHouseVal"]
    return X, y


@app.cell
def _(mo):
    mo.md(r"""
    ------------------------------------------------
    ## **7. Train-Test გაყოფა**

    მონაცემთა ნაწილი გამოვიყენოთ მოდელის გასაწვრთნელად (Train Set),
    ხოლო ნაწილი - მის შესაფასებლად (Test Set).
    """)
    return


@app.cell
def _(X, train_test_split, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_test, X_train, y_test, y_train


@app.cell
def _(X_train):
    categorical_features = ["OceanProximity"]
    numeric_features = [col for col in X_train.columns if col not in categorical_features]
    return categorical_features, numeric_features


@app.cell
def _(mo):
    mo.md(r"""
    ------------------------------------------------
    ## **8. Preprocessing Pipeline**

    preprocessing ეტაპზე საჭიროა:

    * რიცხვითი ცვლადებისთვის
        - missing values-ის შევსება median-ით
        - feature scaling (`StandardScaler`)

    * კატეგორიული ცვლადებისთვის
        - missing values-ის შევსება ყველაზე ხშირი მნიშვნელობით
        - კატეგორიების გარდაქმნა რიცხვით ფორმატში (`OneHotEncoder`)
    """)
    return


@app.cell
def _(
    ColumnTransformer,
    OneHotEncoder,
    Pipeline,
    SimpleImputer,
    StandardScaler,
    categorical_features,
    numeric_features,
):
    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )
    return (preprocessor,)


@app.cell
def _(mo):
    mo.md(r"""
    ------------------------------------------------
    ## **9. მოდელის არჩევა და გაწვრთნა**
    """)
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
            "SVR"
        ],
        value="LinearRegression",
    )

    # Show UI in the notebook
    mo.vstack([mo.md("###Choose regression model"), model_choice])
    return (model_choice,)


@app.cell
def _(
    DecisionTreeRegressor,
    GradientBoostingRegressor,
    KNeighborsRegressor,
    LinearRegression,
    RandomForestRegressor,
    SVR,
    XGBRegressor,
    model_choice,
):
    # Choose model
    model_map = {
        "LinearRegression": LinearRegression(),

        "DecisionTreeRegressor": DecisionTreeRegressor(
            max_depth=8,
            min_samples_leaf=10,
            random_state=42
        ),

        "RandomForestRegressor": RandomForestRegressor(
            n_estimators=300,
            max_depth=12,
            min_samples_leaf=3,
            max_features="sqrt",
            random_state=42,
            n_jobs=-1
        ),

        "GradientBoostingRegressor": GradientBoostingRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=3,
            subsample=0.8,
            random_state=42
        ),

        "XGBRegressor": XGBRegressor(
            n_estimators=500,
            learning_rate=0.05,
            max_depth=4,
            subsample=0.8,
            colsample_bytree=0.8,
            objective="reg:squarederror",
            random_state=42,
            n_jobs=-1
        ),

        "KNeighborsRegressor": KNeighborsRegressor(
            n_neighbors=10,
            weights="distance",
            metric="minkowski"
        ),

        "SVR": SVR(kernel="rbf", C=100, gamma=0.1)
    }

    chosen_model = model_map[model_choice.value]
    return (chosen_model,)


@app.cell
def _(Pipeline, chosen_model, preprocessor):
    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", chosen_model),
        ]
    )
    return (model,)


@app.cell
def _(X_train, model, y_train):
    model.fit(X_train, y_train)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ------------------------------------------------
    ## **10. მოდელის შეფასება**

    მოდელის შესაფასებლად გამოვიყენებთ შემდეგ მეტრიკებს:

    - **MAE** - mean absolute error
    - **RMSE** - root mean squared error
    - **R²** - ახსნილი ვარიაციის წილი
    """)
    return


@app.cell
def _(
    X_test,
    mean_absolute_error,
    mean_squared_error,
    model,
    np,
    pd,
    r2_score,
    y_test,
    y_train,
):
    y_pred = model.predict(X_test)
    y_pred = np.clip(y_pred, y_train.min(), None)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    results_df = pd.DataFrame(
        {
            "Metric": ["MAE", "RMSE", "R²"],
            "Value": [mae, rmse, r2],
        }
    )
    results_df.round(2)
    return (y_pred,)


@app.cell
def _(plt, y_pred, y_test):
    _fig, _ax = plt.subplots(figsize=(8, 6))

    _ax.scatter(
        y_test,
        y_pred,
        alpha=0.25,
        color="steelblue",
        edgecolors="none"
    )

    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())

    _ax.plot(
        [min_val, max_val],
        [min_val, max_val],
        linestyle="--",
        color="red",
        linewidth=2,
        label="Perfect prediction"
    )

    _ax.set_xlabel("Actual Values")
    _ax.set_ylabel("Predicted Values")
    _ax.set_title("Actual vs Predicted House Values")

    _ax.set_aspect("equal", adjustable="box")

    _ax.grid(True, linestyle="--", alpha=0.3)
    _ax.legend()

    _fig
    return


@app.cell
def _(X_test, y_pred, y_test):
    example_idx = X_test.index[0]

    example_features = X_test.loc[[example_idx]].copy()
    example_features["ActualValue"] = y_test.loc[example_idx]
    example_features["PredictedValue"] = y_pred[0]

    example_features
    return


@app.cell
def _(mo):
    mo.md(r"""
    ------------------------------------------------
    ## **11. მოდელის Explainability**
    """)
    return


@app.cell
def _(model, model_choice, np, numeric_features, pd):
    regressor = model.named_steps["regressor"]

    cat_encoder = (
        model
        .named_steps["preprocessor"]
        .named_transformers_["cat"]
        .named_steps["onehot"]
    )

    cat_feature_names = cat_encoder.get_feature_names_out(["OceanProximity"])
    feature_names = list(numeric_features) + list(cat_feature_names)


    if hasattr(regressor, "coef_"):
        importance_df = pd.DataFrame(
            {
                "Feature": feature_names,
                "Importance": np.abs(regressor.coef_),
            }
        )

        importance_df = (
            importance_df
            .sort_values("Importance", ascending=False)
            .reset_index(drop=True)
            .head(5)
        )

        print("Top 5 coefficients:")
        print(importance_df)


    elif hasattr(regressor, "feature_importances_"):
        importance_df = pd.DataFrame(
            {
                "Feature": feature_names,
                "Importance": regressor.feature_importances_,
            }
        )

        importance_df = (
            importance_df
            .sort_values("Importance", ascending=False)
            .reset_index(drop=True)
            .head(5)
        )

        print("Top 5 feature importances:")
        print(importance_df)

    else:
        print(f"{model_choice.value} does not provide coefficients or feature_importances_.")
    return feature_names, importance_df


@app.cell
def _(importance_df, plt, sns):
    _fig, _ax = plt.subplots(figsize=(8, 4))
    sns.barplot(
        data=importance_df,
        x="Importance",
        y="Feature",
        ax=_ax,
        color="steelblue",
        width=0.5
    )
    _ax.set_xlabel("Coefficient Magnitude")
    _ax.set_ylabel("Feature")
    _ax.set_title("Top 5 Most Influential Features", fontsize=14)
    _ax.grid(True, linestyle="--", alpha=0.3)
    _fig
    return


@app.cell
def _(X_test, X_train, feature_names, model, model_choice):
    def _make_shap_plot(model, X_train, X_test, feature_names, model_choice):
        import shap
        import matplotlib.pyplot as plt
        from scipy import sparse

        _regressor = model.named_steps["regressor"]

        _X_train_transformed = model.named_steps["preprocessor"].transform(X_train)
        _X_test_transformed = model.named_steps["preprocessor"].transform(X_test)

        if sparse.issparse(_X_train_transformed):
            _X_train_transformed = _X_train_transformed.toarray()

        if sparse.issparse(_X_test_transformed):
            _X_test_transformed = _X_test_transformed.toarray()

        plt.figure(figsize=(10, 6))

        if hasattr(_regressor, "coef_"):
            _explainer = shap.LinearExplainer(
                _regressor,
                _X_train_transformed
            )

            _shap_values = _explainer(_X_test_transformed)

            shap.summary_plot(
                _shap_values.values,
                _X_test_transformed,
                feature_names=feature_names,
                show=False
            )

        elif hasattr(_regressor, "feature_importances_"):
            _explainer = shap.TreeExplainer(_regressor)

            _shap_values = _explainer(_X_test_transformed)

            shap.summary_plot(
                _shap_values.values,
                _X_test_transformed,
                feature_names=feature_names,
                show=False
            )

        else:
            print(
                f"SHAP is slow for {model_choice.value}. "
                "Using KernelExplainer with a small sample."
            )

            _background = shap.sample(_X_train_transformed, 100, random_state=42)
            _X_test_sample = _X_test_transformed[:200]

            _explainer = shap.KernelExplainer(
                _regressor.predict,
                _background
            )

            _shap_values = _explainer.shap_values(_X_test_sample)

            shap.summary_plot(
                _shap_values,
                _X_test_sample,
                feature_names=feature_names,
                show=False
            )

        plt.title(f"SHAP Summary Plot - {model_choice.value}", fontsize=14)

        return plt.gcf()


    shap_fig = _make_shap_plot(
        model=model,
        X_train=X_train,
        X_test=X_test,
        feature_names=feature_names,
        model_choice=model_choice
    )

    shap_fig
    return


@app.cell
def _(mo):
    mo.md(r"""
    ------------------------------------------------
    ## **12. რა შეიძლება გავაუმჯობესოთ?**

    - cross-validation
    - hyperparameter tuning
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
