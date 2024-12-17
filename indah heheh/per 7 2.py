nilai = 0


#input nilai

if nilai >= 86 and nilai <= 100:
    grade = 'A'
elif nilai >= 76 and nilai <= 85:
    grade = 'B'
elif nilai >= 61 and nilai <= 75:
    grade = 'C'
elif nilai >= 41 and nilai <= 60:
    grade = 'D'
else:
    grade = 'E'

print(f"Nilai Anda adalah: {grade}")
