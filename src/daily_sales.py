import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DailySales:
    def __init__(self, sales_data: pd.DataFrame, returns_data: pd.DataFrame):
        self.sales_data = sales_data
        self.returns_data = returns_data

    def preprocess_data(self):
        self.sales_data['Data'] = pd.to_datetime(self.sales_data['Data'])
        self.sales_data['Dia'] = self.sales_data['Data'].dt.day
        self.returns_data['Data'] = pd.to_datetime(self.returns_data['Data'])
        self.returns_data['Dia'] = self.returns_data['Data'].dt.day

    def daily_sales(self):
        daily_sales = self.sales_data.groupby(['Ano', 'Mes', 'Dia'])['Vendas'].sum().reset_index()
        daily_returns = self.returns_data.groupby(['Ano', 'Mes', 'Dia'])['Returns'].sum().reset_index()
        daily_sales = daily_sales.merge(daily_returns, left_on=['Ano', 'Mes', 'Dia'], right_on=['Ano', 'Mes', 'Dia'], how='left').fillna(0)
        daily_sales['VendasLiquidas'] = daily_sales['Vendas'] - daily_sales['Returns']
        return daily_sales

    def plot_daily_sales(self):
        daily_sales = self.daily_sales()
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=daily_sales, x='Dia', y='VendasLiquidas', hue='Mes')
        plt.title('Vendas Líquidas')
        plt.xlabel('Dia')
        plt.ylabel('Vendas Líquidas')
        return plt.gcf()  # Retorna a figura criada
