import arcade



def draw_lines():

    arcade.open_window(900,900, "lines demo")
    arcade.set_background_color(arcade.color.WHITE)


    width = arcade.get_window().width
    height = arcade.get_window().height

    arcade.start_render()


    for location in range(80, width, 80):
        arcade.draw_line(location, 0, location, height, arcade.color.BLACK, 2)









    arcade.finish_render()
    arcade.run()

draw_lines()