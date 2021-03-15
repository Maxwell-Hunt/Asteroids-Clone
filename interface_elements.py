from setup import *

class TickBox:
    outer_radius = 20
    inner_radius = 8

    def __init__(self, position_x : float, position_y : float, label = "", ticked = False):
        self.position = pygame.Vector2(position_x, position_y)
        self.ticked = ticked
        self.mouse_down = False
        self.label_text = TINY_FONT.render(label, True, (255, 255, 255))
    
    def update(self, delta_time : float):
        mouse_position = pygame.mouse.get_pos()
        if hypot(self.position.x-mouse_position[0], self.position.y-mouse_position[1]) < self.outer_radius:
            if pygame.mouse.get_pressed()[0]:
                self.mouse_down = True
            else:
                if self.mouse_down and not self.ticked:
                    self.ticked = True
                self.mouse_down = False


    def draw(self, screen : pygame.Surface):
        pygame.draw.circle(screen, (255, 255, 255), tuple(self.position), self.outer_radius)
        text_position = (self.position.x - self.label_text.get_width()/2, self.position.y - self.outer_radius - self.label_text.get_height())
        screen.blit(self.label_text, text_position)
        if self.ticked:
            pygame.draw.circle(screen, (0, 0, 0), tuple(self.position), self.inner_radius)


class TickList:

    def __init__(self, position_x : float, position_y : float, fields : List(str), selected = 0, spacing = 100):
        self.tick_boxes = []
        self.selected = selected
        for i, field in enumerate(fields):
            self.tick_boxes.append(TickBox(position_x + spacing * i, position_y, label = field, ticked = (self.selected==i)))

    def update(self, delta_time : float):
        for i, box in enumerate(self.tick_boxes):
            was_selected = box.ticked
            box.update(delta_time)
            if not was_selected and box.ticked:
                for j in range(len(self.tick_boxes)):
                    if i != j:
                        self.tick_boxes[j].ticked = False
                self.selected = i

    def draw(self, screen : pygame.Surface):
        for i, box in enumerate(self.tick_boxes):
            box.draw(screen)