class TreeChart:
    pd = None 
    px = None 
    data = None

    def __init__(self, data, pd, px):
        self.data = data
        self.pd = pd
        self.px = px
        
    def showChart(self):
        print(self.data['genre'])

        df_genre = self.pd.DataFrame(self.data.genre.value_counts()).reset_index().rename(columns={'index':'genre', 'genre':'count'})
        fig_tree = self.px.treemap(df_genre, path=[self.px.Constant("Distribution of Geners"), 'count','genre'])

        fig_tree.update_layout(title='Highest watched Geners on Netflix',
            margin=dict(t=50, b=0, l=70, r=40),
            plot_bgcolor='#333', paper_bgcolor='#333',
            title_font=dict(size=25, color='#fff', family="Lato, sans-serif"),
            font=dict(color='#8a8d93'),
            hoverlabel=dict(bgcolor="#444", font_size=13, font_family="Lato, sans-serif"))

        fig_tree.show()