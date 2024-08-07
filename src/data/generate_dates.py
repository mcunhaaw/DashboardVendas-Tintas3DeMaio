import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Função para gerar datas
def generate_dates(start_date, end_date):
    return pd.date_range(start_date, end_date, freq='D')

# Gerando dados fictícios para vendas e devoluções
start_date = '2024-07-01'
end_date = '2024-07-31'
dates = generate_dates(start_date, end_date)

# Dados de vendas
np.random.seed(42)  # Para reprodutibilidade
sales_data = pd.DataFrame({
    'Data': dates,
    'Sales': np.random.randint(100, 1000, size=len(dates))
})
sales_data['Ano'] = sales_data['Data'].dt.year
sales_data['Mes'] = sales_data['Data'].dt.month
sales_data['Dia'] = sales_data['Data'].dt.day

# Dados de devoluções
returns_data = pd.DataFrame({
    'Return Date': dates,
    'Returns': np.random.randint(0, 100, size=len(dates))
})
returns_data['Ano'] = returns_data['Return Date'].dt.year
returns_data['Mes'] = returns_data['Return Date'].dt.month
returns_data['Dia'] = returns_data['Return Date'].dt.day

# Salvando os dados em CSV
sales_data_path = 'sales_data_july_2024.csv'
returns_data_path = 'returns_data_july_2024.csv'

sales_data.to_csv(sales_data_path, index=False)
returns_data.to_csv(returns_data_path, index=False)

sales_data_path, returns_data_path
