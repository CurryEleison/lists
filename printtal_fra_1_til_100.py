#4: Skriv alle primtal mellem 1 og 100
for primtal in range(2, 101):
   for i in range(2, primtal):
       if (primtal % i) == 0:
           break
   else:
       print(primtal)
