Special Considerations
======================

..  contents:: \


Placing Format Strings in Flash Memory
--------------------------------------

AVR 8-bit microcontrollers, such as the Atmel ATmega328P on the Arduino Nano, have a very small amount of data memory, and if your program has many string constants then that may fill up the available memory quickly.
For this reason, the avr-libc library provides the ``PSTR()`` macro to place string constants in program memory.
Because instruction memory and data memory have distinct address spaces, the standard ``printf()`` and ``fprintf()`` functions cannot access those strings.
Instead, ``printf_P()`` and ``fprintf_P()`` act just like their standard counterparts but use format strings that are in program memory.
For example:

.. code:: c

   printf("The sum of %d and %d is %d\n", i, j, i + j);

could be changed to

.. code:: c

   printf_P(PSTR("The sum of %d and %d is %d\n"), i, j, i + j);

reducing the SRAM usage by 27 bytes and increasing the Flash Memory usage by 27 bytes.

..  TODO:: Compiler arguments to enable/disable matrix & morse fonts and timer-based displays

.. .. file location for Arduino IDE described here: https://support.arduino.cc/hc/en-us/articles/4415103213714-Find-sketches-libraries-board-cores-and-other-files-on-your-computer

``printf`` Limitations
----------------------

To keep the size of the program as small as possible, most microcontrollers' implementations of ``printf()``, ``fprintf()``, ``sprintf()``, and ``snprintf()`` limit the less-commonly used conversions.
For example:

- No floating point conversions (prints without converting the specifier) on most targets

    - This can be overcome with compiler arguments, but it will significantly increase the size of your program (by about 1.4KB on AVR targets)


    - Floating point conversions are supported on Raspberry Pi Pico

- No 64-bit integer conversions (aborts print on AVR targets; prints without converting the specifier on ARM targets)

- AVR does not support specifiers with widths and precisions greater than 255 (truncates the width and precision to 8 bits)

- AVR does not support specifiers with variable width and precision (aborts the print)

    - The *hd44780_blinky* example program demonstrates the occasional need to work around this limitation

The *printf_limitations* example program demonstrates these limitations.

..  TODO:: Linker arguments to enable float conversions


ASCII Control Characters
------------------------

Some ASCII control characters are used to manage output devices.
While modern programmers rarely will see any other than ``\t``, ``\n``, and perhaps ``\r``, there are sensible uses of other control characters for some display modules.
For the USB connection to the host computer, most of these are passed through (and may be ignored by the terminal emulator).
For the display modules controlled by the library, the library determines the effect on the display.
We summarize them here, and they are demonstrated in the example programs.

..  _asciiControlCharacters:
..  list-table:: Uses of ASCII Control Characters
    :header-rows: 2
    :stub-columns: 1
    :align: center

    *   -
        -   ``\a``
        -   ``\b``
        -   ``\t``
        -   ``\n``
        -   ``\v``
        -   ``\f``
        -   ``\r``
        -   0x1B (gcc ``\e``)
        -   0x1F
    *   -   ASCII
        -   bell (alarm)
        -   backspace
        -   horizontal tab
        -   line feed (newline)
        -   vertical tab
        -   form feed (newpage)
        -   carriage return
        -   escape
        -   delete
    *   -   nominal CowPi_stdio behavior
        -   n/a
        -   | shifts cursor left;
            | next character is
            | inclusive-ORed with
            | existing character
        -   shifts cursor right
        -   | clears remaining line,
            | then ``\v\r``
        -   | places cursor in next row,
            | then ``\r``
        -   places cursor in top left
        -   places cursor in left column
        -   sends next byte literally
        -   | ``\b``, then clears
            | existing character
    *   -   USB connection to host computer
        -   passed through
        -   passed through
        -   passed through
        -   passed through as ``\n\r``
        -   passed through
        -   passed through
        -   passed through
        -   passed through
        -   passed through
    *   -   | 7-segment display
            | (no scroll)
        -   ignored
        -   ✅
        -   ✅
        -   ✅
        -   ✅
        -   ✅
        -   ✅
        -   | next byte specifies a segment pattern;
            | see `MAX7219 datasheet <https://www.analog.com/media/en/technical-documentation/data-sheets/max7219-max7221.pdf>`_, Table 6
        -   ✅
    *   -   | 7-segment display
            | (scrolling)
        -   ignored
        -   ignored
        -   inserts four spaces
        -   allows line to clear
        -   ``\n``
        -   ``\n``
        -   ``\n``
        -   | next byte specifies a segment pattern;
            | see `MAX7219 datasheet <https://www.analog.com/media/en/technical-documentation/data-sheets/max7219-max7221.pdf>`_, Table 6
        -   ignored
    *   -   | LED matrix display
            | (scrolling)
        -   ignored
        -   ignored
        -   inserts ten columns
        -   inserts 2×width columns
        -   ``\n``
        -   ``\n``
        -   ``\n``
        -   next byte specifies a column pattern
        -   ignored
    *   -   LCD character display
        -   prints ``CGRAM[7]``
        -   prints ``CGRAM[8]``
        -   ✅
        -   ✅
        -   ✅
        -   ✅
        -   ✅
        -   prints ``CGROM[27]``
        -   prints ``CGROM[127]``
    *   -   Morse Code
        -   | start of message
            | (KA)
        -   | error
            | (HH)
        -   interword space
        -   | new paragraph
            | (BT)
        -   | next line
            | (AA)
        -   | end of message
            | (AR)
        -   ignored
        -   ignored
        -   | error
            | (HH)


Pointing Multiple File Streams to the Same Display Module
---------------------------------------------------------

..  WARNING::
    Using more than one file stream to control one display module will result in undefined behavior.
