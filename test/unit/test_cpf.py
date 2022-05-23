import unittest

import pytest

from src.domain.entity.cpf import Cpf


class CpfTestCase(unittest.TestCase):
    def test_cpf_valido(self):
        cpf = Cpf('935.411.347-80')
        self.assertEqual(cpf.value, '935.411.347-80')

    def test_cpf_invalido_digitos_iguais(self):
        with pytest.raises(Exception) as e:
            Cpf('111.111.111-11')

        self.assertEqual(str(e.value), 'CPF inválido')

    def test_cpf_invalido_digitos_diferentes(self):
        with pytest.raises(Exception) as e:
            Cpf('123.456.789-99')

        self.assertEqual(str(e.value), 'CPF inválido')


if __name__ == '__main__':
    unittest.main()
