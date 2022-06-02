class LineChart:
    __fig_line = None
    __large_title_format = 'Impacto da COVID-19 no lançamento de filmes e séries da Netflix.'
    __small_title_format = 'Devido à pandemia a atualização dos dados foi pausada.'

    def __init__(self, data, go):
        d1 = data[data["type"] == "TV Show"]
        d2 = data[data["type"] == "Movie"]
        col = "year_added"
        vc1 = d1[col].value_counts().reset_index().rename(columns = {col : "count", "index" : col})
        vc1['percent'] = vc1['count'].apply(lambda x : 100*x/sum(vc1['count']))
        vc1 = vc1.sort_values(col)
        vc2 = d2[col].value_counts().reset_index().rename(columns = {col : "count", "index" : col})
        vc2['percent'] = vc2['count'].apply(lambda x : 100*x/sum(vc2['count']))
        vc2 = vc2.sort_values(col)
        trace1 = go.Scatter(x=vc1[col], y=vc1["count"], name="Séries", marker=dict(color="#00f5d4"))
        trace2 = go.Scatter(x=vc2[col], y=vc2["count"], name="Filmes", marker=dict(color="#ff7d00"))
        data = [trace1, trace2]
        
        self.__fig_line = go.Figure(data)
        self.__fig_line.update_traces(hovertemplate=None)
        self.__fig_line.update_xaxes(showgrid=False)
        self.__fig_line.update_yaxes(showgrid=False)

    def showChart(self):
        self.__fig_line.update_layout(title=self.__large_title_format + " " + self.__small_title_format, 
            height=900, margin=dict(t=130, b=0, l=70, r=40), 
            hovermode="x unified", xaxis_title=' ', 
            yaxis_title=" ", plot_bgcolor='#001524', paper_bgcolor='#001524', 
            title_font=dict(size=25, color='#ffecd1',
            family="Lato, sans-serif"),
            font=dict(color='#ffecd1'),
            legend=dict(orientation="h",
            yanchor="bottom",
            y=1,
            xanchor="center",
            x=0.5)) 

        self.__fig_line.add_annotation(dict
            (x=0.8, 
            y=0.3,
            ax=0, 
            ay=0,
            xref = "paper",
            yref = "paper",
            text= "O ano em que mais séries foram lançadas foi 2019 seguido por 2020." )) 

        self.__fig_line.add_annotation(dict
            (x=0.9, 
            y=1,
            ax=0,
            ay=0,
            xref = "paper",
            yref = "paper",
            text= "O ano em que mais filmes foram lançados foi 2019 seguido por 2020" )) 
            
        self.__fig_line.show()