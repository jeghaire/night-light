def on_forever():
    if input.light_level() < 50:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif input.light_level() < 150 and input.light_level() > 50:
        pass
    else:
        basic.show_leds("""
            . # . # .
                        . # . # .
                        # # # # #
                        . # . # .
                        . # . # .
        """)
        basic.clear_screen()
basic.forever(on_forever)
