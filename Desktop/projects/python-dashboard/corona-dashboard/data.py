import pandas as pd



conditions  = ["confirmed","deaths","recovered"]

#######################################################################
daily_df = pd.read_csv("data/daily_reports/01-02-2021.csv")
#print(type(daily_df))

total_df = daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index(name="count")
total_df = total_df.rename(columns={"index" : "condition"})
#print(type(total_df))


#######################################################################
countries_df = daily_df[["Country_Region","Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().reset_index()

print(countries_df)
#######################################################################
dropdown_options = countries_df.sort_values("Country_Region").reset_index()
dropdown_options = dropdown_options["Country_Region"]


def make_global_df():
    def make_df(condition):
        df = pd.read_csv(f"data/{condition}.csv")
        df = df.drop(["Province/State","Country/Region","Lat","Long"],axis=1).sum().reset_index(name=condition)
        #.sort_values(by="Confirmed", ascending=False).reset_index(name=condition)
        df = df.rename(columns={"index":"date"})
        return df
    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df


def make_country_df(country):
    def make_df(condition):
        df = pd.read_csv(f"data/{condition}.csv")
        df = df.loc[df["Country/Region"] == country]
        df = df.drop(["Province/State","Country/Region","Lat","Long"],axis=1).sum().reset_index(name=condition)
        df = df.rename(columns={"index":"date"})
        return df 
    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df


conditions  = ["confirmed","deaths","recovered"]


df = make_country_df("Korea, South")
global_df = make_global_df()
