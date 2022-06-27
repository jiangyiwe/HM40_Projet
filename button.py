import pygame
#button class
class button():
	def __init__(self, x, y, image1,image2, scale, bruitage,volume):
		width1 = image1.get_width()
		height1 = image1.get_height()
		width2 = image1.get_width()
		height2 = image1.get_height()
		self.bruitage = bruitage
		self.craque = pygame.mixer.Sound("son/OS.wav")
		self.volume = volume
		self.image1 = pygame.transform.scale(image1, (int(width1 * scale), int(height1 * scale)))
		self.image2 = pygame.transform.scale(image2, (int(width2 * scale), int(height2 * scale)))
		self.rect1 = self.image1.get_rect()
		self.rect1.topleft = (x, y)
		self.rect2 = self.image2.get_rect()
		self.rect2.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()



		#check mouseover and clicked conditions
		if self.rect1.collidepoint(pos):


			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
				if self.bruitage :
					self.craque.set_volume(self.volume)
					self.craque.play()

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
			action = False

		#draw button on screen
		if  self.rect1.collidepoint(pos):
			surface.blit(self.image2, (self.rect2.x, self.rect2.y))
		else :
			surface.blit(self.image1, (self.rect1.x, self.rect1.y))

		return action


		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

