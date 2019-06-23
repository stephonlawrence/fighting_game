from ecs import Component, Entity

class Health(Component):
  defaults = dict([('current', 100), ('max', 100)])

  @property
  def alive(self):
    return self.current > 0

class Damage(Component):
  defaults = dict([('normal', 10), ('critical', 15), ('critical_percent', 10)])

  def __call__(self):
    '''
    returns a damage calculation based on the properties of the component
    
    '''
    crit = randint(0, 99) <= (self.critical_percent - 1)
    damage = self.normal
    if crit:
      damage = self.critical
    return damage



def main():
  player = Entity('player')
  enemy = Entity('enemy')

  player.health = Health(player)

  print(repr(player.health))

if __name__ == "__main__":
    main()
  