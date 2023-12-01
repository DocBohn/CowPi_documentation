********
Hardware
********

..  |LibraryLicense| image:: https://img.shields.io/github/license/DocBohn/CowPi_hardware?color=rgb(0,153,176)
..  _LibraryLicense: https://github.com/DocBohn/CowPi_hardware/blob/main/LICENSE
..  |DocumentationLicense| image:: https://img.shields.io/github/license/DocBohn/CowPi_documentation
..  _DocumentationLicense: https://github.com/DocBohn/CowPi_documentation/blob/main/LICENSE

-   Hardware design licensed under |LibraryLicense|_
-   Documentation licensed under |DocumentationLicense|_


This section describes the Cow Pi development boards, describes the theory of operation for its components, and summarizes the features of its display module.

.. IMPORTANT::
    If you need to assemble a Cow Pi development board, see the :doc:`construction`.


.. Cow Pi Development Board Overview
.. =================================

**Cow Pi Development Board Overview**


The Cow Pi development board consists of:

- a microcontroller board, such as an Arduino Nano, an Arduino Uno, or a Raspberry Pi Pico
- a display module, such as a MAX7219-driven 8-digit/7-segment display, an HD44780-driven LCD character display, or an SSD1306-driven OLED graphic display
- a 4 × 4 matrix keypad
- two momentary buttons
- two toggleable switches, and
- at least two LEDs

Cow Pi mk1 boards are assembled on solderless breadboards:

.. image:: hardware/mk1a.jpg
    :height: 3cm
    :alt: A rat's nest of wires attached to a solderless breadboard. The keypad is a membrane keypad, and the display is an 8-digit/7-segment display.
.. image:: hardware/mk1d.jpg
    :height: 3cm
    :alt: A rat's nest of wires attached to a solderless breadboard. The keypad is a membrane keypad, and the display is an LCD character display.

Cow Pi mk2 boards are assembled on perfboards:

.. image:: hardware/mk2a.jpg
    :height: 3cm
    :alt: Perfboards mounted on a wooden base with an Arduino Nano mounted upon one of them. Wires stretch across, and between, the perfboards. The keypad is a membrane keypad adhered to a wooden block, and the display is an 8-digit/7-segment display.
.. image:: hardware/mk2b-1.jpg
    :height: 3cm
    :alt: A perfboard designed to mount atop an Arduino Uno. Wires stretch across the perfboard. The keypad is a membrane keypad, and the display is an LED matrix display.
.. image:: hardware/mk2c.jpg
    :height: 3cm
    :alt: Perfboards mounted on a wooden base with an Arduino Nano mounted upon one of them. Wires stretch across, and between, the perfboards. The keypad is a matrix of discrete tactile switches with a low-valued resistor inlined with each row, and the display is an LCD character display.

Cow Pi mk3 boards are assembled on through-hole PCBs:

.. image:: hardware/mk3a.jpg
    :height: 3cm
    :alt: Red printed circuit boards with Arduino Nanos mounted upon them. The keypad is a matrix of discrete tactile switches with a diode inlined with each key, and the display is an LCD character display.
.. image:: hardware/mk3b-vice.jpg
    :height: 3cm
    :alt: A blue printed circuit board designed to mount atop an Arduino Uno. The keypad is a matrix of discrete tactile switches with a "forest" of diodes to the side; while no display is currently attached, insertion points for an arbitrary display module are attached to the board.
.. image:: hardware/mk3c.jpeg
    :height: 3cm
    :alt: A yellow printed circuit board with a Raspberry Pi Pico mounted upon it. The keypad is a matrix of discrete tactile switches with a "forest" of diodes to the side, and the display is an OLED graphic display.

Cow Pi mk4 boards are assembled on surface-mount PCBs:

.. image:: hardware/mk4a.jpeg
    :height: 3cm
    :alt: A red printed circuit board with a Raspberry Pi Pico-H mounted in an elevated position upon it. The keypad is a matrix of discrete tactile switches with adjoining diodes, and the display is an OLED graphic display.

.. image:: hardware/mk4b.jpeg
    :height: 3cm
    :alt: A red printed circuit board with a Raspberry Pi Pico mounted directly upon it. The keypad is a matrix of discrete tactile switches with adjoining diodes, and the display is an OLED graphic display.


The toggleable switches are referred to as the **left switch** and the **right switch**, and each can be positioned in the left or right position.
When a switch is in the right position, its logic value is high, by way of a pull-up resistor.
When a switch is in the left position, the switch is grounded, and its logic value is low.

The momentary buttons are referred to as the **left button** and the **right button**, and each can be pressed (alternatively, in the down position) or unpressed (alternatively, in the up position).
The buttons are normally-open, and so when a button is unpressed, its logic value is high, by way of a pull-up resistor.
When a button is pressed, the button is grounded, and its logic value is low.

The LEDs are referred to as the **left LED** and the **right LED**.
An LED will illuminate when the corresponding microcontroller output is high, and it will deluminate when the corresponding microcontroller output is low.
Most of the microcontroller boards incorporated into Cow Pi designs have an LED mounted on the microcontroller board itself, which we refer to as the **internal LED**.
The internal LED on Arduino boards also serves as the left LED.
The internal LED on Raspberry Pi Pico boards are a distinct, third LED.

The matrix keypad is designed to be scanned using the conventional approach of selectively setting the rows’ logic values and reading the columns’ resulting logic values.

.. WARNING::
    The matrix keypads used in the Cow Pi mk1 designs and the mk2a & mk2b designs cannot safely have multiple keys simultaneously pressed.
    Certain key combinations will result in a short circuit.
.. IMPORTANT::
    The matrix keypad used in the Cow Pi mk2c design cannot reliably read more than two simultaneously-pressed keys.
    Certain key combinations will result in unpressed keys falsely being detected as pressed.
.. NOTE::
    The matrix keypad used in the Cow Pi mk3 & mk4 designs use general-purpose diodes to isolate the keys.
    Any combination of up to 16 simultaneously-pressed keys can safely and reliably be read on Cow Pi *mk3 & mk4 designs only*.

The microcontroller communicates with the display module using either
the Serial Peripheral Interface (SPI) protocol or
the Inter-Integrated Circuit (|i2c| or IIC) protocol, also known as the Two-Wire Interface (TWI) protocol.

.. toctree::

    hardware/boards
    hardware/inputs
    hardware/outputs
