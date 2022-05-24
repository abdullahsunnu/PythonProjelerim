import numpy as np


numbers = np.array([5,6,4,1,2,3,8,9,7,5,50,55,66,70])

resuult = numbers[5] # 5 inçi indexteki sayıyı verir
resuult = numbers[-1] # en son indexteki sayıyı verir
resuult = numbers[0:3] # 0 dan başlar üçünçü indexse kadar olan sayıları verir
resuult = numbers[:5] # en baştan yani 0 dan başlar 5 e kadar olan sayıları verir
resuult = numbers[2:5] # 2 den başlar 5 e kadar olan sayıları verir
resuult = numbers[::] # bütün sayıları verir yani 0 dan başlar en sonki sayıya kadar hepsini verir
resuult = numbers[::-2] # listenin sayılarını 2 atlayarak hepsini alır


numbers2 = np.array([[5,6,4],[1,2,3,8],[9,7,5,50],[55,66,70]])
# resuult = numbers2[0,2]
# resuult = numbers2[2,2]

arr1 = np.arange(0,10)

arr2 = arr1.copy() # copy dersek referans almaz ayrı bir yerden belleğe kaydeder yapılan değişikşlikler aynı olmaz.

arr2[0] = 20

print(arr1)
print(arr2)
# print(resuult)