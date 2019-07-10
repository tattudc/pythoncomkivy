# **args
def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')

def resultado_f2(primeiro, segundo, terceiro):
    print(f'1) {primeiro}')
    print(f'2) {segundo}')
    print(f'3) {terceiro}')

if __name__=='__main__':
    resultado_f1(primeiro='L.Hamilton', segundo='M.Vestapen', terceiro='S. Vettel')
    resultado_f2(primeiro='S.Vettel', segundo='M.Vestapen', terceiro='L.Hamilton')