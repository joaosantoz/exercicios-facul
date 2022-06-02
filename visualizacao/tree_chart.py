class TreeChart:
    __pd = None 
    __px = None 
    __data = None

    def __init__(self, data, pd, px):
        self.__data = data
        self.__pd = pd
        self.__px = px
        
    def showChart(self):
        df_genre = self.__pd.DataFrame(self.__data.genre.value_counts()).reset_index().rename(columns={'index':'genre', 'genre':'count'})
        fig_tree = self.__px.treemap(df_genre, path=[self.__px.Constant("Distribuição dos Gêneros"), 'count','genre'])

        fig_tree.update_layout(title='Gêneros mais assistidos da Netflix',
            margin=dict(t=50, b=0, l=70, r=40),
            plot_bgcolor='#001524', paper_bgcolor='#001524',
            title_font=dict(size=25, color='#fff', family="Lato, sans-serif"),
            font=dict(color='#8a8d93'),
            hoverlabel=dict(bgcolor="#444", font_size=13, font_family="Lato, sans-serif"))

        fig_tree.show()