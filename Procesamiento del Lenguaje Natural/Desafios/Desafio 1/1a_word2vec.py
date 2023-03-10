# -*- coding: utf-8 -*-
"""1a - word2vec.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ftFK68w3M8eiDONvKRMaSJ1I9aZpa5xK

<img src="https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/procesamiento_lenguaje_natural/raw/main/logoFIUBA.jpg" width="500" align="center">


# Procesamiento de lenguaje natural
## Word2vect
"""

import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * (np.linalg.norm(b)))

"""### Datos"""

corpus = np.array(['que dia es hoy', 'martes el dia de hoy es martes', 'martes muchas gracias'])

"""Documento 1 --> que dia es hoy \
Documento 2 --> martes el dia de hoy es martes \
Documento 3 --> martes muchas gracias

### 1 - Obtener el vocabulario del corpus (los términos utilizados)
- Cada documento transformarlo en una lista de términos
- Armar un vector de términos no repetidos de todos los documentos
"""

def obtener_vocabulario(documento):
  return documento.split()

vocabulario=list(map(obtener_vocabulario,corpus))
print(vocabulario)

unicos=[]
def is_in(documento):
  for termino in documento:
    if termino not in unicos:
      unicos.append(termino) 
      
def terminos_unicos(corpus):
  for documento in corpus:
    is_in(documento)

terminos_unicos(vocabulario)
print(unicos)

"""### 2- OneHot encoding
Data una lista de textos, devolver una matriz con la representación oneHotEncoding de estos
"""

import pandas as pd

oneHot = []
def oneHotEncoding(document):
  lista=[]
  for palabra in unicos:
    if palabra in document:
      lista.append(1)
    else:
      lista.append(0)
  return lista
for document in vocabulario:
  oneHot.append(oneHotEncoding(document))

df = pd.DataFrame(oneHot,columns=unicos)
df.head()

"""### 3- Vectores de frecuencia
Data una lista de textos, devolver una matriz con la representación de frecuencia de estos
"""

vF = []
def vectFrec(document):
  lista=[]
  for palabra in unicos:
    if palabra in document:
      lista.append(document.count(palabra))
    else:
      lista.append(0)
  return lista
for document in vocabulario:
  vF.append(vectFrec(document))

df_v = pd.DataFrame(vF,columns=unicos)
df_v.head()

"""### 4- TF-IDF
Data una lista de textos, devolver una matriz con la representacion TFIDF
"""

from math import log

def factorIDF(vocabulario):
  idf=[]
  tamañoCorpus=len(vocabulario)
  for palabra in unicos:
    cant=0
    for document in vocabulario:
      if palabra in document:
        cant+=1
    idf.append(log(tamañoCorpus/cant,10))
  return(idf)

idf=factorIDF(vocabulario)

df_idf = pd.DataFrame([idf],columns=unicos)
df_idf.head()

import numpy as np

tf_df=np.asarray(idf)*np.asarray(vF)
df_tf=pd.DataFrame(tf_df,columns=unicos)
df_tf.head()

"""### 5 - Comparación de documentos
Realizar una funcion que reciba el corpus y el índice de un documento y devuelva los documentos ordenados por la similitud coseno
"""

lista_similitud=[]
def similitud(corpus,indice):
  doc1=corpus[indice]
  simil=[]
  for im,documento in enumerate(corpus):
    simil.append((documento,cosine_similarity(np.asarray(oneHotEncoding(documento)),np.asarray(oneHotEncoding(doc1)))))
  return sorted(simil, key=lambda x: x[1], reverse=True)

lista_similitud=similitud(corpus,2)

df_cs = pd.DataFrame(lista_similitud, columns= ["Documento","Cosine Similarity"])

df_cs.head()

