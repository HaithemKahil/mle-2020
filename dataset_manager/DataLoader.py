import pandas as pd


class DataLoader :

    def load_csv_as_df(self, path:str) -> pd.DataFrame:
        return pd.read_csv(path)

    def load_csv_as_object(self,path:str) -> object:
        pass
