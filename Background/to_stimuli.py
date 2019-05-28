import pandas as pd
import  csv
import numpy as np
from sklearn.utils import shuffle


#files = ['eng_fin.csv', 'eng_non.csv', 'fin_fin.csv', 'fin_non.csv']
files = ['eng_fin.csv', 'eng_non.csv']
files_fin = ['fin_fin.csv', 'fin_non.csv']

# Generate vector to match numbers of matching word pairs
fin_brands = np.arange(60)
non_brands = np.arange(60) + 120

# Shuffle order
np.random.shuffle(fin_brands)
np.random.shuffle(non_brands)

# Split data to English and Finnish tests
non_eng, non_fin = np.split(non_brands, 2)
fin_eng, fin_fin = np.split(fin_brands, 2)

# On English test stimuli are adder to df_test1
empty = []
df_test1 = pd.DataFrame({'stimuli':empty, 'no':empty})

# On Finnish test stimuli are adder to df_test2
df_test2 = pd.DataFrame({'stimuli':empty, 'no':empty})

for file in files:
    df = pd.read_csv(file)
    df['Matching'] = df['Matching'].str.lower()
    stimuli = []
    stimuli_no = []
    for i in range(60):
        if df.iloc[i,3] == 1:
            text = df.iloc[i,1] + ' ' + df.iloc[i,0]
        else:
            text = df.iloc[i,0] + ' ' + df.iloc[i,1]
        if file == 'eng_non.csv':
            if df.iloc[i,5] in non_eng+1:
                stimuli.append(text)
                stimuli_no.append(df.iloc[i,5])
        else:
            if df.iloc[i,5] in fin_eng+1:
                stimuli.append(text)
                stimuli_no.append(df.iloc[i,5])
    df2 = pd.DataFrame({'stimuli':stimuli, 'no':stimuli_no})
    df_test1 = pd.concat([df_test1, df2],ignore_index=True)


for file in files:
    df = pd.read_csv(file)
    df['Conflicting'] = df['Conflicting'].str.lower()
    stimuli = []
    stimuli_no = []
    for i in range(60):
        if df.iloc[i,4] == 1:
            text = df.iloc[i,2] + ' ' + df.iloc[i,0]
        else:
            text = df.iloc[i,0] + ' ' + df.iloc[i,2]
        if file == 'eng_non.csv':
            if df.iloc[i,6] in non_eng+61:
                stimuli.append(text)
                stimuli_no.append(df.iloc[i,6])
        else:
            if df.iloc[i,6] in fin_eng+61:
                stimuli.append(text)
                stimuli_no.append(df.iloc[i,6])
    df2 = pd.DataFrame({'stimuli':stimuli, 'no':stimuli_no})
    df_test1 = pd.concat([df_test1, df2],ignore_index=True)

# We shuffle the order of stimuli
df_test1 = shuffle(df_test1)



# TEST 2
for file in files_fin:
    df = pd.read_csv(file)
    df['Matching'] = df['Matching'].str.lower()
    stimuli = []
    stimuli_no = []
    for i in range(60):
        if df.iloc[i,3] == 1:
            text = df.iloc[i,1] + ' ' + df.iloc[i,0]
        else:
            text = df.iloc[i,0] + ' ' + df.iloc[i,1]
        if file == 'fin_non.csv':
            if df.iloc[i,5] in non_eng+1:
                stimuli.append(text)
                stimuli_no.append(df.iloc[i,5])
        else:
            if df.iloc[i,5] in fin_eng+1:
                stimuli.append(text)
                stimuli_no.append(df.iloc[i,5])
    df2 = pd.DataFrame({'stimuli':stimuli, 'no':stimuli_no})
    df_test2 = pd.concat([df_test2, df2],ignore_index=True)


for file in files_fin:
    df = pd.read_csv(file)
    df['Conflicting'] = df['Conflicting'].str.lower()
    stimuli = []
    stimuli_no = []
    for i in range(60):
        if df.iloc[i,4] == 1:
            text = df.iloc[i,2] + ' ' + df.iloc[i,0]
        else:
            text = df.iloc[i,0] + ' ' + df.iloc[i,2]
        if file == 'fin_non.csv':
            if df.iloc[i,6] in non_eng+61:
                stimuli.append(text)
                stimuli_no.append(df.iloc[i,6])
        else:
            if df.iloc[i,6] in fin_eng+61:
                stimuli.append(text)
                stimuli_no.append(df.iloc[i,6])
    df2 = pd.DataFrame({'stimuli':stimuli, 'no':stimuli_no})
    df_test2 = pd.concat([df_test2, df2],ignore_index=True)


df_test2 = shuffle(df_test2)

df_test1.to_csv('test1.csv', index=False)
df_test2.to_csv('test2.csv', index=False)