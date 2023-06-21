df.loc[df['population'] < 500, ['median_house_value']]
df[df['population'] == df['population'].min()]['households'].max()