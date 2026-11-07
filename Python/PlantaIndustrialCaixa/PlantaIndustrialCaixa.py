# 3. Uma planta industrial precisa monitorar caixas d'água e reservatórios químicos para
# evitar transbordamento ou funcionamento de bombas a seco.
# i. Crie uma classe chamada Reservatorio que controle o nível de fluido de forma
# estritamente segura.
# ii. Na próxima página tem as restrições/passo-a-passo.
# i. O construtor deve receber a identificacao (ex: "Tanque-A"), a capacidade_maxima em
# litros e o nivel_inicial (padrão zero).
# ii. O atributo capacidade_maxima deve ser protegido e acessível apenas para leitura via
# @property (não deve ser alterado após a construção).
# iii. O atributo nivel_atual deve ser protegido (_nivel_atual) e possuir @property e
# @nivel_atual.setter. O setter deve garantir que o volume nunca fique abaixo de zero e
# nunca ultrapasse a capacidade_maxima.
# iv. Crie uma propriedade somente-leitura chamada porcentagem_ocupada que retorne o
# percentual atual de preenchimento do tanque (de 0 a 100%).
# v. Crie uma propriedade booleana alerta_nivel_baixo que retorne True se a ocupação
# estiver abaixo de 20%, e False caso contrário.
# vi. Implemente os métodos abastecer(litros) e consumir(litros) retornando True se a
# operação for concluída com sucesso ou False se a operação for rejeitada por limites
# físicos.