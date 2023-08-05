Other Functions for Display Modules
===================================

..  contents:: \

Relatively Low-Level Functions
------------------------------

The CowPi_stdio library has several functions designed to control the display modules with greater flexibility than you can achieve with the ``stdio`` functions.
If you want or need to use them, they are exposed to the application programmer, and you can review their Doxygen comments in the :doc:`direct-control` Section.
In general, we believe that most, application programmers do not need to use them if you are using the more-convenient ``stdio`` functions and the `Special Functions`_ described in the next section.

..  WARNING::
    Using the lower-level functions to control display modules that you are also addressing with a file stream may result in undesirable behavior.

There are, however, one or two exceptions.

..  doxygenfunction:: cowpi_hd44780_create_character

..  doxygenfunction:: cowpi_font_ascii_to_5wide_dotmatrix

Of these two, we believe that :func:`cowpi_hd44780_create_character` will be more commonly used.
The HD44780 has eight custom-character locations for character values 0-7 and aliased to character values 8-15.
When a character byte holds one of these values, the corresponding custom character will be displayed.
Because the byte value 0x00 represents a terminal ``NUL`` for the ``stdio`` functions, and because the byte values 0x09-0x0D represent ASCII control characters (see :numref:`asciiControlCharacters`),
we recommend that you strictly use the character values 1-8 for the custom characters.

..  TIP::
    When printing using custom characters, you can do so using a ``%c`` conversion specifier:

    ..  code:: cpp

        fprintf(display, "Here's a custom character: %c\n", my_characters[i]);

    or, if there is only one possible character for that string, then a literal byte for the character value can be placed in the format string:

    ..  code:: cpp

        fprintf(display, "Here's a custom character: \x1\n");

The *hd44780_blinky* and *hd44780_lcd_character* examples both demonstrate the use of custom characters.

The *hd44780_lcd_character* example also demonstrates the use of :func:`cowpi_font_ascii_to_5wide_dotmatrix`.
As noted in :doc:`lcd_character`, there are a few ASCII character values that the HD44780 uses for characters other than the corresponding ASCII characters, such as ``\``.
You can overcome this by using :func:`cowpi_font_ascii_to_5wide_dotmatrix` to obtain a sequence of bytes that correspond to the ASCII character, packaged in an array that :func:`cowpi_hd44780_create_character` can make use of.

..  NOTE::
    In the future we anticipate providing `Special Functions`_ to eliminate the need to most application programmers to use even these two lower-level functions.


Special Functions
-----------------

The CowPi_stdio library provides three functions that take a ``FILE *`` argument and performs certain actions on the display.
The :func:`cowpi_clear_display`, :func:`cowpi_sleep_display`, and :func:`cowpi_wake_display` functions perform actions that otherwise would require using
lower-level ``cowpi_max7219_XXX`` or ``cowpi_hd44780_XXX`` functions but do so in a way that do not risk unpredictable behavior.
We summarize them here.

..  doxygenfunction:: cowpi_clear_display

..  doxygenfunction:: cowpi_sleep_display

..  doxygenfunction:: cowpi_wake_display

..  list-table:: Behavior of special functions
    :header-rows: 1
    :stub-columns: 1
    :align: center

    *   -
        -   :func:`cowpi_clear_display`
        -   :func:`cowpi_sleep_display`
        -   :func:`cowpi_wake_display`
    *   -   | USB connection
            | to host computer
        -   ignored
        -   ignored
        -   ignored
    *   -   7-segment display
        -   | Removes all displayed characters
            | and performs a form feed
        -   | Places MAX7219 in
            | "shutdown" mode
        -   | Takes MAX7219 out of
            | "shutdown" mode
    *   -   LED matrix display
        -   | Prints remaining characters
            | that are in the buffer
            | and performs a form feed
        -   | Places MAX7219 in
            | "shutdown" mode
        -   | Takes MAX7219 out of
            | "shutdown" mode
    *   -   LCD character display
        -   | Removes all displayed characters
            | and performs a form feed
        -   Disables backlight
        -   Enables backlight
    *   -   Morse Code
        -   ignored
        -   ignored
        -   ignored
