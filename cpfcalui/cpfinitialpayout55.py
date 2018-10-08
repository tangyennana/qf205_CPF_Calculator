import numpy as np
import pandas as pd

data = np.array([['','SP','BP','EP'],
                ['BRS',745,690,580],
                ['FRS',1365,1265,1060],
                ['ERS',1985,1840,1545]])
df = pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:])
print(df)