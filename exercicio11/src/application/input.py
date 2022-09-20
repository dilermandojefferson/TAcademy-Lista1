def complexo2():
    entrada = []
    while True:       
        inicio = str(input('Digite o seu separador matemático:   ')) 
        for i in inicio:
            if (i =='(') or (i =='[') or (i =='{') or (i ==')') or (i ==']')or (i =='}'):
                entrada.append(i)
            else:    
                print('Entrada invalida')
                entrada.clear()
                break
        if len(entrada) > 0:
            break
            
        else:
            continue
        
    return entrada
        

                    
        
    
