from analise_dados_nao_estruturados import AULA06

#OS TEXTOS PRECISAM ESTAR EM INGLES

documento = """
Amarillo, texas, is known for its abundance of cattle, a local restaurant’s 72-ounce steak-eating challenge and, along an interstate highway, a vibrant drug trade. It is the narcotics traffickers who fill the town’s federal courthouse. Judge Matthew Kacsmaryk, appointed by Donald Trump to preside over the vast rural division, spends most days overseeing trials about fentanyl pills and powdered meth. But his rulings on several spicier cases have made the 47-year-old a conservative darling far beyond the Texas panhandle.
Mr Kacsmaryk, who was brought up evangelical, reads the law like verses of Deuteronomy, interpreting the constitution by attempting to divine what it meant in the founding era. That conservative philosophy has led Texas’s attorney-general and other right-wing lawyers to bring cases against the Biden administration to Amarillo, where Mr Kacsmaryk hears each one.
"""

para_tokenizar = AULA06(documento).tokenizando("palavras")

para_identificando_entidades_e_sentencas = AULA06(documento).identificando_entidades_e_sentencas()

para_analisando_as_sentencas = AULA06(documento).analisando_as_sentencas()

para_extarir_os_topicos = AULA06(documento).extraindo_topicos()

para_extrair_resumo = AULA06(documento).extrair_resumo()