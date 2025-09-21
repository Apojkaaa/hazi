import math

# 3. feladat: 3-4-5 háromszög kerülete és területe
a3, b3, c3 = 3, 4, 5
k3 = a3 + b3 + c3
s3 = k3 / 2
t3 = math.sqrt(s3 * (s3 - a3) * (s3 - b3) * (s3 - c3))
print("3. feladat -> Kerület:", k3, "Terület:", t3)

# 4. feladat: szabályos háromszög magassága (a=6)
a4 = 6
m4 = (a4 * math.sqrt(3)) / 2
print("4. feladat -> Magasság:", m4)

# 5. feladat: kocka lapátlója és testátlója (a=2)
a5 = 2
lap_atlo = a5 * math.sqrt(2)
test_atlo = a5 * math.sqrt(3)
print("5. feladat -> Lapátló:", lap_atlo, "Testátló:", test_atlo)
