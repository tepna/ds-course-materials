import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.pipeline import Pipeline
    from sklearn.model_selection import train_test_split
    from imblearn.over_sampling import RandomOverSampler, SMOTE
    from imblearn.under_sampling import RandomUnderSampler
    from imblearn import FunctionSampler
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import confusion_matrix
    return (
        DecisionTreeClassifier,
        FunctionSampler,
        RandomOverSampler,
        RandomUnderSampler,
        SMOTE,
        confusion_matrix,
        pd,
        plt,
        sns,
        train_test_split,
    )


@app.cell
def _(mo, pd):
    df_loan = pd.read_csv("datasets/lending_club/loan_data.csv")
    df_loan = pd.get_dummies(df_loan)
    mo.vstack([mo.md("###Loan Dataset"), mo.ui.table(df_loan, selection=None)])
    return (df_loan,)


@app.cell
def _(df_loan, train_test_split):
    # Feaqtures, target
    X, y = df_loan.drop(columns="not.fully.paid"), df_loan["not.fully.paid"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_test, X_train, y_test, y_train


@app.cell
def _(mo):
    # UI widgets
    sampler_choice = mo.ui.dropdown(
        options=[
            "RandomUnderSampler",
            "RandomOverSampler",
            "SMOTE",
        ],
        value=None,
    )

    # Show UI in the notebook
    mo.vstack([mo.md("---- \n###Choose Sampler"), sampler_choice])
    return (sampler_choice,)


@app.cell
def _(
    FunctionSampler,
    RandomOverSampler,
    RandomUnderSampler,
    SMOTE,
    sampler_choice,
):
    # Choose sampler
    sampler_map = {
    None: FunctionSampler(func=lambda X, y: (X, y)),
    "RandomUnderSampler": RandomUnderSampler(random_state=42),
    "RandomOverSampler": RandomOverSampler(random_state=42),
    "SMOTE": SMOTE(random_state=42),
    }

    sampler = sampler_map[sampler_choice.value]
    return (sampler,)


@app.cell
def _(X_train, sampler, y_train):
    # Sampling
    X_sampled, y_sampled = sampler.fit_resample(X_train, y_train)
    return X_sampled, y_sampled


@app.cell
def _(DecisionTreeClassifier, X_sampled, X_test, y_sampled):
    # მოდელის შექმნა და გაწვრთნა
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_sampled, y_sampled)

    # პროგნოზირება
    y_pred = model.predict(X_test)
    return model, y_pred


@app.cell
def _(confusion_matrix, mo, model, plt, sns, y_pred, y_sampled, y_test):
    fig1, ax1 = plt.subplots(figsize=(6, 5))
    y_sampled.value_counts().plot(kind="bar", ax=ax1, color=["C0", "C1"], alpha=0.5)
    ax1.set_title("Class distribution in training data")
    ax1.set_xlabel("Class")
    ax1.set_ylabel("Count")
    ax1.tick_params(axis="x", labelrotation=0)

    conf_matrix = confusion_matrix(y_test, y_pred)

    fig2, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=model.classes_, yticklabels=model.classes_)
    ax.set_title("Confusion Matrix")
    ax.set_ylabel("True label")
    ax.set_xlabel("Predicted label")

    mo.hstack([fig1, fig2])
    return


if __name__ == "__main__":
    app.run()
