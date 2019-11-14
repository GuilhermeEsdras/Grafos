from Roteiro7.Roteiro7__funcoes import GrafoComPesos

mapa = GrafoComPesos(
    ['1',  '2',   '3', '4',  '5',  '6',  '7',  '8',  '9', '10',
     '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
     '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
     '31', '32', '33'],
    {
        '1-2': 1, '1-3': 1, '1-4': 1,
        '2-5': 1, '2-9': 1,
        '3-7': 1,
        '4-3': 1, '4-8': 1,
        '5-6': 1,
        '6-2': 1, '6-10': 1,
        '7-6': 1, '7-10': 1, '7-11': 1,
        '8-7': 1, '8-12': 1,
        '9-13': 1,
        '10-9': 1, '10-14': 1,
        '11-15': 1,
        '12-16': 1,
        '13-17': 1, '13-19': 1,
        '14-18': 1, '14-19': 1, '14-20': 1,
        '15-19': 1,
        '16-20': 1,
        '17-21': 1,
        '18-17': 1, '18-22': 1,
        '19-18': 1, '19-24': 1,
        '20-19': 1,
        '21-29': 1, '21-25': 1,
        '22-25': 1, '22-26': 1, '22-23': 1,
        '23-19': 1,
        '24-27': 1, '24-28': 1,
        '27-31': 1,
        '29-30': 1,
        '30-31': 1,
        '31-32': 1, '31-33': 1,
        '33-32': 1
    }
)
print(mapa.matriz_sem_pesos())