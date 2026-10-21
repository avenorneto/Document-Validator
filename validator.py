
import re


def validar_cadastro(nome, email, cpf):
    erros = []

    # Verificar nome completo
    if len(nome.strip().split()) < 2:
        erros.append("Nome incompleto")

    # Verificar formato do e-mail
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        erros.append("E-mail invalido")

    # Verificar CPF
    cpf = re.sub(r"\D", "", cpf)

    if len(cpf) != 11 or len(set(cpf)) == 1:
        erros.append("CPF invalido")
    elif not verificar_digitos_cpf(cpf):
        erros.append("CPF invalido")

    return {
        "status": "APROVADO" if not erros else "REVISAR",
        "inconsistencias": erros
    }


def verificar_digitos_cpf(cpf):
    for tamanho in (9, 10):
        soma = sum(
            int(cpf[i]) * (tamanho + 1 - i)
            for i in range(tamanho)
        )
        digito = (soma * 10) % 11

        if digito == 10:
            digito = 0

        if digito != int(cpf[tamanho]):
            return False

    return True


# Exemplo com dados ficticios
resultado = validar_cadastro(
    "Maria Silva",
    "maria@exemplo.com",
    "123.456.789-09"
)

print(resultado)
