import pandas as pd

languages = ['Python', 'Java', 'C++', 'JavaScript', 'TypeScript']
K = len(languages)

series_lang = pd.Series(languages, index=range(1, K + 1))

print("Series мов програмування:")
print(series_lang)