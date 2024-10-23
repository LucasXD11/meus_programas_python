def calcular_idade_em_anos_meses_dias(dias):
    anos = dias // 365
    dias_restantes = dias % 365
    meses = dias_restantes // 30
    dias_restantes = dias_restantes % 30
    return anos, meses, dias_restantes

dias = int(input("Digite sua idade em dias: "))
anos, meses, dias = calcular_idade_em_anos_meses_dias(dias)
print(f"Você tem {anos} anos, {meses} meses e {dias} dias.")
