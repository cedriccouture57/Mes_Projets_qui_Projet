import arcade
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.color_b = 0
        self.color_g = 0
        self.color_r = 0
        self.y_random = 0
        self.x_random = 0
        self.cercles_list = []
        self.reset()

    def reset(self):
        for i in range(20):
            x_random = random.randint(15, 625)
            y_random = random.randint(15, 465)
            color_r = random.randint(0, 255)
            color_g = random.randint(0, 255)
            color_b = random.randint(0, 255)
            self.cercles_list.append([x_random, y_random, 15, (color_r, color_g, color_b)])

    def on_update(self):
        cercle_change_x = 3
        cercle_change_y = 3
        for circle in self.cercles_list:
            circle[0] += cercle_change_x
            circle[1] += cercle_change_y

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.csscolor.ALICE_BLUE)
        for circle in self.cercles_list:
            arcade.draw_circle_filled(circle[0], circle[1], circle[2], circle[3])


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
