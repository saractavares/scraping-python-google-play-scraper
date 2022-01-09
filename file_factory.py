import os
from tratamento import df_positiva, df_neutra, df_negativa
from pandas_profiling import ProfileReport as pr


path = os.getcwd()

#Report Positivas
profile_positivo = pr(df_positiva, title='Report Geral Reviews Alexa - Avaliações Positivas',
                      html={'style': {'full_width': True}})
profile_positivo.to_notebook_iframe()
profile_positivo.to_file(output_file=f"{path}/Report_Positivas.html")
profile_positivo.to_file(output_file=f"{path}/main/scraping-python-google-play-scraper/page_backup/Report_Positivas.html")

# Report Neutras
profile_neutra = pr(df_neutra, title='Report Geral Reviews Alexa - Avaliações Neutras',
                    html={'style': {'full_width': True}})
profile_neutra.to_notebook_iframe()
profile_neutra.to_file(output_file=f"{path}/Report_Neutras.html")
profile_neutra.to_file(output_file=f"{path}/main/scraping-python-google-play-scraper/page_backup/Report_Neutras.html")

# Report Negativas
profile_negativa = pr(df_negativa, title='Report Geral Reviews Alexa - Avaliações Negativas',
                      html={'style': {'full_width': True}})
profile_negativa.to_notebook_iframe()
profile_negativa.to_file(output_file=f"{path}/Report_Negativas.html")
profile_negativa.to_file(output_file=f"{path}/main/scraping-python-google-play-scraper/page_backup/Report_Negativas.html")

# Salvando localmente as tabelas que serão inseridas no banco
df_positiva.to_csv(f"{path}/df_positiva.csv", sep="|", index=False)
df_neutra.to_csv(f"{path}/df_neutra.csv", sep="|", index=False)
df_negativa.to_csv(f"{path}/df_negativa.csv", sep="|", index=False)

# Backup de tabelas já consumidas, para histórico
df_positiva.to_csv(f"{path}/main/scraping-python-google-play-scraper/tables_backup/df_positiva.csv", sep=";", index=False)
df_neutra.to_csv(f"{path}/main/scraping-python-google-play-scraper/tables_backup/df_neutra.csv", sep=";", index=False)
df_negativa.to_csv(f"{path}/main/scraping-python-google-play-scraper/tables_backup/df_negativa.csv", sep=";", index=False)


print('_____________ Acionando a Limpeza do Banco de Dados _____________')

import drop
