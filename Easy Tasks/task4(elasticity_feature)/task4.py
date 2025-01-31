import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def elasticity_df(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Function for finding elasticity
    '''

    df_grouped = df.groupby('sku')

    results = []

    for sku, group in df_grouped:
        # Add 1 to log to escape log(0) case
        log_sales = np.log(group['qty'] + 1)

        price = group['price'].values.reshape(-1, 1)

        model = LinearRegression()
        model.fit(price, log_sales)

        log_sales_pred = model.predict(price)

        # R-squared will be our elasticity
        r_squared = r2_score(log_sales, log_sales_pred)

        results.append({'sku': sku, 'elasticity': r_squared})

    results = pd.DataFrame(results)

    return results
