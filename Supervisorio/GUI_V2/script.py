import pandas as pd
from pprint import pprint
file = 'C:/Users/Rafael Lucena/Workspace/TCC/Supervisorio/GUI_V2/testes/exemplo_xlsx.xlsx'

df = pd.read_excel(file, header=0)
print([col for col in df.columns])