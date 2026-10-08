import numpy as np
import pandas as pd
import plotly.express as px
from nicegui import ui

global_state = {"phase": 0}


def update_figure(plot: ui.plotly):
    X = np.linspace(0, 3, 100) + global_state["phase"]
    df_sin = pd.DataFrame({"x": X, "y": np.sin(X), "function": "sin"})
    df_cos = pd.DataFrame({"x": X, "y": np.cos(X), "function": "cos"})
    df = pd.concat([df_sin, df_cos])
    plot.update_figure(px.line(df, x="x", y="y", color="function"))


with ui.header().classes("row items-center") as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon="menu").props(
        "flat color=white"
    )
    ui.label("The sinusoid exercice").classes("text-xl")

with ui.footer().classes("text-xl") as footer:
    ui.label("Parameter info")
    ui.label().bind_text_from(
        global_state,
        "phase",
        backward=lambda text: f"Phase = {text:.2f}",
    )

with ui.left_drawer().classes("bg-blue-100") as left_drawer:
    ui.label("Options").classes("text-xl")

    def change_phase():
        global_state["phase"] = 1
        update_figure(plot)

    ui.button("Change phase").on_click(change_phase)

# Necessary query to make the plot full screen
ui.query(".nicegui-content").classes("absolute inset-0 p-0")

# Content
X = np.linspace(0, 3, 100)
df_sin = pd.DataFrame({"x": X, "y": np.sin(X), "function": "sin"})
df_cos = pd.DataFrame({"x": X, "y": np.cos(X), "function": "cos"})
df = pd.concat([df_sin, df_cos])
fig = px.line(df, x="x", y="y", color="function")
plot = ui.plotly(fig).classes("w-full h-full")

ui.run(title="The sinusoid exercice")
