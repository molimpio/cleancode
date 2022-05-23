import re


class Cpf:
    __factor_digit1 = 10
    __factor_digit2 = 11

    def __init__(self, value: str):
        if self.__validate(value) is False:
            raise Exception('CPF inválido')
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __validate(self, cpf: str):
        cpf = self._clean_cpf(cpf)

        if self._is_valid_length(cpf) is False:
            return False

        if self._has_all_digits_equal(cpf) is True:
            return False

        digit1 = self._calculate_check_digit(cpf, self.__factor_digit1)
        digit2 = self._calculate_check_digit(cpf, self.__factor_digit2)
        check_digit = self._extract_check_digit(cpf)
        calculate_digit = str(digit1) + str(digit2)
        return check_digit == calculate_digit

    @staticmethod
    def _clean_cpf(cpf: str) -> str:
        return ''.join(re.findall(r'\d+', cpf))

    @staticmethod
    def _is_valid_length(cpf: str) -> bool:
        return len(cpf) == 11

    @staticmethod
    def _has_all_digits_equal(cpf: str) -> bool:
        return all(digit == cpf[0] for digit in cpf)

    @staticmethod
    def _calculate_check_digit(cpf: str, factor: int) -> int:
        total = 0

        for digit in cpf:
            if factor > 1:
                total += int(digit) * factor
                factor = factor - 1

        resto = total % 11
        if resto < 2:
            return 0
        else:
            return 11 - resto

    @staticmethod
    def _extract_check_digit(cpf: str) -> str:
        return cpf[-2:]
