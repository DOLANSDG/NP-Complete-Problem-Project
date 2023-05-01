"""
Creates graphs from csv
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1], sep=',')
max_value = max(list(df['runtime']))
df['runtime'] = df['runtime'].apply(lambda x: x / max_value)

r = range(250)
y = [y**3 for y in r]
max_value = max(y)
y = list(map(lambda x: x / max_value, y))

plt.plot(r, y, label='x^3')
plt.plot(df['V_size'], df['runtime'], label='test data')
plt.legend()
plt.ylabel('runtime (normalized)')
plt.xlabel('number of vertices')
plt.show()

print()
