..  include:: ../mk1ef.txt

Installing the IDE
==================
*Cow Pi mk1e: Arduino Nano form factor*

\
\

..  ATTENTION::
    **If you are a Windows user,** please review the notes about CH340 USB Driver issues for :ref:`Windows10CH340` and :ref:`Windows11CH340`.

\
\

Broadly speaking, you have two options:

-   Using the :ref:`mk1fArduinoIDE` (either on a lab computer or your personal laptop)
-   Using :ref:`mk1eVSCodeWithPlatformIO`


..  _mk1eArduinoIDE:

..  include:: ide-arduino-before-board-selection.rst

-   You will need to select the board and port;
    on Windows, you may need to select "Show Hidden Ports" (see :numref:`mk1eSelectingBoard`\ (a)).
    With Arduino Nanos, you will also need to select the processor (see :numref:`mk1eSelectingBoard`\ (b) and the discussion below).

.. _mk1eSelectingBoard:
.. figure:: ../../../blank.png

    Selecting board and processor in the Arduino IDE.

    +-----------------------------------------------+---------------------------------------------------------+
    | a                                             | b                                                       |
    +===============================================+=========================================================+
    | .. image:: selecting-nano.jpg                 | .. image:: selecting-nano-processor.jpg                 |
    |    :width: 8cm                                |    :width: 8cm                                          |
    |    :align: center                             |    :align: center                                       |
    +-----------------------------------------------+---------------------------------------------------------+
    | Selecting the board with Arduino IDE 2.0.     | Selecting the processor after selecting the board.      |
    +-----------------------------------------------+---------------------------------------------------------+

..  include:: ide-arduino-after-board-selection.rst

If you are satisfied with using the Arduino IDE, then proceed to :doc:`power-mk1e`.

----

.. _mk1eVSCodeWithPlatformIO:

..  include:: ide-platformio.rst

If you are satisfied with using the Arduino IDE, then proceed to :doc:`power-mk1e`.

----

..  [#sketches]
    | The Arduino language is based off of the Wiring language, which in turn is based off of the Processing language, which was designed to make computing accessible to artists.
..  [#usingC]
    | Your code in the I/O labs will be C code.
..  [#arduinoMain]
    | https://github.com/arduino/ArduinoCore-avr/blob/master/cores/arduino/main.cpp
..  [#usbConnection]
    | You can connect the USB cable to a "wall wart" USB power supply or to a USB battery pack if you only want to provide power to the Arduino Nano, but you need to connect it to a computer to upload a new sketch to the Arduino Nano.
..  [#toughLuck]
    | If it makes you feel any better, when we used Altera boards for the I/O labs, Mac users had no choice but to use lab computers.
