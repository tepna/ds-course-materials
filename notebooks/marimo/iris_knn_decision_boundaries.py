import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from sklearn.datasets import load_iris
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    return (
        KNeighborsClassifier,
        Pipeline,
        StandardScaler,
        load_iris,
        mo,
        np,
        plt,
    )


@app.cell
def _(load_iris, mo):
    # Load iris dataset into a DataFrame
    iris = load_iris(as_frame=True)
    df_iris = iris.frame.copy()
    mo.vstack(
        [
            mo.md("##Iris Dataset"),
            mo.ui.table(df_iris, selection=None),
        ]
    )
    return df_iris, iris


@app.cell
def _(df_iris, mo):
    feature_cols = df_iris.columns[:-1]  # all except "target"
    target_col = "target"

    # Choose 2 features for 2D decision boundary
    feature_x = mo.ui.dropdown(
        options=list(feature_cols),
        value="petal length (cm)",
        label="Feature on X-axis",
    )
    feature_y = mo.ui.dropdown(
        options=list(feature_cols),
        value="petal width (cm)",
        label="Feature on Y-axis",
    )

    # Choose k
    k_slider = mo.ui.slider(
        start=1,
        stop=25,
        value=5,
        step=1,
        label="Number of neighbors (k)",
    )

    mo.vstack(
        [
            mo.md("---- \n## k-NN Decision Boundary on Iris Dataset"),
            mo.hstack([feature_x, feature_y, k_slider]),
        ]
    )
    return feature_x, feature_y, k_slider, target_col


@app.cell
def _(
    KNeighborsClassifier,
    Pipeline,
    StandardScaler,
    df_iris,
    feature_x,
    feature_y,
    iris,
    k_slider,
    mo,
    np,
    plt,
    target_col,
):
    # Ensure two different features
    if feature_x.value == feature_y.value:
        mo.md("⚠️ Please choose two *different* features.")
        raise mo.StopExecution()

    X = df_iris[[feature_x.value, feature_y.value]].values
    y = df_iris[target_col].values
    class_names = iris.target_names

    # k-NN with scaling
    k = int(k_slider.value)
    model = Pipeline(
        steps=[
            ("scale", StandardScaler()),
            ("knn", KNeighborsClassifier(n_neighbors=k)),
        ]
    )
    model.fit(X, y)

    # Create a meshgrid for decision boundary
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 300),
        np.linspace(y_min, y_max, 300),
    )

    grid_points = np.c_[xx.ravel(), yy.ravel()]
    Z = model.predict(grid_points)
    Z = Z.reshape(xx.shape)

    # Plot decision boundary + points
    fig, ax = plt.subplots(figsize=(6, 5))

    # Background (decision regions)
    ax.contourf(xx, yy, Z, alpha=0.3)

    # Training points
    scatter = ax.scatter(
        X[:, 0],
        X[:, 1],
        c=y,
        edgecolor="k",
        alpha=0.8,
    )

    # Legend with class names
    handles, _ = scatter.legend_elements()
    ax.legend(handles, class_names, title="Classes")

    ax.set_xlabel(feature_x.value)
    ax.set_ylabel(feature_y.value)
    ax.set_title(f"k-NN Decision Boundary (k = {k})")

    fig
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
