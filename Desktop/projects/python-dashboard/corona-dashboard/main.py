import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from data import countries_df, total_df, dropdown_options, make_global_df, make_country_df
from builders import make_table
from dash.dependencies import Input, Output

print(countries_df)

stylesheets = [
    "https://unpkg.com/reset-css/reset.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap"
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

server = app.server

bubble_map = px.scatter_geo(countries_df, 
                            template="plotly_dark",
                            size="Confirmed",
                            size_max=40,
                            projection="natural earth",
                            title="Confirmed By Country",
                            color_continuous_scale=px.colors.sequential.Oryel,
                            hover_name="Country_Region",  
                            color="Confirmed",
                            locations="Country_Region", 
                            locationmode="country names",
                            hover_data={
                                    "Confirmed":":,2f", 
                                    "Deaths":":,2f", 
                                    "Recovered":":,2f", 
                                    "Country_Region":False
                        })
bubble_map.update_layout(margin=dict(l=0, r=0, t=50, b=0))
#bubble_map.show()

bars_graph = px.bar(total_df, 
    x="condition", 
    y="count", 
    #color=["Confirmed","Deaths","Recovered"],
    hover_data={'count':":,"},
    template="plotly_dark", 
    title="Total Global Cases",
    labels={
        "condtion":"Condition",
        "count":"Count",
     #   "color":"Condition"
    })
bars_graph.update_traces(marker_color=["#e74c3c","#8e44ad","#27ae60"])


app.layout = html.Div(
    style={
        "textAlign":"center", 
        "minHeight":"100vh", 
        "backgroundColor":"#111111",
        "color":"white",
        "fontFamily":"Open Sans, sans-serif",
    },
    children = [
        html.Header(
            style={"textAlign":"center", "paddingTop": "50px", "marginBottom": 100},
            children=[html.H1("Corona Dashboard", style={"fontSize":50})]
        ),
        html.Div(
            style ={"display":"grid","gap":50,"gridTemplateColumns":"repeat(4,1fr)"},
            children=[html.Div(
                        style={"grid-column":"span 3"},
                        children=[dcc.Graph(figure=bubble_map)]),
                      html.Div(children=[make_table(countries_df)]),
            ]
        ),
        html.Div(       
            style={"display":"grid","gap":50,"gridTemplateColumns": "repeat(4, 1fr)"},
            children=[
                html.Div(children=[dcc.Graph(figure=bars_graph)]),
                html.Div(
                    style={"grid-column":"span 3"},
                    children=[
                        dcc.Dropdown(
                            style={"width":320, "margin":"0 auto", "color":"#111111",},
                            placeholder="Select a Country",id="country",
                            options=[
                                {'label':country, 'value':country} 
                                for country in dropdown_options
                            ]),
                            dcc.Graph(id="country_graph")
                        ]
                    )
                ]
            )
        ]
)


#map_figure = px.scatter_geo(countries_df)
#map_figure.show()


@app.callback(Output("country_graph","figure"),[Input("country","value")])
def update_hello(value):
    if value:
        df = make_country_df(value)
    else:
        df = make_global_df()
    fig = px.line(
            df,
            x="date",y=["confirmed","deaths","recovered"],
            template = "plotly_dark",
             labels={
                 "value" : "Cases",
                 "variable" : "Condition",
                 "value" : "Date",
             },
             hover_data = {
                 "value":  ":,",
                 "variable": False,
                 "date": False,
             }
        )
    fig.update_xaxes(rangeslider_visible=True)
    fig["data"][0]["line"]["color"] = "pink"
    return fig

## for only development
#if __name__ == '__main__':
#    app.run_server(debug=True)