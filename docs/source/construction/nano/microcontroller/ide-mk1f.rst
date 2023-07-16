..  include:: ../mk1ef.txt

Installing the IDE
==================
*Cow Pi mk1f: Arduino Nano form factor*

Broadly speaking, you have two options:

-   Using the :ref:`mk1fArduinoIDE`
-   Using :ref:`mk1fVSCodeWithPlatformIO`


..  _mk1fArduinoIDE:

..  include:: ide-arduino-before-board-selection.rst


You will need to select the board and port;
on Windows, you may need to select "Show Hidden Ports" (see :numref:`mk1fSelectingBoard`\ (a)).
With Arduino Nanos, you will also need to select the processor (see :numref:`mk1fSelectingBoard`\ (b) and the discussion below).

.. _mk1fSelectingBoard:
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

If you are satisfied with using the Arduino IDE, then proceed to :doc:`power-mk1f`.

----

.. _mk1fVSCodeWithPlatformIO:

..  include:: ide-platformio.rst

If you are satisfied with using the Arduino IDE, then proceed to :doc:`power-mk1f`.

----

..  [#sketches]
    | The Arduino language is based off of the Wiring language, which in turn is based off of the Processing language, which was designed to make computing accessible to artists.
..  [#usingC]
    | Your code in the I/O labs will be C code.
..  [#arduinoMain]
    | https://github.com/arduino/ArduinoCore-avr/blob/master/cores/arduino/main.cpp
..  [#usbConnection]
    | You can connect the USB cable to a "wall wart" USB power supply or to a USB battery pack if you only want to provide power to the Arduino Nano, but you need to connect it to a computer to upload a new sketch to the Arduino Nano.


