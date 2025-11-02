combos = int(input())
Pa, Pb, Pc = map(int, input().split())

tipos_damage = []

for i in range(combos):
    s = input()
    dmg = s.count("A") * Pa + s.count("B") * Pb + s.count("C") * Pc
    tipos_damage.append(dmg)
print(*tipos_damage, sep = "\n")  


  
