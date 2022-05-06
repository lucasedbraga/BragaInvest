import matplotlib.pyplot as plt


def juros_compostos(c,i,t, plot=False):
	"""
	:param c: Capital
	:param i: Taxa (aa)
	:param t: Tempo (anos)
	"""
	m = c*((1+(i/100))**t)

	if plot:
		valores = [c]
		for n in range(2,t):
			valores.append(valores[-1]*(1+(i/100)))
		print(valores)
		plt.plot(valores)
		plt.show()
					
	return m

def recorrente_juros_compostos(c,i,t, plot=False):
	"""
	:param c: Capital
	:param i: Taxa (aa)
	:param t: Tempo (anos)
	"""
	m = c*((1+(i/100))**t)

	valores = [c]
	for n in range(1, t):
		valores.append(c+(valores[-1]*(1+(i/100))))

	if plot:
		plt.plot(valores)
		plt.show()
					
	return valores

def juros_simples(c,i,t, plot=False):
	"""
	:param c: Capital
	:param i: Taxa (aa)
	:param t: Tempo (anos)
	"""
	m = c*(1+(i/100)*t)

	if plot:
		pass
		
	return m


def fluxo_caixa_descontado(cc_a, c_d, t_pl,  t_d, investimento, juros, tempo):
	"""
	Cálculo da capacidade de geração de caixa em t instantes
	cc_a: Custo de Capital aos acionistas
	c_d: Custo da dívida
	t_pl: Total de patrimônio líquido
	t_d: Total de dívida
	investimento:
	juros:
	tempo: Tempo
	"""

	# Taxa de Desconto
	taxa_min_atratividade = (cc_a*(t_pl/(t_pl+t_d)))+(c_d*(t_d/(t_d+t_pl)))

	# Desconto a valor futuro
	# TODO : montar o fluxo de caixa

	def fluxo_caixa_livre(c, j, t):
		fcl = recorrente_juros_compostos(c,j,t,plot=True)

		return fcl

	valor_da_empresa = list()

	fluxo_caixa_livre = fluxo_caixa_livre(investimento, juros, tempo)

	for t in range(tempo):
		fcl = fluxo_caixa_livre[t]
		vde = fcl/((1+taxa_min_atratividade)**t)
		valor_da_empresa.append(vde)

	valor_da_empresa = sum(valor_da_empresa)
	print(valor_da_empresa)




if __name__ == '__main__':
	#recorrente_juros_compostos(1000, 11.95, 10, plot=True)
	fluxo_caixa_descontado(1,1,1,1,1000,20,20)
