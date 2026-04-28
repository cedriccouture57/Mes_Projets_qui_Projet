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

        ##couleur

        arcade.draw_polygon_filled([(43, 223), (60, 230), (63, 208), (44, 211)], arcade.color.LIGHT_GRAY)
        arcade.draw_polygon_filled([(67,276 ), (70,272 ), (117,280 ), (125,278 )], arcade.color.AERO_BLUE)
        arcade.draw_polygon_filled([(72,293 ), (90,293 ), (171,234 ), (71,231 )], arcade.color.BLUE_SAPPHIRE)
        arcade.draw_triangle_filled((374), (233),(400), (230) ,(374), (219), arcade.color.GRAY_BLUE)
        arcade.draw_arc_filled((386), (227), 65, 11, arcade.color.GRAY_BLUE, 0, 130, 170, 15)
        arcade.draw_arc_filled(369, 226, 61, 18, arcade.color.GRAY_BLUE, 0, 170, 0)
        arcade.draw_polygon_filled([(166,184 ), ( 209,186), (237,199 ), (193,209 ),(146,197)], arcade.color.GRAY_BLUE)

        arcade.draw_ellipse_outline(194,194,12,7,arcade.color.DARK_GRAY,1)

        arcade.draw_polygon_filled([(132,204 ), (147,197 ), (181,205 ), (152,216 ),(178,248),(140,234),(125,220),(144,207)], arcade.color.LIGHT_GRAY)
        arcade.draw_polygon_filled([(185,220 ), (194,208 ), (233,200 ), (272,217 ), (285,226 ), (254,225 ), (240,240 )],arcade.color.BLUE_SAPPHIRE)
        arcade.draw_polygon_filled([(150,185 ), (243,187 ), (243,180 ), (149,177 )],arcade.color.BLUE_SAPPHIRE)
        arcade.draw_line(212,187,221,186, arcade.color.BLUE_SAPPHIRE)
        arcade.draw_polygon_filled([(178,204 ), (194,209 ), (185,220 ), (257,246 ), (172,243 ), (152,216 )],arcade.color.LIGHT_CYAN)

        arcade.draw_polygon_filled([(367,239 ), (364,228 ), (346,220 ), (330,218 ), (325,214 ), (308,212),(283,219),(252,240)],arcade.color.LIGHT_CYAN)
        arcade.draw_polygon_filled([(255,224 ), (272,224 ), (255,241 ), (276,246 ), (252,246 ), (240,240 )],arcade.color.GRAY)

        arcade.draw_polygon_filled([(252,240 ), (300,239 ), (297,249 ), (275,247 )],arcade.color.BLUE_SAPPHIRE)
        arcade.draw_polygon_filled([(296,248), (317,252), (330,251), (356,239), (352,233), (342,233),(300,239)], arcade.color.DARK_SLATE_GRAY)
        arcade.draw_line(295,248,326,253,arcade.color.DARK_SLATE_GRAY)
        arcade.draw_line(319,252 ,331,250 , arcade.color.DARK_SLATE_GRAY,3)
        arcade.draw_line(330,251 ,349 ,241 , arcade.color.DARK_SLATE_GRAY,4)
        arcade.draw_line(341,249 ,352 ,241 , arcade.color.DARK_SLATE_GRAY,2)
        arcade.draw_line(298,240 ,339 ,233 , arcade.color.DARK_SLATE_GRAY,3)

        arcade.draw_line(296 ,248 ,299,239 , arcade.color.BLACK)

        arcade.draw_polygon_filled([(284,217 ), (334,217 ),(379,235) ,(347,234 )],arcade.color.BLUE_SAPPHIRE)

        arcade.draw_polygon_filled([(150,248), (172,248), (176,247), (150,239)], arcade.color.BLUE_SAPPHIRE)
        arcade.draw_polygon_filled([(62,230), (138,233), (124,220), (143,206),(134,206),(123,211),(62,212)], arcade.color.BLUE_SAPPHIRE)
        arcade.draw_polygon_filled([(63,213 ), (123,211 ), (131,205 ), (63,207)], arcade.color.LIGHT_CYAN)
        arcade.draw_polygon_filled([(247,206), (272,217), (297,218), (307,213),(299,207),(271,206),(267,210),(251,206)], arcade.color.LIGHT_CYAN)
        arcade.draw_polygon_filled([(243,205 ), (259,204 ), (259,200 ), (235,199 )], arcade.color.LIGHT_CYAN)
        arcade.draw_polygon_filled([(229,196 ), (246,195 ), (251,191 ), (242,188),(211,188)], arcade.color.LIGHT_CYAN)
        arcade.draw_point(106,280,arcade.color.BLUE_SAPPHIRE,1)
        arcade.draw_circle_outline(107,258,8,arcade.color.YELLOW,1,0,15)
        arcade.draw_line(102,261,104,258,arcade.color.YELLOW)
        arcade.draw_line(104,258 ,106 ,261 , arcade.color.YELLOW)
        arcade.draw_line(108,258 ,110 ,261 , arcade.color.YELLOW)
        arcade.draw_line(110,258 ,112 ,261 , arcade.color.YELLOW)
        arcade.draw_line(105,256 , 107,253 , arcade.color.YELLOW)
        arcade.draw_line(107,253 , 109, 256, arcade.color.YELLOW)
        arcade.draw_polygon_filled([(379,234), (387,232 ), (377,220 ), (336,219 )],arcade.color.LIGHT_GRAY)
        arcade.draw_line(360,234,364,235,arcade.color.BLUE_SAPPHIRE)


        arcade.draw_line(399,227 , 412,227 , arcade.csscolor.BLACK, 1)
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

        arcade.draw_arc_outline(350,227,19,100,arcade.csscolor.BLACK,20, 180, 1, 90, 20)
#arcade.draw_lrbt_rectangle_filled(274,430,226 ,400 ,arcade.color.BLUE)
        #nose
        arcade.draw_lines([(399,228 ), (392,231 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(392,231 ), (384,233 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(384, 233), (373, 235)], arcade.color.BLACK, 1)
        arcade.draw_lines([(399, 228), (400, 225)], arcade.color.BLACK, 1)


        arcade.draw_lines([(373,234 ), (368,236 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(367,235 ), (369,240 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(369,240 ), (356,238 )], arcade.color.BLACK, 1)
        #
        arcade.draw_lines([(356,238 ), (352,242 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(352,242 ), (340,249 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(397, 228), (395, 229)], arcade.color.BLACK, 1)
        arcade.draw_lines([(397, 228), (395, 229)], arcade.color.BLACK, 1)
        arcade.draw_lines([(340, 248), (336,251 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(336,251 ), (332,251 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(332, 251), (324, 253)], arcade.color.BLACK, 1)
        arcade.draw_lines([(324, 253), (304,250 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(304, 250), (290,248 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(290, 248), (264,246 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(264,246 ), (172,242 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(172, 242), (177,245 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(177, 245), ( 178,247 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(178, 247), (168, 249)], arcade.color.BLACK, 1)
        arcade.draw_lines([(168, 249), (156,247 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(156,246 ), (116,274 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(73,271 ), (121,276 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(121,276 ), (124,280 )], arcade.color.BLACK, 1)
        #Suite
        arcade.draw_lines([(60,229 ), (70,231 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(70,231 ), (73,271 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(74, 271), (68,273 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(68,273 ), (68,275 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(68, 275), (74,277 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(73,277 ), (71,292 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(71,292 ), (90,294 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(90,294 ), (107,281)], arcade.color.BLACK, 1)
        arcade.draw_lines([(73,276 ), (118,281 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(118,281 ), (122,279)], arcade.color.BLACK, 1)
        #inside outline
        arcade.draw_lines([(69,230 ), (278,241 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(278,241 ), (304,237)], arcade.color.BLACK, 1)
        arcade.draw_lines([(304,237 ), (340,232 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(340,232 ), (368,236 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(72,233 ), (87,245 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(87,245 ), (154,248 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(269,229 ), (308,228 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(308,228 ), (327,226 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(327,226 ), (303,223 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(303,223 ), (286,224 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(286,224 ), (291,226 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(291, 226), (269,229 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(281,218 ), (244,222 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(61,229 ), (63,206 )], arcade.color.BLACK, 1)

        arcade.draw_lines([(99,213 ), (125,217 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(125,217 ), (158,218 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(44,217 ), (62,220 )], arcade.color.BLACK, 1)
        arcade.draw_lines([(44,212), (62,214)], arcade.color.BLACK, 1)
        arcade.draw_lines([(44,220 ), (62,226 )], arcade.color.BLACK, 1)

        arcade.draw_lines([(85,271 ), (89,244)], arcade.color.BLACK, 1)
        arcade.draw_lines([(71,271 ), (85, 271)], arcade.color.BLACK, 1)



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