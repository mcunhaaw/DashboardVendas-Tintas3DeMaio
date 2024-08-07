import plotly.graph_objects as go
import pandas as pd

class ReturnsAnalysis:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def preprocess_data(self):
        self.data['Data'] = pd.to_datetime(self.data['Data'])
        self.data['Mes'] = self.data['Data'].dt.month
        self.data['Ano'] = self.data['Data'].dt.year
        self.data['Dia'] = self.data['Data'].dt.day

    def monthly_returns(self):
        monthly_returns = self.data.groupby(['Ano', 'Mes'])['Returns'].sum().reset_index()
        return monthly_returns

    def plot_monthly_returns(self):
        monthly_returns = self.monthly_returns()
        fig = go.Figure()

        for year in monthly_returns['Ano'].unique():
            yearly_data = monthly_returns[monthly_returns['Ano'] == year]
            fig.add_trace(go.Scatter(x=yearly_data['Mes'], y=yearly_data['Returns'],
                                     mode='lines+markers', name=f'Ano {year}'))

        fig.update_layout(title='Devoluções Mensais',
                          xaxis_title='Mês',
                          yaxis_title='Devoluções',
                          template='plotly_white')

        return fig
