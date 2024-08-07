import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            print(data.columns) 
            print(data.dtypes)  

            data['Data'] = pd.to_datetime(data['Data'])

            print(data.dtypes)  
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"O arquivo {self.file_path} não foi encontrado.")