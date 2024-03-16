class CriandoAlgoritmo():
    def __init__(self) -> None:
        pass
    def analisando_texto(self, text):
        #Tirando pontos e virgulas do texto
        text = text.replace(".", "").replace(",", "")

        #Criando a lista de palavras boas
        lista_de_palavras_boas = ['magnífico','esplêndido','majestoso','encantador','fascinante','deslumbrante',
            'deslumbrante','pitoresco','estonteante','resplandecente','aprovo','admiro','aprecio','gosto','encanto',
            'estimulo','louvo','valorizo','enalteço','recomendo','boa','bom','amigável','bondoso','generoso','compreensivo',
            'empático','atencioso','carismático','encorajador','inspirador','talentoso','inteligente','criativo','honesto',
            'confiável','determinado','corajoso','otimista','enérgico','resiliente','respeitoso','belo','encantador','elegante',
            'sofisticado','magnífico','deslumbrante','estonteante','fascinante','excepcional','surpreendente','extraordinário',
            'inovador','fantástico','brilhante','espetacular','impecável','exuberante','notável','impressionante','deslumbrante', 'bonito', 'lindo', 'muito', 'pouco']

        #Criando a lista de palavras ruins
        lista_de_palavras_ruins = ['terrível','péssima','horrível','desagradável','ruim','medíocre','insatisfatória','fraca',
            'decepcionante','desastroso','desaprovo','desgosto','desprezo','detesto','abomino','critico','repudio','rejeito','condeno',
            'desdenho','egoísta','arrogante','insensível','mesquinho','manipulador','desonesto','rancoroso','cínico','preconceituoso',
            'teimoso','imprevisível','inflexível','indiferente','irritável','impaciente','egocêntrico','hostil','agressivo','falso',
            'pessimista','feio','desagradável','desconfortável','desordenado','desinteressante','obsoleto','repugnante','repetitivo',
            'ineficiente','desnecessário','complicado','desajeitado','insatisfatório','desconfortável','desajeitado','desprovido',
            'desorganizado','desgastado','frustrante','desanimador', 'feio', 'muito', 'pouco', 'feia']

        #Codigo em qual lista a palavra esta
        palavras = text.split()
        ruim = []
        boa = []
        neutras = []
        for i in palavras:
            if i in lista_de_palavras_boas:
                boa.append(i)
            elif i in lista_de_palavras_ruins:
                ruim.append(i)
            else:
                neutras.append(i)

        qtd_boa = len(boa)
        qtd_ruim = len(ruim)
        qtd_neutras= len(neutras)

        if qtd_neutras > (qtd_boa+qtd_ruim)**3:
            print(f'O texto {text}, foi consioderado neutro.')

        elif qtd_boa > qtd_ruim:
            print(f'O texto {text}, foi consioderado bom.')

        else:
            print(f'O texto {text}, foi consioderado ruim.')