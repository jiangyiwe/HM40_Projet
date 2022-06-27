import pygame


def pointInRectanlge( px, py, rw, rh, rx, ry):
    if px > rx and px < rx + rw:
        if py > ry and py < ry + rh:
            return True
    return False
class Slider:
    def __init__(self, position: tuple, upperValue: int = 100, sliderWidth: int = 30, text: str = "", outlineSize: tuple = (200, 60)) -> None:
        self.position = position
        self.outlineSize = outlineSize
        self.text = text
        self.sliderWidth = sliderWidth
        self.upperValue = upperValue

    # returns the current value of the slider
    def getValue(self) -> float:
        return self.sliderWidth / (self.outlineSize[0] / self.upperValue)

    # renders slider and the text showing the value of the slider
    def render(self, display: pygame.display) -> None:
        # draw outline and slider rectangles

        pygame.draw.rect(display, (100, 100, 100), (self.position[0], self.position[1],
                                        self.sliderWidth, self.outlineSize[1]-5))

        pygame.draw.rect(display, (250, 250, 250), (self.position[0]+self.sliderWidth-5, self.position[1],
                                              5, self.outlineSize[1] - 5))

        pygame.draw.rect(display, (175, 175, 175), (self.position[0], self.position[1],
                                              self.outlineSize[0], self.outlineSize[1]), 3)

        # determite size of font
        self.font = pygame.font.Font(pygame.font.get_default_font(), int((30 / 100) * self.outlineSize[1]))

        # create text surface with value
        valueSurf = self.font.render(f"{self.text} {round(self.getValue())}", True, (0, 0, 0))

        # centre text
        textx = self.position[0] + (self.outlineSize[0] / 2) - (valueSurf.get_rect().width / 2)
        texty = self.position[1] + (self.outlineSize[1] / 2) - (valueSurf.get_rect().height / 2)

        display.blit(valueSurf, (textx, texty))

    # allows users to change value of the slider by dragging it.
    def changeValue(self) -> None:
        # If mouse is pressed and mouse is inside the slider
        mousePos = pygame.mouse.get_pos()
        if pointInRectanlge(mousePos[0], mousePos[1]
                , self.outlineSize[0], self.outlineSize[1], self.position[0], self.position[1]):
            if pygame.mouse.get_pressed()[0]:
                # the size of the slider
                self.sliderWidth = mousePos[0] - self.position[0]

                # limit the size of the slider
                if self.sliderWidth < 1:
                    self.sliderWidth = 0
                if self.sliderWidth > self.outlineSize[0]:
                    self.sliderWidth = self.outlineSize[0]

