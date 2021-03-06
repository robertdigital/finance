from src import finance_model as fm
import os

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'IBM', 'FB', 'SNAP']

identifiers = ['Gap']

ID_ABV = {
    'High': 'h',
    'Low': 'l',
    'Open': 'op',
    'Close': 'cp',
    'Volume': 'vol',
    'Adj Close': 'acp',
    'Gap': 'gp'
}


for ticker in tickers:
    for identifier in identifiers:
        model, history = fm.train(ticker, identifier=identifier)

        path = '../models/' + ticker.lower() + '/'
        id_abv = ID_ABV[identifier]

        try:
            os.mkdir(path)
        except FileExistsError:
            print('Model directory already exists.')
        except FileNotFoundError:
            print('Model directory not found. Try different path name.')

        fm.save(model=model, history=history,
                identifier=id_abv, path=path)
