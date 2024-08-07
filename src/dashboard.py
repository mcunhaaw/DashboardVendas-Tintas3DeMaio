import os
import streamlit as st
from data_loader import DataLoader
from sales_analysis import SalesAnalysis
from returns_analysis import ReturnsAnalysis
from daily_sales import DailySales

class SalesDashboard:
    def __init__(self, sales_file_path, returns_file_path):
        self.sales_file_path = sales_file_path
        self.returns_file_path = returns_file_path

    def run(self):
        st.title('Dashboard de Vendas - Tintas Três de Maio')

        # Criar instâncias do DataLoader com o caminho relativo à pasta 'Data'
        sales_loader = DataLoader(os.path.join('Data', self.sales_file_path))
        returns_loader = DataLoader(os.path.join('Data', self.returns_file_path))
        
        # Carregar dados
        try:
            sales_data = sales_loader.load_data()
            returns_data = returns_loader.load_data()
        except FileNotFoundError as e:
            st.error(str(e))
            return

        # Exibir tabelas de dados
        st.subheader('Dados de Vendas')
        st.dataframe(
            sales_data.head().style
            .background_gradient(cmap='Blues')
            .format("{:.2f}")
            .set_properties(**{'font-size': '18px', 'text-align': 'center'})
            .set_table_styles(
                [{'selector': 'thead th', 'props': [('font-size', '20px')]}]
            )
        )
        
        st.subheader('Dados de Devoluções')
        st.dataframe(
            returns_data.head().style
            .background_gradient(cmap='Reds')
            .format("{:.2f}")
            .set_properties(**{'font-size': '18px', 'text-align': 'center'})
            .set_table_styles(
                [{'selector': 'thead th', 'props': [('font-size', '20px')]}]
            )
        )

        # Sales Analysis
        sales_analysis = SalesAnalysis(sales_data)
        sales_analysis.preprocess_data()

        # Returns Analysis
        returns_analysis = ReturnsAnalysis(returns_data)
        returns_analysis.preprocess_data()

        # Daily Sales Analysis
        daily_sales = DailySales(sales_data, returns_data)
        daily_sales.preprocess_data()

        # Display Sales Plots
        st.subheader('Vendas mensais')
        fig_sales = sales_analysis.plot_monthly_sales()
        st.plotly_chart(fig_sales)

        # Display das devoluções
        st.subheader('Devoluções mensais')
        fig_returns = returns_analysis.plot_monthly_returns()
        st.plotly_chart(fig_returns)

        # Display vendas líquidas diárias
        st.subheader('Vendas Líquidas Diárias')
        daily_sales_data = daily_sales.daily_sales()
        st.dataframe(
            daily_sales_data.pivot_table(index='Dia', columns='Mes', values='VendasLiquidas')
            .style.background_gradient(cmap='Greens')
            .format("{:.2f}")
            .set_properties(**{'font-size': '18px', 'text-align': 'center'})
            .set_table_styles(
                [{'selector': 'thead th', 'props': [('font-size', '20px')]}]
            )
        )

        st.subheader('Vendas Totais Diárias - gráfico estimado')
        fig_daily_sales = daily_sales.plot_daily_sales()
        st.plotly_chart(fig_daily_sales)
        
