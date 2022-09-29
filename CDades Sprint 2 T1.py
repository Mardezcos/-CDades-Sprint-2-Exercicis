#!/usr/bin/env python
# coding: utf-8

# # CDades - Sprint 2
# ## Tasca 1 - Exercici 1

# In[ ]:


# Creo una lista con los meses del año


# In[96]:


lista_meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
print(lista_meses)


# In[99]:


# Creo las listas de los trimestres
for i in range(len(lista_meses)):
 if i < 3: list_1T.append(lista_meses[i])
 elif 3<= i < 6: list_2T.append(lista_meses[i])
 elif 6<= i < 9: list_3T.append(lista_meses[i])
 elif 9<= i < 12: list_4T.append(lista_meses[i])
print(list_1T)
print(list_2T)
print(list_3T)
print(list_4T)


# In[100]:


#Creo las lista que agrupa los meses del año en listas por trimestres
lista_trimestres=([list_1T]+[list_2T]+[list_3T]+[list_4T])
print(lista_trimestres)


# ## Tasca 1 - Exercici 2

# In[101]:


#Código para acceder al segundo mes del primer trimestre
segonMes1T=(lista_trimestres[0])[1]
print(segonMes1T)


# In[102]:


#Código para acceder a los meses del primer trimestre

#Los muestro juntos en la lista del trimestre
meses_1T=lista_trimestres[0]
print(meses_1T)


# In[103]:


#Los muestro de uno en uno
enero=(lista_trimestres[0])[0]
febrero=(lista_trimestres[0])[1]
marzo=(lista_trimestres[0])[2]
print(enero)
print(febrero)
print(marzo)


# In[104]:


#Código para acceder a septiembre y octubre
#Los muestro por separado
sep=(lista_trimestres[2])[2]
oct=(lista_trimestres[3])[0]
print(sep)
print(oct)


# In[105]:


#Los muestro concatenados
sepYOct=(lista_trimestres[2])[2] + ' y ' + (lista_trimestres[3])[0]
print(sepYOct)


# ## Tasca 1 - Exercici 3

# In[111]:


# Creo una lista con números desordenados
numeros=[6,22,76,98,4,87,25,35]
print(numeros)


# In[112]:


# ¿Cuántos números hay?
print(len(numeros))


# In[109]:


# ¿Cuántas veces aparece el número 3?
print(numeros.count(3))


# In[122]:


# ¿Cuántas veces aparece el número 3 y 4?
if numeros.count(3) and numeros.count(4): 
    print('Los números 3 y 4 aparecen ' + str(numeros.count(3)+numeros.count(4)) + ' veces entre los dos')
elif numeros.count(3) or numeros.count(4): 
    print('El número 3 aparece ' + str(numeros.count(3)) + ' veces y el número 4 aparece ' + str(numeros.count(4)) + ' veces')
else:
    print('Los números 3 y 4 no aparecen en ninguna ocasión')


# In[115]:


# ¿Cuál es el número más alto?
y=0
for x in numeros:
    if x>y:
        y=x
print(y)


# In[116]:


# ¿Cuáles son los tres números más pequeños?
# Ordeno la lista de manera ascendente
numeros.sort()
print(numeros)


# In[117]:


# Devuelvo los tres primeros elementos de la lista
print(numeros[:3])


# In[118]:


# ¿Cuál es el rango de la lista creada al inicio de la tarea?
print('El rango de esta lista es de 0 a ' + str(len(numeros)-1))


# ## Tasca 1 - Exercici 3

# In[23]:


# Creo un dicionario
compra = { "Pomes" : {"Qty": 0, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66} }
print(compra)


# In[24]:


# Añado una fruta
compra["Cireres"] = {"Qty" : 10, "€": 1.25}
print(compra)


# In[25]:


# Cuántas frutas he comprado
# Un método sería hacer un len(compra) puede haber cantidades a cero que indica que de esa fruta no se ha comprado nada
# Para hacer una comprobación de las cantidades compradas trabajo con los valores del diccionario
frutas = compra.values()
print(frutas)
numFrutas=0
for x in frutas:
    if x['Qty']>0: numFrutas+=1  # Compruebo de qué frutas hemos comprado realmente
print('Hemos comprado ' + str(numFrutas) + ' frutas')

