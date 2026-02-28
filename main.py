from Enemigo import *
from Zoombie import *
from ogro import * # type: ignore

zombie = zombie(10, 1) # type: ignore
ogro = ogro(20, 3) # type: ignore

print("===============================")
print(f" {zombie.get_tipo_enemigo()} tiene {zombie.puntos_energia} de energia y puede hacer ataques de {zombie.ataque}")
print(f"{zombie.habla()}")
print(f"{ogro.get_tipo_enemigo()} tiene {ogro.puntos_energia} de energia y puede hacer ataques de {ogro.ataque}")
print(f"{ogro.habla()}")
