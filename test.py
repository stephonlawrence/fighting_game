from ecs.Component import Damage, Health
from ecs.Entity import Entity

def main():
  player = Entity('player')
  enemy = Entity('enemy')

  player.health = Health(player)
  player.damage = Damage(player)

  enemy.health = Health(enemy)

  print(repr(player), player.health)
  print(repr(enemy), enemy.health)
  enemy.health.current -= player.damage()
  print(repr(player), player.health)
  print(repr(enemy), enemy.health)
  enemy.health.current -= player.damage()
  print(repr(player), player.health)
  print(repr(enemy), enemy.health)

if __name__ == "__main__":
    main()
  