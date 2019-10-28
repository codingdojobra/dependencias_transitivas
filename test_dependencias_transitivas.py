import unittest
def remover_duplicidades(atual, nova):
    for i in nova:
        if i not in atual:
            atual += i

    return atual
def gera_dependencias(dependencias):
    dependencia_total = {}
    for i in dependencias:
        raiz = i[0]
        dependencia_total[raiz] = i[1:]

    for linha_de_dependencia in dependencias:
        for i in range(1, len(linha_de_dependencia)):
            raiz = linha_de_dependencia[0]
            classe = linha_de_dependencia[i]
            if classe in dependencia_total.keys():
                dependencias_da_classe = dependencia_total[classe]
                dependencia_total[raiz] = remover_duplicidades(
                    dependencia_total[raiz],
                    dependencias_da_classe
                )
                dependencia_total[raiz] = ''.join(sorted(dependencia_total[raiz]))

    for linha in dependencia_total.items():
        raiz = linha[0]
        linha_de_dependencia = linha[1]
        for i in range(0, len(linha_de_dependencia)):
            classe = linha_de_dependencia[i]
            if classe in dependencia_total.keys():
                dependencias_da_classe = dependencia_total[classe]
                dependencia_total[raiz] = remover_duplicidades(
                    dependencia_total[raiz],
                    dependencias_da_classe
                )
                dependencia_total[raiz] = ''.join(sorted(dependencia_total[raiz]))

    return dependencia_total

class TestDependenciasTransitivas(unittest.TestCase):
    def test_framework(self):
        self.assertTrue(True)

    def test_E_F(self):
        entrada = ['EF', 'FH']
        esperado = {
            'E': 'FH',
            'F': 'H'
        }
        self.assertEqual(esperado, gera_dependencias(entrada))

    def test_A_C(self):
        entrada = ['ABC', 'CG']
        esperado = {
            'A': 'BCG',
            'C': 'G'
        }
        self.assertEqual(esperado, gera_dependencias(entrada))

    def test_geral(self):
        entrada = [
            'ABC',
            'BCE',
            'CG',
            'DAF',
            'EF',
            'FH',
        ]
        esperado = {
            'A': 'BCEFGH',
            'B': 'CEFGH',
            'C': 'G',
            'D': 'ABCEFGH',
            'E': 'FH',
            'F': 'H'
        }
        self.assertEqual(esperado, gera_dependencias(entrada))

if __name__ == '__main__':
    unittest.main()
