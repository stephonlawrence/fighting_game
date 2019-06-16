import pygame
import os
import pygame.time as ptime
import pygame.image as pimage
import pygame.sprite as psprite


def load_image(path: str):
  return pimage.load(os.path.join(os.getcwd(), path))

class LoopingAnimation(psprite.Sprite):
  def __init__(self, frames):
    psprite.Sprite.__init__(self).__init__(self)
    self.frames = frames
    self.current_frame = 0
    self.image = frames[0]
    self.rect = self.image.get_rect()
    self.playing = False
  
  def update(self, *args):
    if self.playing:
      self.current_frame += 1
      self.current_frame %= len(self.frames)
      self.image = self.frames[self.current_frame]
      self.rect = self.image.get_rect(center=self.rect.center)

  def start(self):
    self.playing = True
  
  def stop(self):
    self.playing = False
    self.current_frame = 0
    self.image = frames[0]
    self.rect = self.image.get_rect()
  
  def pause(self):
    self.playing = False

def update_render(screen):
  pygame.display.flip()


def main():
  pygame.init()

  pygame.display.set_caption("First Game")

  screen_width = 1000
  screen_height = 800

  screen = pygame.display.set_mode((screen_width, screen_height))

  running = True

  images = [
    "img_seq/run-cycle-inked2_xcf-Frame_01__100ms___replace_.png",
    "img_seq/run-cycle-inked2_xcf-Frame_02__100ms___replace_.png",
    "img_seq/run-cycle-inked2_xcf-Frame_03__100ms___replace_.png",
    "img_seq/run-cycle-inked2_xcf-Frame_04__100ms___replace_.png",
    "img_seq/run-cycle-inked2_xcf-Frame_05__100ms___replace_.png",
    "img_seq/run-cycle-inked2_xcf-Frame_06__100ms___replace_.png",
    "img_seq/run-cycle-inked2_xcf-Frame_07__100ms___replace_.png",
    "img_seq/run-cycle-inked2_xcf-Frame_08__100ms___replace_.png",
    "img_seq/run-cycle-inked2_xcf-Frame_09__100ms___replace_.png",
    "img_seq/run-cycle-inked2_xcf-Frame_10__100ms___replace_.png",
    "img_seq/run-cycle-inked2_xcf-Frame_11__100ms___replace_.png",
    "img_seq/run-cycle-inked2_xcf-Frame_12__100ms___replace_.png"
  ]

  player = LoopingAnimation([load_image(path) for path in images])

  # image = pimage.load(os.path.join(os.getcwd(), "img_seq", "run-cycle-inked2_xcf-Frame_01__100ms___replace_.png"))
  # image.set_colorkey((255, 0, 255))
  player.start()
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    screen.fill((0, 0, 0))

    image_width, image_height = player.image.get_rect().size
    x = (screen_width / 2) - (image_width / 2)
    y = (screen_height / 2) - (image_height / 2)
    screen.blit(player.image, (x, y))
    update_render(screen)
    player.update()
    

if __name__ == "__main__":
  main()
