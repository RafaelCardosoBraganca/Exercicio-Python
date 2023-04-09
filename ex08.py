#ler uma medida em metros e informar seu valor em km, hm, dam, dm, cm, mm
m=float(input('Informe alguma distância em metros: '))
km= m/1000
hm= m/100
dam= m/10
dm= m*10
cm= m*100
mm= m*1000
print('São {}m que equivalem à:'.format(m))
print('{} km\n{} hm\n{} dam\n{} dc\n{} cm\n{} mm'.format(km, hm, dam, dm, cm, mm))

