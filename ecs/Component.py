from random import randint
import sys
import ecs
import json

class Component(object):
  __slots__ = ['entity', 'defaults']
  # defaults = dict()
  ComponentCatalog = dict()
  ComponentTypes = dict()

  def __new__(cls, entity=None, **properties):
    cname = cls.__name__
    print("cname", cname)
    if cname not in Component.ComponentTypes:
      Component.ComponentTypes[cname] = cls
      cls.ComponentCatalog = dict()
    if entity not in cls.ComponentCatalog:
      cls.ComponentCatalog[entity]
      component = Component.__new__(cls, entity=entity, **properties)
      # component = super(Component, cls).__new__(cls, entity=entity, **properties)
    else:
      component = cls.ComponentCatalog(entity)
    return component

  def __init__(self, entity: ecs.Entity=None, **properties):
    self.entity = entity

    for propery, value in self.defaults.items():
      setattr(self, propery, properties.get(propery, value))
    

  def __repr__(self):
    ''' <Component entity_id> '''
    cname = self.__class__.__name__
    ename = ''
    if self.entity:
      for propery, component in self.entity.components.items():
        if component == self:
          ename = ' entity:{}.{}'.format(self.entity.name, propery)
    return '<{}{}>'.format(cname, ename)

  def __getitem__(self, key):
    return getattr(self, key)

  def __setitem__(self, key, value):
    return setattr(self, key, value)

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
    keys = self.defaults.keys()
    data = dict()
    for key in keys:
      if key != 'defaults':
        data[key] = getattr(self, key)
    # strip off extra white space
    json_string = '\n'.join([line.rstrip() for line in json.dumps(data, indent=4)]).split('\n')
    return json_string
  def restart(self):
    for prop, value in self.defaults.items():
      setattr(self, prop, value)

