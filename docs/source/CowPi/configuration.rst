Configuration / Initializing the Board
======================================

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
