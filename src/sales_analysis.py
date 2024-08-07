import plotly.graph_objects as go
import pandas as pd

class SalesAnalysis:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def preprocess_data(self):
        self.data['Data'] = pd.to_datetime(self.data['Data'])
        self.data['Mes'] = self.data['Data'].dt.month
        self.data['Ano'] = self.data['Data'].dt.year
        self.data['Dia'] = self.data['Data'].dt.day

    def monthly_sales(self):
        monthly_sales = self.data.groupby(['Ano', 'Mes'])['Vendas'].sum().reset_index()
        return monthly_sales

    def plot_monthly_sales(self):
        monthly_sales = self.monthly_sales()
        fig = go.Figure()

        for year in monthly_sales['Ano'].unique():
            yearly_data = monthly_sales[monthly_sales['Ano'] == year]
            fig.add_trace(go.Scatter(x=yearly_data['Mes'], y=yearly_data['Vendas'],
                                     mode='lines+markers', name=f'Ano {year}'))

        fig.update_layout(title='Vendas Mensais',
                          xaxis_title='Mês',
                          yaxis_title='Vendas',
                          template='plotly_white')

        return fig
