inicio = int(input("Digite 1 para abri aplicativo\n2 Para sair do aplicativo.\n"))

lista_tarefas=[]

while inicio == 1:

    pergunta = int(input('O que deseja fazer ? \n1 Para adicionar uma ou mais tarefas: \n2 Para mostrar as tarefas: \n3 Para editar as tarefas:\n4 Para salvar a lista de tarefas: \n5 Para sair:\n '))

    if pergunta ==1:
        quantidade = int(input('Informe quantas tarefas deseja adicionar ?\n '))
        for x in range (1, quantidade+1 ):
            tarefa = input('Qual tarefa deseja adicionar ? \n').title()
            lista_tarefas.append(tarefa)

    elif pergunta ==2:
        print(lista_tarefas)

    elif pergunta == 3:
        editar = int(input('O que deseja editar ?\n1 Para remover uma tarefa\n2 Para trocar uma tarefa\n3 Para remover todas tarefas\n4 para voltar inicio\n'))

        if editar == 1:       
            try:     
                lista_tarefas.remove(input('Qual tarefa deseja remover ?\n').title())
            except:
                print('Tarefa não encontrada')

        elif editar == 2:
            
            tarefa_antiga = input('Informe qual tarefa deseja substituir ? \n').title()
            tarefa_nova = input('Informe a tarefa nova ? \n').title()
            lista_tarefas = list(map(lambda x: x.replace(tarefa_antiga, tarefa_nova), lista_tarefas))   
                    
        elif editar == 3:
            lista_tarefas.clear()
        else:
            print('Voltando ao inicio')

    elif pergunta ==4:
        lista_numerada = []
        for indice, x in enumerate(lista_tarefas, start=1):
            lista_numerada.append(f'Tarefa {indice}, {x}')

        f = open("lista de tarefas", "w")
        f.write(str(lista_numerada))
        f.close()

    else:
        print ('Adeus')
        break


    


