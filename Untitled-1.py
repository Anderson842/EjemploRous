n = int(input("Ingrese el número de municipios: "))
votosc1 = 0
votosc2 = 0
total_votos = 0
print("\nIngrese los votos obtenidos en cada municipio por los candidatos:")
for i in range(n):
    print(f"Municipio {i + 1}:")
    c1 = int(input(f"  Votos para el candidato 1: "))
    c2 = int(input(f"  Votos para el candidato 2: "))

    votosc1 += c1
    votosc2 += c2

    total_votos += c1 + c2

    porcentaje_c1 = (votosc1 / total_votos) * 100
    porcentaje_c2 = (votosc2 / total_votos) * 100

    mas_votos = votosc1
    menos_votos = votosc1
    candidato_mas_votado = "Candidato 1"
    candidato_menos_votado = "Candidato 1"

    if votosc2 > mas_votos:
      mas_votos = votosc2
      candidato_mas_votado = "Candidato 2"
    if votosc2 < menos_votos:
      menos_votos = votosc2
      candidato_menos_votado = "Candidato 2"