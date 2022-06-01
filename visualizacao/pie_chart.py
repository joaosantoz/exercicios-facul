class PieChart:
    px = None

    def __init__(self, data, px):
        self.px = px
        self.data = data

    def showChart(self):
        labels = {
            'Movie': 'Filme',
            'TV Show': 'Série'
        }

        self.data['type'] = self.data['type'].replace(labels)

        fig_donut = self.px.pie(self.data, names='type', height=500, width=1000, hole=0.7,
        title='Categoria Mais Assistida Netflix',
        color_discrete_sequence=['#ff7d00', '#00f5d4'])
        fig_donut.update_traces(hovertemplate=None, textposition='outside',
        textinfo='percent+label', rotation=90)
        fig_donut.update_layout(margin=dict(l=20, r=20), showlegend=False,
        plot_bgcolor='#001524', paper_bgcolor='#001524',
        title_font=dict(size=25, color='#ffecd1', family="Lato, sans-serif"),
        font=dict(size=17, color='#ffecd1'),
        hoverlabel=dict(bgcolor="#444", font_size=13,
        font_family="Lato, sans-serif"))

        fig_donut.show()