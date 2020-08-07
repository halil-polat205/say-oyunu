import random
import time
from oyun_modul import aralık

print( """
Sayı Tahmin Oyunu
Nasıl Oynanır:
Oyun sizden belirlenen aralıkta sayı tutmanızı ister. 
Doğru sayıyı bilirseniz oyunu kazanırsınız.
Not: Harf veya karakter girmemeye özen gösteriniz. 
""")

z = 0
x = random.randint(0,10)

while True:
	
	z+=1

	y= input("Değer giriniz: ")
	
	if y.isdigit() == False:
		print("Lütfen sayı değeri giriniz!!")

	elif y.isdigit() == True:
		y = int(y)

		if y>10:
			print("Lütfen 10 'dan küçük bir sayı giriniz!!")

		elif y<=10:

			if x==y:
				print("Winner Winner Chicken Dinner")
				print("{}.kezde bildiniz".format(z))
				aralık(z)
							
				a = input("tekrar oynamak ister misin?(E/H)")
							
				if a == "E" or a == "e":
					z = 0
					x = random.randint(0,10)

				elif a == "H" or a == "h":
					print("yine bekleriz:) \n çıkılıyor...")
					time.sleep(3)
					z=0
					quit()
					
				else:
					print("e/E ya da h/H")
					print("\a")
					quit()

			elif x<y:
				print("aşağı")

			elif x>y:
				print("yukarı")


			else:
					print("lütfen sayı giriniz!!")

		else:
			pass

	else:
		pass