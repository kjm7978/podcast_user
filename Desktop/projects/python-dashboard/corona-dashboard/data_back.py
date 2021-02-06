{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Confirmed</th>\n",
       "      <th>Deaths</th>\n",
       "      <th>Recovered</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Country_Region</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Afghanistan</th>\n",
       "      <td>55059</td>\n",
       "      <td>2404</td>\n",
       "      <td>47723</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Albania</th>\n",
       "      <td>78992</td>\n",
       "      <td>1393</td>\n",
       "      <td>47922</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Algeria</th>\n",
       "      <td>107578</td>\n",
       "      <td>2894</td>\n",
       "      <td>73530</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Andorra</th>\n",
       "      <td>9972</td>\n",
       "      <td>101</td>\n",
       "      <td>9206</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Angola</th>\n",
       "      <td>19829</td>\n",
       "      <td>466</td>\n",
       "      <td>18180</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Vietnam</th>\n",
       "      <td>1850</td>\n",
       "      <td>35</td>\n",
       "      <td>1460</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>West Bank and Gaza</th>\n",
       "      <td>159443</td>\n",
       "      <td>1840</td>\n",
       "      <td>149621</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Yemen</th>\n",
       "      <td>2122</td>\n",
       "      <td>615</td>\n",
       "      <td>1426</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Zambia</th>\n",
       "      <td>55042</td>\n",
       "      <td>780</td>\n",
       "      <td>49394</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Zimbabwe</th>\n",
       "      <td>33548</td>\n",
       "      <td>1234</td>\n",
       "      <td>26583</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>192 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                    Confirmed  Deaths  Recovered\n",
       "Country_Region                                  \n",
       "Afghanistan             55059    2404      47723\n",
       "Albania                 78992    1393      47922\n",
       "Algeria                107578    2894      73530\n",
       "Andorra                  9972     101       9206\n",
       "Angola                  19829     466      18180\n",
       "...                       ...     ...        ...\n",
       "Vietnam                  1850      35       1460\n",
       "West Bank and Gaza     159443    1840     149621\n",
       "Yemen                    2122     615       1426\n",
       "Zambia                  55042     780      49394\n",
       "Zimbabwe                33548    1234      26583\n",
       "\n",
       "[192 rows x 3 columns]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "#######################################################################\n",
    "daily_df = pd.read_csv(\"data/daily_reports/01-02-2021.csv\")\n",
    "#print(type(daily_df))\n",
    "\n",
    "total_df = daily_df[[\"Confirmed\", \"Deaths\", \"Recovered\"]].sum().reset_index(name=\"count\")\n",
    "total_df = total_df.rename(columns={\"index\" : \"condition\"})\n",
    "#print(type(total_df))\n",
    "\n",
    "\n",
    "#######################################################################\n",
    "countries_df = daily_df[[\"Country_Region\",\"Confirmed\", \"Deaths\", \"Recovered\"]]\n",
    "countries_df = countries_df.groupby(\"Country_Region\").sum()\n",
    "\n",
    "#######################################################################\n",
    "conditions  = [\"confirmed\",\"deaths\",\"recovered\"]\n",
    "\n",
    "\n",
    "\n",
    "        \n",
    "        \n",
    "countries_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        date  confirmed   deaths  recovered\n",
      "0    1/22/20        557       17         30\n",
      "1    1/23/20        655       18         32\n",
      "2    1/24/20        941       26         39\n",
      "3    1/25/20       1433       42         42\n",
      "4    1/26/20       2118       56         56\n",
      "..       ...        ...      ...        ...\n",
      "373  1/29/21  102069214  2206461   56408992\n",
      "374  1/30/21  102583825  2219984   56762214\n",
      "375  1/31/21  102965859  2227910   57049348\n",
      "376   2/1/21  103412987  2238128   57320703\n",
      "377   2/2/21  103869826  2253064   57671339\n",
      "\n",
      "[378 rows x 4 columns]\n"
     ]
    }
   ],
   "source": [
    "def make_global_df():\n",
    "    def make_df(condition):\n",
    "        df = pd.read_csv(f\"data/{condition}.csv\")\n",
    "        df = df.drop([\"Province/State\",\"Country/Region\",\"Lat\",\"Long\"],axis=1).sum().reset_index(name=condition)\n",
    "        df = df.rename(columns={\"index\":\"date\"})\n",
    "        return df\n",
    "    final_df = None\n",
    "    for condition in conditions:\n",
    "        condition_df = make_df(condition)\n",
    "        if final_df is None:\n",
    "            final_df = condtion_df\n",
    "        else:\n",
    "            final_df = final_df.merge(condition_df)\n",
    "    return final_df\n",
    "\n",
    "\n",
    "def make_country_df(country):\n",
    "    def make_df(condition):\n",
    "        df = pd.read_csv(f\"data/{condition}.csv\")\n",
    "        df = df.loc[df[\"Country/Region\"] == country]\n",
    "        df = df.drop([\"Province/State\",\"Country/Region\",\"Lat\",\"Long\"],axis=1).sum().reset_index(name=condition)\n",
    "        df = df.rename(columns={\"index\":\"date\"})\n",
    "        return df \n",
    "    final_df = None\n",
    "    for condition in conditions:\n",
    "        condition_df = make_df(condition)\n",
    "        if final_df is None:\n",
    "            final_df = condtion_df\n",
    "        else:\n",
    "            final_df = final_df.merge(condition_df)\n",
    "    return final_df\n",
    "\n",
    "\n",
    "conditions  = [\"confirmed\",\"deaths\",\"recovered\"]\n",
    "\n",
    "\n",
    "\n",
    "df = make_country_df(\"Iran\")\n",
    "global_df = make_global_df()\n",
    "print(global_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
