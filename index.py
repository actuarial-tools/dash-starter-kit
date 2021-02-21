from app import app
import dash_html_components as html
import dash_bootstrap_components as dbc
import router
from view import header_bar_view

layout = html.Div([
    header_bar_view.layout,
    router.layout,
])

app.layout = html.Div(layout)

if __name__ == '__main__':
    PORT = 5000
    app.run_server(
        port=PORT,
        host='0.0.0.0',
        debug=True,
    )
