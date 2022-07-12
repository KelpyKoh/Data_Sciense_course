import pandas as pd
dff = pd.DataFrame({
    'id': [12,3,5],
    'cat': ['t','r','u']
})
dff.plot(kind='bar')