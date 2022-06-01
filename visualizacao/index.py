import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# import matplotlib.pyplot as plt
# from pyparsing import Char
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from line_chart import LineChart
from pie_chart import PieChart
from tree_chart import TreeChart

data = pd.read_csv("./dataset/netflix_titles.csv", index_col = "show_id", parse_dates = True)
data.head(3)

data.info()

data.isnull().sum()

data.nunique()

data = data.dropna( how='any',subset=['cast', 'director'])

data['country'].fillna('Missing',inplace=True)
data['date_added'].fillna('Missing',inplace=True)
data['rating'].fillna('Missing',inplace=True)
data.isnull().sum().sum()

data["date_added"] = pd.to_datetime(data['date_added'])
data['year_added'] = data['date_added'].dt.year
data['month_added'] = data['date_added'].dt.month

data = data.rename(columns={"listed_in":"genre"})
data['genre'] = data['genre'].apply(lambda x: x.split(",")[0])
data.head()

data.describe(include='O')

pieChart = PieChart(data, px)
lineChart = LineChart(data, go)
treeChart = TreeChart(data, pd, px)

pieChart.showChart()
lineChart.showChart()
treeChart.showChart() 