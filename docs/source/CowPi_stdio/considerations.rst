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

Enabling Floating Point Conversions
"""""""""""""""""""""""""""""""""""

AVR Targets
'''''''''''

You can enable floating point conversions on AVR targets by passing these arguments to the linker::

    -Wl,-u,vfprintf -lprintf_flt -lm

-   **If using the Arduino IDE**\ , then you must create a *platform.local.txt* compiler configuration file (or edit one that is already present);
    this will change the settings for *all* projects. Using your file browser or command line, navigate to:

        :Windows:   *C:\\Users\\*\ ▶username◀\ *\\AppData\\Local\\Arduino15\\packages\\arduino\\hardware\\avr\\*\ ▶version_number◀\ *\\*

        :MacOS:     */Users/*\ ▶username◀\ */Library/Arduino15/packages/arduino/hardware/avr/*\ ▶version_number◀\ */*

        :Linux:     */home/*\ ▶username◀\ */.arduino15/packages/arduino/hardware/avr/*\ ▶version_number◀\ */*

        (if using an Arduino Nano Every, replace *avr* with *megaavr*)

    In that directory, create (or edit) the file *platform.local.txt* with this line:

    ..  code-block:: ini

        compiler.c.elf.extra_flags = -Wl,-u,vfprintf -lprintf_flt -lm

-   **If using PlatformIO**\ , you can enable these arguments on a project-by-project basis.
    These arguments will be ``build_flags`` in the project's *platformio.ini* file.
    For example:

    ..  code-block:: ini
        :emphasize-lines: 5

        [env:nanoatmega328new]
        platform = atmelavr
        board = nanoatmega328new
        framework = arduino
        build_flags = -Wl,-u,vfprintf -lprintf_flt -lm

ARM Targets
'''''''''''

..  TODO:: Linker arguments and/or inline asm directive for ARM


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
            | see :numref:`sevenSegmentTable` and :numref:`sevenSegmentFigure`, or see `MAX7219 datasheet <https://www.analog.com/media/en/technical-documentation/data-sheets/max7219-max7221.pdf>`_, Table 6
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
            | see :numref:`sevenSegmentTable` and :numref:`sevenSegmentFigure`, or see `MAX7219 datasheet <https://www.analog.com/media/en/technical-documentation/data-sheets/max7219-max7221.pdf>`_, Table 6
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

..  _memoryExpensiveDisplays:

Enabling/Disabling Memory-Expensive Display Modules
---------------------------------------------------

While the CowPi_stdio library is written for run-time configuration, there are some portions that you may wish to eliminate at compile-time to reduce the memory used.
You can do so by passing compile-time arguments that are discussed below:

Matrix Font
"""""""""""

The dot matrix font defined in the library is sizable indeed.
Removing the dot matrix font will eliminate a little over 2KB -- on AVR devices, this savings will be in flash memory;
on ARM devices, this savings will be in RAM

- ``-DNO_MATRIX_FONT`` explicitly excludes the dot matrix font and any display modules that depend upon it;
  this is the default for the ATmega328P (Arduino Uno, Arduino Nano)
- ``-DMATRIX_FONT`` explicitly includes the dot matrix font;
  this is the default for all other microcontrollers

Morse Code Font
"""""""""""""""

The Morse Code font defined in the library is smaller than the dot matrix font but large enough to consider excluding.
Removing the Morse Code font will eliminate a little over 1KB -- on AVR devices, this savings will be in flash memory;
on ARM devices, this savings will be in RAM

- ``-DNO_MORSE_FONT`` explicitly excludes the Morse Code font and the Morse Code display;
  this is the default for the ATmega328P (Arduino Uno, Arduino Nano)
- ``-DMORSE_FONT`` explicitly includes the Morse Code font;
  this is the default for all other microcontrollers

Timed Displays
""""""""""""""

There are some displays that update based on a timer, such as the scrolling 7-segment display, the LED matrix display, and the Morse Code display.
Passing the compiler argument ``-DNO_TIMED_DISPLAYS`` will disable these displays and will elimate 880 bytes from flash memory.
This argument is *not* the default on any microcontrollers.

Which displays are disabled
"""""""""""""""""""""""""""

- The scrolling option for the :doc:`seven_segment` is disabled when ``NO_TIMED_DISPLAYS`` is defined
- The :doc:`led_matrix` is disabled when either ``NO_TIMED_DISPLAYS`` or ``NO_MATRIX_FONT`` is defined
- The :doc:`morse_code` is disabled when either ``NO_TIMED_DISPLAYS`` or ``NO_MORSE_FONT`` is defined
- All other displays are always enabled

If you attempt to configure a disabled display module, then the ``FILE *`` variable that :func:`add_display_module` returns will be ``NULL``, the same as would happen for any other configuration error.

..  _passingCompilerArguments:

Passing Compiler Arguments
""""""""""""""""""""""""""

These examples specifically show disabling the Morse Code font and timer-based displays;
replace the arguments shown with your intended arguments.

-   **If using the Arduino IDE**\ , then you must create a *platform.local.txt* compiler configuration file (or edit one that is already present);
    this will change the settings for *all* projects. Using your file browser or command line, navigate to:

        :Windows:   *C:\\Users\\*\ ▶username◀\ *\\AppData\\Local\\Arduino15\\packages\\arduino\\hardware\\*\ ▶platform◀\ *\\*\ ▶version_number◀\ *\\*

        :MacOS:     */Users/*\ ▶username◀\ */Library/Arduino15/packages/arduino/hardware/*\ ▶platform◀\ */*\ ▶version_number◀\ */*

        :Linux:     */home/*\ ▶username◀\ */.arduino15/packages/arduino/hardware/*\ ▶platform◀\ */*\ ▶version_number◀\ */*

        Where *▶platform◀* is the specific platform for your microcontroller board:

            :avr:           Arduino Nano, Arduino Uno, Arduino Mega 2560
            :megaavr:       Arduino Nano Every
            :samd:          Arduino Nano 33 IoT
            :mbed_nano:     Arduino Nano 33 BLE
            :mbed_rp2040:   Arduino Nano RP2040 Connect, Raspberry Pi Pico

    In that directory, create (or edit) the file *platform.local.txt* with lines such as these:

    ..  code-block:: ini

        compiler.c.extra_flags = -DNO_MORSE_FONT -DNO_TIMED_DISPLAYS
        compiler.cpp.extra_flags = -DNO_MORSE_FONT -DNO_TIMED_DISPLAYS

-   **If using PlatformIO**\ , you can enable these arguments on a project-by-project basis.
    These arguments will be ``build_flags`` in the project's *platformio.ini* file.
    For example:

    ..  code-block:: ini
        :emphasize-lines: 5

        [env:nanoatmega328new]
        platform = atmelavr
        board = nanoatmega328new
        framework = arduino
        build_flags = -DNO_MORSE_FONT -DNO_TIMED_DISPLAYS
