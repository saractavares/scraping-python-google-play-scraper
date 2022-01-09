<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/saractavares/scraping-python-google-play-scraper">
   <img src="https://github.com/saractavares/scraping-python-google-play-scraper/blob/main/readme/logo-scrap.png?raw=true" alt="Logo" width="150" height="150">
  </a>

  <h1 align="center">Scraping Usando Python</h1>
 Este projeto permite coletar reviews de qualquer app na google play store, você só precisa trocar o ID do app na função reviews_all().
  <br></br>
  <p align="center">
  <h4>App Sendo Coletado Nesse Momento = Alexa </h4>
    Um projeto de coleta, limpeza e armazenamento de dados provenientes da Google Play Store. </br>
    Banco de Dados: <strong> Google BigQuery </strong>
    <br></br>
    <a href="https://github.com/saractavares/scraping-python-google-play-scraper"><strong>Explore os arquivos »</strong></a>
    <br></br>
    <div style="display: inline_block">
     <img align="center" alt="sara-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
     <img align="center" alt="sara-HTML" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg">
     <img align="center" alt="sara-CSS" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg">
     <img align="center" alt="sara-bigquery" height="30" width="30" src="https://ssl.gstatic.com/pantheon/images/gcpIconGallery.svg?v2">
     <img align="center" alt="sara-sql" height="30" width="30" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Sql_data_base_with_logo.png/800px-Sql_data_base_with_logo.png">
    </div>
  </p>
</div>



```
Este projeto consiste em:
1º Raspagem dos comentários do aplicativo Alexa na Google Play Store
2º Limpeza dos dados coletados
3º Filtragem de acordo com a avaliação (estrelas dadas)
4º Geração de 3 arquivos csv's filtradas pela avaliação dos usuários 
5º Conexão e gravação no banco de dados de 3 tabelas de acordo com as avaliações
6º Backup dos Reports e dos CSV
7º Limpeza dos arquivos CSV já consumidos
```

## Bibliotecas Usadas:

- Google-Play_Scraper  -> para fazer o scraping
- Pandas-Profiling     -> para gerar os reports em html
- Pandas_gbq           -> para manipular o banco de dados Google BigQuery
- Pandas               -> para manipular os csv que irão para o banco
- NumPy                -> para manipulação das tabelas
- Google Auth          -> para autenticação da api do banco
- Time                 -> temporizador entre comandos
- os                   -> lib nativa do python que usa o sistema

## Exemplo de Análises Obtidas com Pandas Profiling:
<div style="display: inline_block">
     <img align="center" alt="sara-HTML" src="https://github.com/saractavares/scraping-python-google-play-scraper/blob/main/readme/aval_positivas.png?raw=true">
</div>

## Instruções windows:

Dentro de C:\Users<seu-usuario>\ faça o diretório onde trabalhará Sugestão de nome: scrap ex. do caminho: C:\Users\sara\scrap

  
## Instruções Linux: 

Faça o diretório onde trabalhará Sugestão de nome: scrap ex. do caminho: sara@sara:~/Área de Trabalho/scrap

## Passo a Passo:
  
Dentro de scrap faremos mais uma pasta "main". É dentro de main que faremos o git clone deste repositório. Resultado final do caminho: C:\Users\sara\scrap\main Certifique-se de estar igual.

Execute o VS Code a partir de main. A estrutura de pastas no VS Code deve ser:
  
```tree
SCRAP |_
        MAIN
```
  
Abra o terminal e execute: 
```git
git clone https://github.com/saractavares/scraping-python-google-play-scraper.git
```
Espere terminar.

Agora precisará executar a Venv. No terminal, digite e execute:

Windows:
```
scrap-env-win\Scripts\Activate.ps1
```
  
Linux:
```
  source scrap-env/bin/activate
```

Agora adicionaremos as bibliotecas necessárias: No terminal execute essa sequência, aguardando entre uma instalção e outra, claro:
  ```
  pip install google_play_scraper
  ```
  ```
  pip install pandas
  ```
  Atenção: Numpy é instalado junto com Pandas, no comando acima.

  ```
  pip install pandas_profiling
  ```
  ```
  pip install google-auth
  ```
  ```
  pip install pandas_gbq
  ```

Bibliotecas extras para evitar engasgos:
  ```
  pip install IPython
  ```
  ```
  pip install ipywidgets
  ```

| **Atenção**: Se mesmo após as instalações, o código ainda reclamar que não há a biblioteca, certifique-se de estar usando a mesma versão python, nesse caso é a 3.8.10 Você pode conferir isso no canto inferior esquerdo da janela do VsCode. Sempre recomendo reiniciar o Vs Code após a instalação das bibliotecas. |
| --- |
  
  
Podemos agora seguir para a parte do banco de dados. Para conseguir subir as tabelas, você precisará das credenciais de acesso. É o arquivo scrap-sauter-b84203485905.json que foi enviado no email.

  
A chave deve estar dentro da pasta "credentials", dentro de "database". Se não estiver, faça. A estrutura final deve ser:

  
Windows:
  ```
  C:\Users\sara\scrap\main\scraping-python-google-play-scraper\database\credentials\scrap-sauter-b84203485905.json
  ```

Linux:
  ```
  /home/sara/Área de Trabalho/scrap/main/scraping-python-google-play-scraper/database/credentials/scrap-sauter-b84203485905.json
  ```

  
Por padrão, o repositório no github não tráz as pastas de backup pois as adicionamos ao gitignore, então as faremos também. Dentro de scraping-python-google-play-scraper faça as pastas "page_backup" e "tables_backup".

A estrutura será:

  ```tree
  > SCRAP 
        |_ 
          > MAIN 
                |_ 
                  > scraping-python-google-play-scraper 
                        |_ 
                          > page_backup 
                          > tables_backup 
                          > database 
                              |_ 
                                > credentials 
                          ...
  ```

Sem mais delongas, hora de rodar! Abra o módulo scrap.py e execute!


  ### O fluxo da execução é:

```
1º scrap.py -> faz -> scraping por meio da lib google-play-scraper 
   depois   -> invoca -> tratamento.py

2º tratamento.py -> faz -> limpeza dos dados coletados e organização por score 
        depois   -> invoca -> file_factory.py

3º file_factory.py -> faz -> 3 arquivos html de report usando a lib pandas-profiling 
          depois   -> invoca -> drop.py

4º drop.py -> faz -> checagem se existe já tabelas no banco de dados, se sim, as apaga 
  depois   -> invoca -> insert_tables.py

5º insert_tables.py -> faz -> inserção dos arquivos csv nas tabelas correspondentes por meio de pandas_gbq
           depois   -> invoca -> limpar.py

6º limpar.py -> faz -> limpeza dos arquivos csv já consumidos da raiz local

--- Fim do Processo --- 
```
  
  
<div align=center> 
  <a href="https://instagram.com/dadososfatos/" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
  <a href = "mailto: sara27082011@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
  <a href="https://www.linkedin.com/in/saractavares" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
  <a href="https://saractavares.github.io/" target="_blank"><img src="https://img.shields.io/badge/-Portifolio-%d31717?style=for-the-badge&logo=portifolio&logoColor=<d31717>" target="_blank"></a>
</div>
