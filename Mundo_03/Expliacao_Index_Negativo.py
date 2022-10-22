lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Milk Shake')
print(lanche)
print()

# Pedi pra começar no índice 1 e ir até até,
# mas não vai contar o 3 em python, vai até o penúltimo,
# logo 2.
print(lanche[1:3])  # Output: Suco, Pizza
print()

# Defini o início, mas não o final,
# logo vai mostrar tudo a partir do início definido
print(lanche[1:])
print()

# Vai começar do início, mas não vai mostrar o último no caso,
# -1, mas pode ser os 2 último -2 e assim por diante.
print(lanche[:-1])
print()

# Estou pedindo para pegar o último elemento,
# indo de traz pra frente, se for o -2, será o penúltimo
"""
Importante!!
Se eu peço de traz pra frente o index começa em -1,
mas se eu peço na ordem comum o index começa em 0.
"""
print(lanche[:-1])
print()

# Se eu quero uma lista inversa, começando o último até o início,
# pois não foi definido o fim
print(lanche[::-1])
print()


"""
('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Milk Shake')
    0            1       2        3        4
    -5          -4      -3       -2       -1
  Sintaxe: start : end : step
  por padrão step é 1, mesmo se não for declarado
  Quando colocamos -1 é a mesma coisa que ir de um em um, só muda a direção.
  
  lanche[-1:2:-1]
  -1 de traz pra frente, primeiro item (Milk Shake)
  2 até o item 2, que deveria ser até o item 2, mas como em python vai até o penúltimo ele vai até Pudim
  -1 de 1 em 1  de traz pra frente.

"""
print()
print(lanche[-1:2:-1])


