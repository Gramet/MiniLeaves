import pandas as pd
import os

subs = [f for f in os.listdir('/home/gaetan/Downloads') if f.startswith('sub') and f.endswith('.csv')]

print(len(subs))

list_subs = []
for sub in subs:
    df = pd.read_csv(os.path.join('/home/gaetan/Downloads', sub))
    if len(df)==10838:
        list_subs.append(df)

df_tot = pd.concat(list_subs, axis=1, sort=False)
df_tot['majority'] = df_tot.mode(axis=1)[0]
sub_v_df = pd.DataFrame(list(df_tot['majority'].apply(int).values))
sub_v_df.to_csv('submission_voting.csv',header=['class_index'],index=False)

