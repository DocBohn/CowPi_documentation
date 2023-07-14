Configuring ``stdio`` File Streams
==================================

..  contents:: \

Configuring ``stdin`` and ``stdout``
------------------------------------

Printing to the Serial Monitor or other serial terminal emulator on a host computer is common enough, especially for debugging.
For this reason, the :func:`cowpi_stdio_setup` function will configure the standard output file stream (``stdout``) to send its output to the USB connection to the host computer.
This will allow you to use ``printf()`` to print to a serial terminal.
Someone less-common is reading input from a serial terminal.
Nonetheless, the :func:`cowpi_stdio_setup` function will also configure the standard input file stream (``stdin``) to get its input from the USB connection to the host computer.
This will allow you to use ``scanf()`` to read from a serial terminal.

..  image:: img/printf_and_scanf.gif

The only parameter is the bitrate, in bits per second;
be sure to match the serial terminal's expectations.
**9600** is typical, though **115200** isn't uncommon.

..  doxygenfunction:: cowpi_stdio_setup

..  NOTE::
    The :func:`cowpi_setup` function will call :func:`cowpi_stdio_setup`.
    If you call :func:`cowpi_setup` then there is no need to separately call :func:`cowpi_stdio_setup`.

..  IMPORTANT::
    If your program calls :func:`cowpi_stdio_setup` without a serial terminal to connect to, then one of two things
    will happen, depending on which microcontroller board you are using:

    - Your program may continue to run without printing anything, and will reset when a serial terminal is connected (example: Arduino Nano)
    - Your program may block until a serial terminal is connected (example: Raspberry Pi Pico)

..  NOTE::
    The :func:`cowpi_stdio_setup` function does *not* configure the standard error file stream (``stderr``).
    You may explicitly set the ``stderr`` file stream.
    Common choices are to assign ``stderr = stdout`` or to assign ``stderr`` to a Morse Code "display" using :func:`cowpi_add_display_module`.


Configuring a Display Module
----------------------------

To configure a display module and obtain a file stream that can be used with ``fprintf()`` to send text to that display module, use the :func:`cowpi_add_display_module` function.

..  doxygenfunction:: cowpi_add_display_module

The function returns a ``FILE *`` pointer that can be used with ``fprintf()``.
If the function returns ``NULL`` then the file stream was not created.

The :func:`cowpi_add_display_module` function takes two arguments.
The first argument is a :struct:`cowpi_display_module_t` structure that has the details for the display module,
and the second argument is a :struct:`cowpi_display_module_protocol_t` structure that has details for the communication protocol that will be used to communicate with the display module.

Owing to differences between the C programming language and the C++ programming language, the ``CowPi_stdio`` library offers two mechanisms to create those arguments.

Configuring a Display Module in C
"""""""""""""""""""""""""""""""""

The C programming language allows structures to be initialized while skipping over fields whose values are irrelevant or whose default values are acceptable.
Therefore, in *C* files we recommend calls of the form

..  code-block:: c
    :linenos:

    FILE *display = cowpi_add_display_module(
                (cowpi_display_module_t) {
                        .display_module = XXX,          // XXX is the type of display module
                        ...other_relevant_fields...
                },
                (cowpi_display_module_protocol_t) {
                        .protocol = YYY,                // YYY is the communication protocol
                        ...other_relevant_fields...
                }
            );

The structures are:

..  doxygenstruct:: cowpi_display_module_t
    :members:
    :undoc-members:

..  doxygenstruct:: cowpi_display_module_protocol_t
    :members:
    :undoc-members:

..  NOTE::
    When initializing the structures, you should *only* specify the fields that are relevant for your display module and communication protocol.
    For example, you would not specify the ``i2c_address`` for the ``SPI`` protocol, nor would you specify the ``display_orientation`` for a ``SEVEN_SEGMENT`` display module.

As a specific example, you might configure a 16x2 LCD character display that uses the |i2c| protocol with:

..  code-block:: c
    :linenos:

    FILE *display = cowpi_add_display_module(
                (cowpi_display_module_t) {
                        .display_module = LCD_CHARACTER,
                        .width = 16,
                        .height = 2
                },
                (cowpi_display_module_protocol_t) {
                        .protocol = I2C
                        .i2c_address = cowpi_discover_i2c_address(SDA, SCL)
                }
            );
    fprintf(display, "Hello, World!\n");

Enumerated types are available where relevant.

Available Display Modules
^^^^^^^^^^^^^^^^^^^^^^^^^

..  doxygenenum:: display_modules

..  seealso::
    -   The :doc:`seven_segment` page has further discussion about MAX7219-driven seven-segment display modules.
    -   The :doc:`led_matrix` page has further discussion about MAX7219-driven LED matrix display modules.
    -   The :doc:`lcd_character` page has further discussion about HD44780-driven LCD character display modules.
    -   (SSD1306-driven OLED matrix displays are not yet available)
    -   The :doc:`morse_code` page has further discussion about using Morse Code to communicate with only an LED or active buzzer.

For MAX7219-driven LED matrix displays, there is no standard relationship between dot matrix positions and MAX7219 bits.
For this reason, we provide a way to ensure that the top of the characters are at the top of the display and to ensure that the characters are forward-facing and not reversed.

..  doxygenenum:: orientations

..  doxygenenum:: flips

Available Communication Protocols
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  doxygenenum:: protocols

Because HD44780-driven LCD character displays do not natively communicate over a serial protocol, an adapter is required.
Depending on which adapter you use, you may need to specify how the adapter maps the protocol's bits to the display module's bits.

..  seealso::
    The :doc:`protocols` page has further discussion about the communication protocols.

..  doxygenenum:: adapter_mappings

Configuring a Display Module in C++
"""""""""""""""""""""""""""""""""""

The C++ programming language does not allow skipping over fields in ``struct`` initializers, and so we have provided convenience functions.
These convenience functions have default argument values where appropriate (which is not an option in C), and so in *CPP* and *INO* files we recommend calls of the form

..  code-block:: cpp
    :linenos:

    FILE *display = cowpi_add_display_module(
                cowpi_configure_XXX(...arguments...),   // XXX is the type of display module
                cowpi_configure_YYY(...arguments...)    // YYY is the communication protocol
            );

As a specific example, you might configure a 16x2 LCD character display that uses the |i2c| protocol with:

..  code-block:: cpp
    :linenos:

    FILE *display = cowpi_add_display_module(
                cowpi_configure_lcd_character_display(16, 2),
                cowpi_configure_i2c(cowpi_discover_i2c_address(SDA, SCL));
            );
    fprintf(display, "Hello, World!\n");

Convenience functions are available for each of the possible display modules and communication protocols.

Available Display Modules
^^^^^^^^^^^^^^^^^^^^^^^^^

..  doxygenfunction:: cowpi_configure_seven_segment_display

..  seealso::
    The :doc:`seven_segment` page has further discussion about MAX7219-driven seven-segment display modules.

..  doxygenfunction:: cowpi_configure_led_matrix_display

..  seealso::
    The :doc:`led_matrix` page has further discussion about MAX7219-driven LED matrix display modules.

..  doxygenfunction:: cowpi_configure_lcd_character_display

..  seealso::
    The :doc:`lcd_character` page has further discussion about HD44780-driven LCD character display modules.

(``cowpi_configure_oled_matrix_display()`` is not yet available)

..  doxygenfunction:: cowpi_configure_morse_code

..  seealso::
    The :doc:`morse_code` page has further discussion about using Morse Code to communicate with only an LED or active buzzer.

Available Communication Protocols
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  doxygenfunction:: cowpi_configure_single_pin

..  doxygenfunction:: cowpi_configure_spi

..  doxygenfunction:: cowpi_configure_i2c

..  seealso::
    The :doc:`protocols` page has further discussion about the communication protocols.
