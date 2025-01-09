# Código para escrever texto na cor teal no terminal
def write_teal(text):
    # teal = '\033[36m'  # Código ANSI para a cor vermelho sangue
    # reset = '\033[0m'  # Código ANSI para resetar as cores
    print(f"{teal}{text}{reset}")

# Testando a função
write_teal("Este texto é para a branch Blue! - GitFlow")