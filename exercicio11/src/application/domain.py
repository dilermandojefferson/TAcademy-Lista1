def verificacao(entrada):

    entrada_salva=[]

    for i in entrada:

        if (i =="(") and (")" in entrada_salva):
            entrada_salva.remove(")")

        elif  i =="(": 
            entrada_salva.append("(")
  

        if (i ==")") and ("(" in entrada_salva):
            entrada_salva.remove("(")
                
        elif  i ==")":  
            entrada_salva.append(")")
#_______________________________________
                
        if (i =="[") and ("]" in entrada_salva):
            entrada_salva.remove("]")

        elif  i =="[": 
            entrada_salva.append("[")
  

        if (i =="]") and ("[" in entrada_salva):
            entrada_salva.remove("[")
                
        elif  i =="]":  
            entrada_salva.append("]")     
#_______________________________________

        if (i =="{") and ("}" in entrada_salva):
            entrada_salva.remove("}")

        elif  i =="{": 
            entrada_salva.append("{")
  

        if (i =="}") and ("{" in entrada_salva):
            entrada_salva.remove("{")
                
        elif  i =="}":  
            entrada_salva.append("}") 

    return entrada_salva            





""" def simples():

    padrao = ["{}",'[]','()']
    entrada = input('Digite o seu separador matemático')
    for i in padrao:
        if entrada == i:
            print ('é um separador matemático')
            exit()
        
    print('Não e um separador matemático')     
 """

""" def complexo():
    entrada = str(input('Digite o seu separador matemático'))
    aberto = 0
    fechado = 0
    for i in entrada:
        if (i == '(') or (i == '[') or (i == '{'):
            aberto += 1
        elif (i == ')') or (i == ']') or (i == '{'):
            fechado -= 1          
  

    if aberto - fechado == 0:
        print('sua entrada esta correta')     
    else:        
        print('sua entrada esta incorreta') 
 """

   




            

