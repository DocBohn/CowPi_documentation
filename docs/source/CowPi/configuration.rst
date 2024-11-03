Initializing the Board and Pin Configuration
============================================

Initializing the Board
----------------------

When using a Cow Pi board, a single function call is sufficient to configure all pins and fully initialize the board if no :doc:`../expansion` are used.
(If expansions are used, their pins must must be configured separately, as must their initialization.)

The :func:`cowpi_setup` function does three things:

-   It initializes the standard input/output/error FILE streams at the specified bitrate
-   It configures the display module using the same :struct:`cowpi_display_module_t` and :struct:`cowpi_display_module_protocol_t` arguments as the CowPi_stdio library's :func:`cowpi_add_display_module` function
    -   The function returns a pointer to the display module's FILE stream
-   It assigns the peripheral inputs and outputs to the microcontroller pins appropriate to your particular Cow Pi board,
    and it configures the pins accordingly

..  doxygenfunction:: cowpi_setup
    :project: CowPi


Custom Pin Configuration
------------------------

The :func:`cowpi_setup` configures the pins for the inputs and outputs on the Cow Pi board,
but pins used by other inputs and outputs must be configured separately.
The CowPi library provides framework-independent functions to configure pins as output pins, high-impedance ("floating") input pins, or pulled-up input pins.
(Portability aside, we very strongly recommend using these functions to reduce some guesswork by other functions in the library.)

These functions take a single argument:
a bit vector that identifies which pin(s) are to be configured.
If bit *n* is a 1, then pin *n* will be configured by the function.
If bit *n* is a 0, then pin *n*'s existing configuration will be left unchanged.

..  doxygenfunction:: cowpi_set_output_pins
    :project: CowPi

..  doxygenfunction:: cowpi_set_floating_input_pins
    :project: CowPi

..  doxygenfunction:: cowpi_set_pullup_input_pins
    :project: CowPi
