import yfinance as yf 

ticker = 'SBIN.NS'
df_SBI = yf.download(ticker, multi_level_index=False, auto_adjust=False)
df_SBI

df_ticker = yf.download(ticker, multi_level_index=False, auto_adjust=False)
df_ticker


file_path = f'C:/Users/nagar/Documents/IIQF PGPAT/New folder/SBI.xlsx'
file_path

df_ticker.to_excel(file_path)

df_ticker.to_csv(file_path)

df_SBI_2010 = df_SBI.loc['2010-01-01':,:].copy()

df_SBI_2010['change_tomorrow'] = df_SBI_2010.Close.pct_change(-1) * 100 * -1
df_SBI_2010


import numpy as np

df_SBI_2010['change_tomorrow_direction'] = np.where(
    df_SBI_2010.change_tomorrow > 0, 'UP' , 'DOWN')

df_SBI_2010.change_tomorrow_direction.value_counts()    

df_SBI_2010.to_excel(f'C:/Users/nagar/Documents/IIQF PGPAT/New folder/SBI processed.xlsx')

import pandas as pd
df = pd.read_excel(f'C:/Users/nagar/Documents/IIQF PGPAT/New folder/SBI processed.xlsx' , parse_dates=['Date'] , index_col=0)

target = df.change_tomorrow_direction
explanatory = df[['Open','High','Low','Close','Volume']]

from sklearn.ensemble import RandomForestClassifier

model_dt = RandomForestClassifier(max_depth=None)
model_dt.fit(explanatory, target)



y_pred = model_dt.predict(X=explanatory)
y_pred

df_predictions = df[['Open','High','Low','Close','Volume','change_tomorrow_direction']].copy()
df_predictions['prediction'] = y_pred
df_predictions

comp = df_predictions.change_tomorrow_direction == df_predictions.prediction
comp.sum()
len(comp)
comp.sum()/len(comp)

df_predictions.to_excel(f'C:/Users/nagar/Documents/IIQF PGPAT/New folder/SBI prediction.xlsx')

df_predictions.iloc[-1:, :]


import pickle

with open('C:/Users/nagar/Documents/IIQF PGPAT/New folder/SBImodel_dt_classification.pkl', 'wb') as f:
    pickle.dump(model_dt, f)


