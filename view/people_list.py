import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash_table import DataTable
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import datasource, app, SELECTED_PERSON, PEOPLE_SELECTED_BUTTON
from view import people_detail


detail_btn = dbc.Button(
    html.Span([html.I(className="fas fa-edit"), " Detail"]),
    outline=True, size="sm", color="primary", disabled=True, id=PEOPLE_SELECTED_BUTTON
)


def _get_fields_and_data(data: dict):
    _data = data.get('results')
    fields = list(_data[0].keys())
    return (
        [{"id": i, "name": i.upper()} for i in fields[:5]],
        _data
    )


def create_table(data: dict):
    fields, _data = _get_fields_and_data(data)
    return DataTable(
        id='people_table',
        columns=fields,
        row_selectable="single",
        sort_action="native",
        sort_mode="multi",
        data=_data
    )


def layout():
    data = datasource.people.all()
    return dbc.Card(
        dbc.CardBody([
            html.H4("Starwars People"),
            detail_btn,
            html.Hr(),
            dcc.Store(id=SELECTED_PERSON),
            create_table(data),
            people_detail.layout
        ]),
        className="backdrop-cards"
    )


@app.callback(
    Output(PEOPLE_SELECTED_BUTTON, 'disabled'),
    Input(SELECTED_PERSON, 'data')
)
def toggle_navbar_collapse(selected):
    return False if selected else True


@app.callback(
    Output(SELECTED_PERSON, 'data'),
    Input('people_table', 'selected_rows'),
    State('people_table', 'data')
)
def on_select_analysis(selected_rows, rows):
    result = None
    if all([selected_rows, rows]):
        result = rows[selected_rows[0]]

    return result
