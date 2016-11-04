import unittest
from diamond import diamond, affiche_ligne, indice_lettre


class TestAfficheLigne(unittest.TestCase):

    def test_when_a_return_centered_a(self):
        lettre = 'c'
        lettre_courante = 'a'
        lettre_remplissage = '-'
        largeur_ligne = indice_lettre(lettre) * 2 - 1
        nb_espaces = indice_lettre(lettre) - 1 - (indice_lettre(lettre) - indice_lettre(lettre_courante))
        result = affiche_ligne(lettre, nb_espaces, lettre_courante, largeur_ligne, lettre_remplissage)
        self.assertEquals(result, '  a  \n')

    def test_when_c_return_c_without_starting_spaces(self):
        lettre = 'c'
        lettre_courante = 'c'
        lettre_remplissage = '-'
        largeur_ligne = indice_lettre(lettre) * 2 - 1
        nb_espaces = indice_lettre(lettre) - 1 - (indice_lettre(lettre) - indice_lettre(lettre_courante))
        result = affiche_ligne(lettre, nb_espaces, lettre_courante, largeur_ligne, lettre_remplissage)
        self.assertEquals(result, 'c---c\n')

    def test_when_b_return_b_with_starting_spaces(self):
        lettre = 'c'
        lettre_courante = 'b'
        lettre_remplissage = '-'
        largeur_ligne = indice_lettre(lettre) * 2 - 1
        nb_espaces = indice_lettre(lettre) - 1 - (indice_lettre(lettre) - indice_lettre(lettre_courante))
        result = affiche_ligne(lettre, nb_espaces, lettre_courante, largeur_ligne, lettre_remplissage)
        self.assertEquals(result, ' b-b \n')


class TestDiamond(unittest.TestCase):

    def test_when_a_return_a(self):
        params = 'a'
        result = diamond(params)
        self.assertEquals(result, 'a\n')

    def test_when_c_return_diamond(self):
        params = 'c'
        result = diamond(params)
        self.assertEquals(result, '  a  \n b b \nc   c\n b b \n  a  \n')


class TestIndiceLettre(unittest.TestCase):

    def test_when_a_return_1(self):
        params = 'a'
        result = indice_lettre(params)
        self.assertEquals(result, 1)

    def test_when_A_return_1(self):
        params = 'A'
        result = indice_lettre(params)
        self.assertEquals(result, 1)

    def test_when_b_return_2(self):
        params = 'b'
        result = indice_lettre(params)
        self.assertEquals(result, 2)

    def test_when_z_return_1(self):
        params = 'z'
        result = indice_lettre(params)
        self.assertEquals(result, 26)


if __name__ == '__main__':
    unittest.main()
