#
# Transformar de decimal a binario
#
#Solicitud de dato por teclado
n_Valor = input('íngrese numero : ')
n_Valor = int(n_Valor)
#Tansforma un valor entero a binario
b_Valor = bin(n_Valor)

print('El valor Binario de ', n_Valor, ' es ', b_Valor, '\n')
print('El valor es', format(14, 'b'))
