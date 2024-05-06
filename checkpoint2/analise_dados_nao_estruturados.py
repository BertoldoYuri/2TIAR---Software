import nltk
from nltk import pos_tag, ne_chunk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tree import Tree
from nltk.corpus import wordnet

from collections import Counter

import pandas as pd


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')
nltk.download('stopwords')

class AULA06:
    def __init__(self, texto) -> None:
        self.doc = texto

    def tokenizando(self, tipos):
        tokens = []
        texto = self.doc

        if tipos == 'frases':
            tokens.extend(sent_tokenize(texto))

        elif tipos == 'palavras':
            # Load stopwords
            stopwords_ingles = stopwords.words('english')

            # Tokenize and remove stopwords
            tokens_sem_stopwords = []
            for palavra in word_tokenize(texto):
                if palavra not in stopwords_ingles:
                    tokens_sem_stopwords.append(palavra)
            tokens.extend(tokens_sem_stopwords)

        elif tipos == 'paragrafos':
            tokens.extend(texto.split('\n\n'))
        else:
            raise ValueError("O tipo de tokenização especificado não é válido. Por favor, escolha entre 'frases', 'palavras' ou 'paragrafos'.")

        return tokens


    def identificando_entidades_e_sentencas (self):
        textos = self.tokenizando("palavras")
        
        tags = pos_tag(textos)

        entities = []
        for word, tag in tags:
            if tag in ['NNP', 'NNPS']:  # People and Organizations
                entities.append((word, "PERSON/ORGANIZATION"))
            elif tag in ['NN']:  # Locations (may have false positives)
                entities.append((word, "LOCATION"))
            elif tag in ['CD']:  # Dates (may have false positives)
                entities.append((word, "DATE"))

        df_novo = pd.DataFrame(entities, columns=('palavras', 'entidades'))

        return df_novo

    def analisando_as_sentencas(self):
        texto = self.doc

        # Tokenize o texto em palavras e frases
        tokens = word_tokenize(texto)
        sentences = sent_tokenize(texto)

        # Part-of-speech tagging
        tags = pos_tag(tokens)

        # Named Entity Recognition (NER)
        ner_chunks = ne_chunk(tags)

        # Prepare empty dictionary for results
        analysis_results = {}

        # Semantic Analysis (WordNet)
        wordnets = []
        for word, tag in tags:
            if tag.startswith('NN'):  # Apenas substantivos para este exemplo
                synsets = wordnet.synsets(word)
                if synsets:
                    wordnets.append((word, synsets[0]))

        return analysis_results
    

    def extraindo_topicos(self):

        textos = self.tokenizando("palavras")

        contador = Counter(textos)

        dd = []
        # Exibir a contagem de cada palavra
        for palavra, contagem in contador.items():
            dd.append({"palavra":palavra,"QTD":contagem})

        df = pd.DataFrame(dd)

        df_ordenado = df.sort_values(by='QTD', ascending=False)
            
        return df_ordenado

    def extrair_resumo(self):

        df_principais_topicos = self.extraindo_topicos()

        l_analisando_sentesas = self.analisando_as_sentencas()

        df_analisando_sentesa_tokens = pd.DataFrame(l_analisando_sentesas['tokens'], columns=("Palavra", "Token"))

        df_analisando_sentesa_wordnets = pd.DataFrame(l_analisando_sentesas['wordnet_synsets'], columns=("Palavra", "Synsets"))

        df_identificando_entidades_e_sentencas = self.identificando_entidades_e_sentencas()

        df_final = df_principais_topicos.merge(df_analisando_sentesa_tokens, on='palavra', how='left')\
                                        .merge(df_analisando_sentesa_wordnets, on='palavra', how='left')\
                                        .merge(df_identificando_entidades_e_sentencas, on='palavra', how='left')

        return df_principais_topicos, df_analisando_sentesa_tokens, df_analisando_sentesa_wordnets, df_identificando_entidades_e_sentencas       


