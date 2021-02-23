import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from flask import request
from app import app, ROUTER_STORE, USER_ID
from service.util import get_user_id
from view import unknown_view, people_list

_CONTEND_ID = 'page_content'
_ROUTER_ID = 'url'

@app.callback([
    Output(_CONTEND_ID, 'children'),
    Output(ROUTER_STORE, 'data'),
    Output(USER_ID, 'data')
],
    Input(_ROUTER_ID, "pathname")
)
def url_manager(url):
    user_id = get_user_id(request.cookies).upper()
    result = [[], None, user_id]
    path = url.split('/')

    #root of application
    if any([url == '/']):
        result[0] = people_list.layout()
        result[1] = {"url": url, "page": "main"}

    #explicit route
    if url == '/help':
        result[0] = unknown_view.page_help
        result[1] = {"url": url, "page": "help"}

    #level two routing test/id
    if len(path) == 3:
        result[1] = {"url": url, "page": path[1],
                     "uid": path[2]}
        if path[1] == 'route-1':
            result[0] = None

        if path[1] == 'route-2':
            result[0] = None

        if path[1] == 'route-3':
            result[0] = None

        if path[1] == 'route-4':
            result[0] = None

        if path[1] == 'route-5':
            result[0] = None

    #if no route match show 404 page
    return result if result[0] else [
        unknown_view.page_404(
            f'unable to locate the resource at the following url:{url}'),
        {},
        user_id
    ]


layout = html.Div([
    dcc.Store(id=ROUTER_STORE),
    dcc.Store(id=USER_ID),
    dcc.Location(id=_ROUTER_ID),
    html.Div(id=_CONTEND_ID)
])
