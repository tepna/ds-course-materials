import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    from ucimlrepo import fetch_ucirepo 
    return fetch_ucirepo, mo, pd, plt


@app.cell
def _(mo):
    mo.md(r"""
    ###Online Retail Data
    """)
    return


@app.cell
def _(fetch_ucirepo):
    # fetch dataset 
    online_retail = fetch_ucirepo(id=352) 
    df_retail = online_retail.data.original
    df_retail
    return (df_retail,)


@app.cell
def _():
    # df_retail.isna().sum()
    return


@app.cell
def _(df_retail, pd):
    df_retail["Revenue"] = df_retail["Quantity"] * df_retail["UnitPrice"]

    # Add some time features
    df_retail["InvoiceDate"] = pd.to_datetime(df_retail["InvoiceDate"])
    df_retail["Date"] = df_retail["InvoiceDate"].dt.date
    df_retail["Hour"] = df_retail["InvoiceDate"].dt.hour
    df_retail["Month"] = df_retail["InvoiceDate"].dt.to_period("M").dt.to_timestamp()
    df_retail["Week"] = df_retail["InvoiceDate"].dt.to_period("W").dt.start_time
    df_retail["Weekday"] = df_retail["InvoiceDate"].dt.day_name()
    return


@app.cell
def _(mo):
    agg_dropdown = mo.ui.dropdown(
            options={
                "Daily": "D",
                "Weekly": "W",
                "Monthly": "M",
            },
            value="Daily",
            label="Aggregation level",
        )

    ma_window_slider = mo.ui.slider(
        start=1,
        stop=60,
        value=7,
        step=1,
        label="Moving average window (in periods)",
    )

    mo.vstack(
        [
            mo.md("### Revenue over time"),
            agg_dropdown,
            ma_window_slider,
        ]
    )
    return agg_dropdown, ma_window_slider


@app.cell
def _(agg_dropdown, df_retail, ma_window_slider, plt):
    rule = agg_dropdown.value  # "D", "W", "M"

    ts = (
        df_retail.set_index("InvoiceDate")["Revenue"]
        .resample(rule)
        .sum()
        .to_frame(name="Revenue")
    )

    # Moving average
    window = ma_window_slider.value
    ts["MA"] = ts["Revenue"].rolling(window=window, min_periods=1).mean()

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(ts.index, ts["Revenue"], label="Revenue")
    ax.plot(ts.index, ts["MA"], label=f"Moving average ({window})")

    ax.set_title(f"Revenue over time ({agg_dropdown.value})")
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue")
    ax.legend()
    fig.tight_layout()

    fig
    return


@app.cell
def _(df_retail, mo, plt):
    # Monthly revenue (for Christmas peak)
    monthly = (
        df_retail.set_index("InvoiceDate")["Revenue"]
        .resample("ME")
        .sum()
    )

    # Weekday revenue
    weekday = (
        df_retail.groupby("Weekday", sort=False)["Revenue"]
        .sum()
        .reindex(
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        )
    )

    fig1, ax1 = plt.subplots(figsize=(7, 4))
    ax1.bar(monthly.index, monthly.values)
    ax1.set_title("Monthly revenue")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Revenue")
    fig1.autofmt_xdate()

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.bar(weekday.index, weekday.values)
    ax2.set_title("Revenue by weekday")
    ax2.set_xlabel("Weekday")
    ax2.set_ylabel("Revenue")
    ax2.tick_params(axis="x", labelrotation=45)
    fig2.tight_layout()

    mo.vstack([mo.md("### Seasonality: monthly & weekday patterns"), 
               mo.hstack([fig1, fig2])])
    return


@app.cell
def _(mo):
    metric_dropdown = mo.ui.dropdown(
        options={
            "Revenue (sum)": "Revenue",
            "Quantity (sum)": "Quantity",
        },
        value="Revenue (sum)",
        label="Metric",
    )

    top_n_slider = mo.ui.slider(
        start=5,
        stop=50,
        value=10,
        step=1,
        label="Top-N products",
    )

    mo.vstack(
        [
            mo.md("### Top products"),
            metric_dropdown,
            top_n_slider,
        ]
    )
    return metric_dropdown, top_n_slider


@app.cell
def _(df_retail, metric_dropdown, plt, top_n_slider):
    metric = metric_dropdown.value  # "Revenue" or "Quantity"
    top_n = top_n_slider.value

    grouped = (
        df_retail.groupby("Description", dropna=False)[metric]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )

    _fig, _ax = plt.subplots(figsize=(8, max(4, 0.3 * top_n)))
    _ax.barh(grouped.index[::-1], grouped.values[::-1])
    _ax.set_title(f"Top {top_n} products by {metric}")
    _ax.set_xlabel(metric)
    _ax.set_ylabel("Product")
    _fig.tight_layout()

    _fig
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
