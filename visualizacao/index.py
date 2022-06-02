import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

from line_chart import LineChart
from pie_chart import PieChart
from tree_chart import TreeChart

class ChartBuilder:
    __data: None

    def __init__(self, dataSet):
        dataSet = dataSet
        dataSet.head(3)
        dataSet.info()
        dataSet.isnull().sum()
        dataSet.nunique()

        self.__data = dataSet

        self.organiseData()


    def organiseData(self):
        self.__data = self.__data.dropna( how='any',subset=['cast', 'director'])

        self.__data['country'].fillna('Missing',inplace=True)
        self.__data['date_added'].fillna('Missing',inplace=True)
        self.__data['rating'].fillna('Missing',inplace=True)
        self.__data.isnull().sum().sum()

        self.__data["date_added"] = pd.to_datetime(self.__data['date_added'])
        self.__data['year_added'] = self.__data['date_added'].dt.year
        self.__data['month_added'] = self.__data['date_added'].dt.month

        self.__data = self.__data.rename(columns={"listed_in":"genre"})
        self.__data['genre'] = self.__data['genre'].apply(lambda x: x.split(",")[0])
        self.__data.head()

        self.__data.describe(include='O')

    def __showPieChart(self):
        pieChart = PieChart(self.__data, px)
        pieChart.showChart()

    def __showLineChart(self):
        lineChart = LineChart(self.__data, go)
        lineChart.showChart()

    def __showTreeChart(self):
        treeChart = TreeChart(self.__data, pd, px)
        treeChart.showChart() 

    def showAllCharts(self):
        self.__showLineChart()
        self.__showPieChart()
        self.__showTreeChart()

dataSet = pd.read_csv("./dataset/netflix_titles.csv", index_col = "show_id", parse_dates = True)

chartBuilder = ChartBuilder(dataSet)

chartBuilder.showAllCharts()