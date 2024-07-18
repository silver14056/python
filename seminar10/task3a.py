import seaborn as sns


def length_group(x):
    if x < 35:
        return 'low'
    elif 35 <= x <= 42:
        return 'middle'
    else:
        return 'high'


penguins = sns.load_dataset("penguins")
penguins['height_group'] = penguins['bill_length_mm'].apply(length_group)
print(penguins[penguins['height_group'] == 'low'])
penguins.to_csv('penguins.csv', index=False)

