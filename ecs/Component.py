from random import randint
import sys
from ecs.Entity import Entity
import json
class Component(object):
  __slots__ = ['entity', 'defaults', 'properties']

  def __init__(self, entity: Entity, **properties):
    self.entity = entity
    self.properties = dict(self.defaults)
    
    for key, value in properties.items():
      self.properties[key] = value
    

  def __repr__(self):
    ''' <Component entity_id> '''
    cname = self.__class__.__name__
    return '<{} {}>'.format(cname, self.entity.uid)

  def __getattr__(self, key):
    if key in super(Component, self).__getattribute__('__slots__'):
      return super(Component, self).__getattr__(key)
    return self.properties[key]

  def __setattr__(self, key, value):
    if key in super(Component, self).__getattribute__('__slots__'):
      super(Component, self).__setattr__(key, value)
    else:
      self.properties[key] = value

  def __str__(self):
    ''' json of properties '''
    return json.dumps(self.properties)

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

