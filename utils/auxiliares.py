def verificar_login_crush(login, lista_crush):
    for crush in lista_crush:
        if login == crush[4]:
            return True

    return False


def fazer_login_crush(login, senha, lista_crush):
    for crush in lista_crush:
        if login == crush[4] and senha == crush[5]:
            return True

    return False
