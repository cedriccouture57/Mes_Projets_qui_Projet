"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import cursorbox
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_TITLE = "Rx7"


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """
    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.BABY_BLUE

        # If you have sprite lists, you should create them here,
        # and set them to None

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_mouse_motion(self, x: float, y: float, var1, var2):
        cursorbox.mouseX = x
        cursorbox.mouseY = y

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        #
        arcade.draw_line(44,223 ,60,230 ,arcade.csscolor.BLACK ,1)
        arcade.draw_line(44, 223, 44, 210, arcade.csscolor.BLACK, 1)
        arcade.draw_line(44, 210, 63, 207, arcade.csscolor.BLACK, 1)

        arcade.draw_line(63, 207, 133, 204, arcade.csscolor.BLACK, 1)
        arcade.draw_line(124, 211, 165, 186, arcade.csscolor.BLACK, 1)
        arcade.draw_line(124, 211, 90, 213, arcade.csscolor.BLACK, 1)

        arcade.draw_line(165, 186, 178, 185, arcade.csscolor.BLACK, 1)
        arcade.draw_line(178, 185, 150, 185, arcade.csscolor.BLACK, 1)
        arcade.draw_arc_outline(150 ,181 ,9 , 40 ,arcade.csscolor.BLACK,180,360, 2,tilt_angle=89 )
        arcade.draw_arc_filled(150, 181, 8, 39, arcade.csscolor.WHITE_SMOKE, 180, 360, tilt_angle=89)

        arcade.draw_line(150, 177, 245, 180, arcade.csscolor.BLACK, 1)

        arcade.draw_line(165, 186, 210, 188, arcade.csscolor.BLACK, 1)
        arcade.draw_line(210, 188, 272, 218, arcade.csscolor.BLACK, 1)
        arcade.draw_line(230, 197, 248, 195, arcade.csscolor.BLACK, 1)

        arcade.draw_line(248, 195, 252, 191, arcade.csscolor.BLACK, 1)
        arcade.draw_line(244, 188, 150, 185, arcade.csscolor.BLACK, 1)

        arcade.draw_arc_outline(244, 184, 9, 40, arcade.csscolor.BLACK, 180, 360, 2, tilt_angle=269)
        arcade.draw_arc_filled(244, 184, 8, 39, arcade.csscolor.WHITE_SMOKE, 180, 360, tilt_angle=269)
        arcade.draw_line(252, 191, 246, 189, arcade.csscolor.BLACK, 1)
        arcade.draw_line(245, 205, 258, 205, arcade.csscolor.BLACK, 1)
        arcade.draw_line(258, 205, 261, 201, arcade.csscolor.BLACK, 1)
        arcade.draw_lines([(270,218),(328,216)], arcade.color.BLACK, 1)
        arcade.draw_lines([(328,216 ), (324,214) ], arcade.color.BLACK, 1)

        arcade.draw_lines([(324,214 ), (272,211)], arcade.color.BLACK, 1)
        arcade.draw_lines([(252,205 ), (272,212 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(267,210 ), (271,205 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(271,205 ), (300,207 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(300,207 ), (310,213 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(260,201 ), (232,199 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(328,216 ), (331,219)], arcade.color.BLACK, 1)
        arcade.draw_lines([(331,217 ), (372,219 )], arcade.color.BLACK, 1)

        arcade.draw_arc_outline(350,227,19,100,arcade.csscolor.BLACK,20, 180, 2, 90, 20)
        arcade.draw_lrbt_rectangle_filled(274,430,226 ,400 ,arcade.color.BABY_BLUE)
        arcade.draw_arc_outline(350, 222, 16, 90, arcade.csscolor.BLACK, 20, 180, 2, 90, 20)



        arcade.draw_lines([(373,234 ), (368,236 )], arcade.color.BLACK, 1)





        #Suite
        arcade.draw_lines([(60,229 ), (70,231 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(70,231 ), (73,271 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(74, 271), (68,273 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(68,273 ), (68,275 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(68, 275), (74,277 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(73,277 ), (71,292 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(71,292 ), (90,294 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(90,294 ), (107,281 )], arcade.color.BLACK, 1)






        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.

        #

        cursorbox.draw_information()
    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass


    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()



if __name__ == "__main__":
    main()