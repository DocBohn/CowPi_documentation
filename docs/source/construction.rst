*************************************
Cow Pi Physical Assembly Instructions
*************************************

The nature of the physical assembly depends on whether you are assembling a mark 1, 2, 3, or 4 Cow Pi.

----

Cow Pi mk1 boards are assembled on solderless breadboards.
Mark 1 designs require no soldering skill but do require attention to detail.
The instructions for Mark 1 designs include checkpoints at which you should have someone else -- a second set of eyes -- check whether you followed the preceding instructions correctly.
The astute reader will notice that while the first couple of checkpoints take place as you set up your environment, most checkpoints are situated between adding new components or wires to the circuit and applying power.
While the odds of you making a catastrophic mistake are low, spending a few minutes having someone check your work can save you hours of frustration.
We also provide the *io_test* code as part of the CowPi library to further validate your progress -- but this code can, of course, be run only after applying power to your circuit.

.. image:: hardware/mk1a.jpg
    :height: 3cm
    :alt: A rat's nest of wires attached to a solderless breadboard. The keypad is a membrane keypad, and the display is an 8-digit/7-segment display.
.. image:: hardware/mk1d.jpg
    :height: 3cm
    :alt: A rat's nest of wires attached to a solderless breadboard. The keypad is a membrane keypad, and the display is an LCD character display.

|

Cow Pi mk2 boards are one-off designs assembled on perfboards.
Mark 2 designs require both soldering skills for both through-hole pins for wires, and Mark 2 designs also require attention to detail.
We do not provide instructions to assemble Mark 2 designs because, as we noted, they are one-off designs that served specific purposes.
The design documentation is also limited.
If you really want to heat up your soldering iron, we recommend a Mark 3 design.

.. image:: hardware/mk2a.jpg
    :height: 3cm
    :alt: Perfboards mounted on a wooden base with an Arduino Nano mounted upon one of them. Wires stretch across, and between, the perfboards. The keypad is a membrane keypad adhered to a wooden block, and the display is an 8-digit/7-segment display.
.. image:: hardware/mk2b-1.jpg
    :height: 3cm
    :alt: A perfboard designed to mount atop an Arduino Uno. Wires stretch across the perfboard. The keypad is a membrane keypad, and the display is an LED matrix display.
.. image:: hardware/mk2c.jpg
    :height: 3cm
    :alt: Perfboards mounted on a wooden base with an Arduino Nano mounted upon one of them. Wires stretch across, and between, the perfboards. The keypad is a matrix of discrete tactile switches with a low-valued resistor inlined with each row, and the display is an LCD character display.

|

Cow Pi mk3 boards are assembled on through-hole PCBs.
Mark 3 designs require through-hole soldering skills.
We placed links to the Gerber files are (or rather, will be) in the instructions;
you can have a small number of boards produced for just a few dollars.
The instructions for Mark 3 designs include only a few of checkpoints to have a second set of eyes check your work -- the opportunities for errors are very few.
These checkpoints are intended to make sure you don't have to include desoldering to the set of skills you'll need.

.. image:: hardware/mk3a.jpg
    :height: 3cm
    :alt: Red printed circuit boards with Arduino Nanos mounted upon them. The keypad is a matrix of discrete tactile switches with a diode inlined with each key, and the display is an LCD character display.
.. image:: hardware/mk3b-vice.jpg
    :height: 3cm
    :alt: A blue printed circuit board designed to mount atop an Arduino Uno. The keypad is a matrix of discrete tactile switches with a "forest" of diodes to the side; while no display is currently attached, insertion points for an arbitrary display module are attached to the board.
.. image:: hardware/mk3c.jpeg
    :height: 3cm
    :alt: A yellow printed circuit board with a Raspberry Pi Pico mounted upon it. The keypad is a matrix of discrete tactile switches with a "forest" of diodes to the side, and the display is an OLED graphic display.

|

Cow Pi mk4 boards are assembled on surface-mount PCBs.
If you have the PCBs manufactured and delivered to you unpopulated, then Mark 4 designs require surface-mount soldering skills.
On the other hand, if you have PCBs manufactured and assembled, then you will need no skills and only a small degree of attention to detail.

.. image:: hardware/mk4a.jpeg
    :height: 3cm
    :alt: A red printed circuit board with a Raspberry Pi Pico-H mounted in an elevated position upon it. The keypad is a matrix of discrete tactile switches with adjoining diodes, and the display is an OLED graphic display.

.. image:: hardware/mk4b.jpeg
    :height: 3cm
    :alt: A red printed circuit board with a Raspberry Pi Pico mounted directly upon it. The keypad is a matrix of discrete tactile switches with adjoining diodes, and the display is an OLED graphic display.

----

.. toctree::
    :maxdepth: 3

    construction/nano/construction-mk1e
    construction/nano/construction-mk1f
    construction/pico/assemble-mk3c
    construction/pico/assemble-mk4b
