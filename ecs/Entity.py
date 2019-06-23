from uuid import uuid4, UUID
# import ecs


class Entity(object):
  """
  >>> e = Entity('player', 0)
  >>> e
  <Entity player:0>
  >>> print e
  {}
  >>> e.health = 1
  >>> print e.health
  1
  >>> print e['health']
  1
  >>> e.health = 10
  >>> e.health
  10
  """


  __slots__ = ['uid', 'name', 'components']
  def __init__(self, name: str=None, uid: UUID=None):
    self.name = name
    self.uid = uuid4() if uid is None else uid
    self.components = dict()

  def __repr__(self):
    cname = self.__class__.__name__
    name = self.name or self.uid
    if name != self.uid:
      name = '{} {}'.format(name, self.uid)
    return '<{} {}>'.format(cname, name)

  def __str__(self):
    ''' {collection of the components} '''
    if len(self.components) == 0:
      return '{}'
    return '{'+ ' {} '.format(', '.join(self.components.keys())) +'}'

  def __getitem__(self, key):
    ''' e['key'] '''
    return self.components[key]

  def __setitem__(self, key, value):
    ''' e['key'] = value '''
    self.components[key] = value

  def __getattr__(self, key):
    ''' e.key '''
    if key in super(Entity, self).__getattribute__('__slots__'):
      return super(Entity, self).__getattr__(key)
    return self.components[key]
  
  def __setattr__(self, key, value):
    ''' e.key = value '''
    Component = __import__("ecs.Component").Component
    if key in super(Entity, self).__getattribute__('__slots__'):
      super(Entity, self).__setattr__(key, value)
    else:
      if isinstance(value, Component):
        v: Component = value
        vCatalog = v.__class__.ComponentCatalog
        if v.entity is None:
          v.entity = self
          for entity, comp in vCatalog.items():
            if comp == v:
              if self not in vCatalog:
                vCatalog.pop(entity)
                for relationship_name, component in entity.components:
                  if component == value:
                    entity.components.pop(relationship_name)
                    break
              vCatalog[self] = v
      self.components[key] = value
