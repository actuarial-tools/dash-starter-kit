import dash_bootstrap_components as dbc
import dash_html_components as html
from functools import partial


def _unknown_page(title, text):
    return dbc.Jumbotron(
        [
            html.H1(title, className="text-danger"),
            html.Hr(),
            html.P(text),
        ]
    )

page_help = _unknown_page('Help','Help Page')
page_welcome = _unknown_page('Dash Starter Kit','Welcome to Dash Starter Kit')
page_404 = partial(_unknown_page, '404: Not found')
page_no_results = partial(_unknown_page, 'No results available')
