import dash
import dash_bootstrap_components as dbc
from datasource import http as repo

# Font Awesome CSS.
FA = "https://use.fontawesome.com/releases/v5.8.1/css/all.css"

# Global variable
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
ROUTER_ID = 'url'
CONTENT_ID = 'page_content'
ROUTER_STORE = 'router_store'
SELECTED_PERSON = 'selected_person'
PEOPLE_SELECTED_BUTTON = 'selected_person_btn'
USER_ID='user_id'

datasource = repo
app = dash.Dash(__name__, external_stylesheets=[
                dbc.themes.BOOTSTRAP, FA], update_title=None)
app.config.suppress_callback_exceptions = True
app.title = 'Dash Starter Kit'
