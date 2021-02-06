import plotly.express as px
from data import countries_df
print(type(countries_df))
print(countries_df.head())
map_figure = px.scatter_geo(countries_df, 
                            template="plotly_dark",
                            size="Confirmed",
                            size_max=40,
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
map_figure.show()