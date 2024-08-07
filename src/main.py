import os
from dashboard import SalesDashboard

def main():
    dashboard = SalesDashboard('sales_data_july_2024.csv', 'returns_data_july_2024.csv')
    dashboard.run()

if __name__ == '__main__':
    main()
