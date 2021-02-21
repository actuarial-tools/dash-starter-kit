from os import link
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash_core_components.Store import Store
import dash_html_components as html
from dash.dependencies import ALL, Input, Output, State
from dash.exceptions import PreventUpdate
from app import app, datasource, SELECTED_PERSON, PEOPLE_SELECTED_BUTTON
import dash

_PEOPLE_DETAIL_MODAL = 'people_modal'
_PEOPLE_DETAIL_FORM = 'people_form'
_CLOSE_MODAL_BTN = 'close_btn'

def get_form_field(item: dict):
    fields = list(item.keys())
    return [
        dbc.FormGroup([
            dbc.Label('{}'.format(i.upper())),
            dbc.Input(type="text", value=item.get(i), disabled=True)
        ])
        for i in fields[:7]
    ]


layout = html.Div([
    dcc.Store(id='form_data'),
    dbc.Modal([
        dbc.ModalHeader(id='title'),
        dbc.ModalBody([
            dbc.Form(id=_PEOPLE_DETAIL_FORM)
        ], id="new-analysis-modal-body"),
        dbc.ModalFooter(
            html.Div([
                dbc.Button(
                    html.Span([html.I(className="fas fa-times"), "Close"]),
                    outline=True, color="warning", id=_CLOSE_MODAL_BTN
                )
            ])
        )
    ],
        id=_PEOPLE_DETAIL_MODAL,
        is_open=False,
    )]
)


@app.callback(
    Output(_PEOPLE_DETAIL_MODAL, 'is_open'),
    Output('title', 'children'),
    Output(_PEOPLE_DETAIL_FORM, 'children'),
    [
        Input(PEOPLE_SELECTED_BUTTON, 'n_clicks'),
        Input(_CLOSE_MODAL_BTN, 'n_clicks')
    ],
    [
        State(SELECTED_PERSON, 'data'),
    ])
def on_modal_open(add_btn, close_btn, selected_person):
    ctx = dash.callback_context
    triggered = ctx.triggered[0].get("prop_id").split(".")[0]

    if triggered:
        if triggered == PEOPLE_SELECTED_BUTTON:
            return [True, selected_person.get('name'), get_form_field(selected_person)]

        if triggered == _CLOSE_MODAL_BTN:
            return [False, '', []]

    raise PreventUpdate
