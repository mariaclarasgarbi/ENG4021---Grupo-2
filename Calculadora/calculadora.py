import soma
import subtracao
import multiplicacao
import divisao

aux=int(input("Informe a operação desejada:\n1-Soma\n2-Subtracao\n3-Multiplicacao\n4-Divisao\n"))
if(aux==1):
    resultado=int(soma.soma())
    print(f"Resultado: {resultado}")
elif(aux==2):
    resultado=int(subtracao.subtracao())
    print(f"Resultado: {resultado}")
elif(aux==3):
    resultado=int(multiplicacao.multiplicacao())
    print(f"Resultado: {resultado}")
elif(aux==4):
    resultado=int(divisao.divisao())
    print(f"Resultado: {resultado}")






