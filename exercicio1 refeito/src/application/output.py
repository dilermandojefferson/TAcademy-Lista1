def mostra_resultado(salariobruto:float,valores_desconto):
    print(f'Seu salário brunto é de : {salariobruto}')
    print(f'Você pagou {valores_desconto.desconto_ir} de imposto de renda')
    print(f'Você pagou {valores_desconto.desconto_inss} para o INSS')
    print(f'Você pagou {valores_desconto.desconto_sindicato} para o sindicato')
    print(f'seu salario liquido é de: {valores_desconto.salario_liquido}')
