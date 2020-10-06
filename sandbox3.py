import arcade

def main():

    arcade.open_window (800,800, "Stripes")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

    stripe = arcade.create_rectangle(800,0,100,1600, arcade.color.BLACK)



    stripe.draw()


    arcade.finish_render()
    arcade.run()



main()