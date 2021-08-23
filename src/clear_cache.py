import os

with open('newest_ts', 'r') as f:
    newest_ts = f.read()

print(f"The newest timestamp is {newest_ts}.")

data_list = os.listdir('./data')
data_list.remove('historical')
data_list.remove(f'data_{newest_ts}.json')

for f in data_list:
    os.rename(f"./data/{f}", f"./data/historical/{f}")