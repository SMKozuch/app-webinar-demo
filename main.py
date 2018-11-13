import pandas as pd
from keboola import docker



cfg = docker.Config('/data/')
params = cfg.get_parameters()

n_times = params['number_of_times']

in_tables = cfg.get_input_tables()
data = pd.read_csv(in_tables[0]['full_path'])

data = data.append([data] * n_times, ignore_index=True)

data.to_csv('/data/out/tables/output.csv', index=False)
cfg.write_table_manifest('/data/out/tables/output.csv',
                            destination='out.c-webinar.demo')

print('Done')