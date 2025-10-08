from nicegui import ui
import plotly.express as px
import numpy as np
import pandas as pd


def update_figure(plot: ui.plotly, phase=0):
    X = np.linspace(0, 3, 100) + phase
    df_sin = pd.DataFrame({"x": X, "y": np.sin(X), "function": "sin"})
    df_cos = pd.DataFrame({"x": X, "y": np.cos(X), "function": "cos"})
    df = pd.concat([df_sin, df_cos])
    plot.update_figure(px.line(df, x="x", y="y", color="function"))


def app():
    ui.colors(
        base_100="oklch(100% 0 0)",
        base_200="oklch(93% 0 0)",
        base_300="oklch(86% 0 0)",
    )

    ui.query(".nicegui-content").style("padding: 0; overflow: hidden;")

    with ui.element("div").classes("flex flex-col w-full h-screen"):
        # Header
        with ui.element("header").classes("min-h-[4%] bg-base-300 p-4"):
            ui.label("The sinusoid exercice").classes("text-xl")

        # Main
        with ui.element("div").classes("flex grow"):
            with ui.element("div").classes("w-[30%] max-w-xs bg-base-200 p-4"):
                ui.label("Options").classes("text-xl")
                ui.button("Change phase").on_click(lambda: update_figure(plot, phase=1))

            # Content
            with ui.element("div").classes("grow bg-base-100 p-4"):
                X = np.linspace(0, 3, 100)
                df_sin = pd.DataFrame({"x": X, "y": np.sin(X), "function": "sin"})
                df_cos = pd.DataFrame({"x": X, "y": np.cos(X), "function": "cos"})
                df = pd.concat([df_sin, df_cos])
                fig = px.line(df, x="x", y="y", color="function")
                plot = ui.plotly(fig).classes("w-full h-full")

        # Footer
        with ui.element("footer").classes("min-h-[4%] bg-base-300 p-4"):
            with ui.row().classes("items-center text-xl"):
                ui.label("Parameter info")


app()
ui.run(title="Styles")
