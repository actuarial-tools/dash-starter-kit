import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app, PLOTLY_LOGO


# search_bar = dbc.Row(
#     [
#         dbc.Col(dbc.Input(type="search", placeholder="Search")),
#         dbc.Col(
#             dbc.Button("Search", color="primary", className="ml-2"),
#             width="auto",
#         ),
#     ],
#     no_gutters=True,
#     className="ml-auto flex-nowrap mt-3 mt-md-0",
#     align="center",
# )

# layout = dbc.Navbar(
#     [
#         html.A(
#             # Use row and col to control vertical alignment of logo / brand
#             dbc.Row(
#                 [
#                     dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
#                     dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),
#                 ],
#                 align="center",
#                 no_gutters=True,
#             ),
#             href="https://plot.ly",
#         ),
#         dbc.NavbarToggler(id="navbar-toggler"),
#         dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
#     ],
#     color="dark",
#     dark=True,
# )


layout = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Help", href="/help")),
        dbc.NavItem(dbc.NavLink("404", href="/404")),
    ],
    brand="Dash Starter Kit",
    brand_href="/",
    color="primary",
    dark=True,
)