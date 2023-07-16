***************************************
Cow Pi mark 1 Construction Instructions
***************************************

*In addition to the professor and the TAs, you may freely seek help on
this assignment from other students.*

In the I/O labs, we will use a microcontroller board with some
peripherals. In this prelab, you will assemble the hardware for the I/O
labs.


Preparation
===========

Obtaining the Hardware
----------------------

The EE Shop has prepared “class kits” for CSCE 231; your class kit costs
$30. The EE Shop is located at 122 Scott Engineering Center and is open
M-F 7am-4pm. You do not need an appointment. You may pay at the window
with cash, with a personal check, or with your NCard. The EE shop does
*not* accept credit cards.

.. _inventorying:

Inventorying the Hardware
-------------------------

Examine the contents of your class kit. It contains:

-   | One (1) full-sized solderless breadboard
    | |breadboardx|

-   | One (1) Arduino Nano (or clone) microcontroller board
    | |nanox|

-   | One (1) USB cable (mini-USB shown; yours may be different)
    | |usbCablex|

-   | One (1) :math:`4 \times 4` matrix keypad
    | |keypadx|

-   | One (1) 8-pin male-male header strip
      (might already be inserted into keypad’s female connectors;
      might have more than 8 pins)
    | |headerInx| or |headerOutx|

-   | Two (2) breadboard-mount momentary pushbuttons, aka tactile switches;
      these might have two leads (which might or might not be attached to cardboard strip),
      or they might have 4 prongs
    | |buttons2Pinx| or |buttons4Pinx|

-   | Two (2) breadboard-mount slide switches
    | |switchesx|

-   | One (1) Light Emitting Diode (LED) (color may be different than shown)
    | |LEDx|

-   | One (1) 1k\ :math:`\Omega` resistor
    | |resistorx|

-   | One (1) 40-conductor 10cm "rainbow" cable (male-to-male),
    | *or* One (1) 20-conductor 10cm "rainbow" cable (male-to-male) and one (1) 20-conductor 20cm "rainbow" cable (male-to-male)
    | |dupontCablex|

-   | One (1) :math:`2 \times 16` character LCD display module
    | |lcd1602x|

-   | One (1) |i2c| Serial Interface (might be attached to display module)
    | |serialAdapterx| or |adafruitAdapterx| or |piggypackAdapterx|

-   | One (1) 4-conductor 20cm "rainbow" cable (female-to-male)
    | |fourConductorx|



..  |breadboardx| image:: oldconstruction/inventory/breadboard.jpg
    :height: 2cm
..  |nanox| image:: oldconstruction/inventory/nano.jpg
    :height: 2cm
..  |usbCablex| image:: oldconstruction/inventory/usb.jpg
    :height: 2cm
..  |keypadx| image:: oldconstruction/inventory/keypad.jpg
    :height: 2cm
..  |headerInx| image:: oldconstruction/inventory/keypad-header-in-connector.jpg
    :height: 2cm
..  |headerOutx| image:: oldconstruction/inventory/keypad-header-without-connector.jpg
    :height: 2cm
..  |buttons2Pinx| image:: oldconstruction/inventory/buttons-2pin.jpg
    :height: 2cm
..  |buttons4Pinx| image:: oldconstruction/inventory/buttons-4pin.jpg
    :height: 2cm
..  |switchesx| image:: oldconstruction/inventory/sliders-spdt.jpg
    :height: 2cm
..  |LEDx| image:: oldconstruction/inventory/led.jpg
    :height: 1cm
..  |resistorx| image:: oldconstruction/inventory/resistor.jpg
    :height: 1cm
..  |dupontCablex| image:: oldconstruction/inventory/mm-cable.jpg
    :height: 2cm
..  |lcd1602x| image:: oldconstruction/inventory/lcd1602.jpg
    :height: 2cm
..  |serialAdapterx| image:: oldconstruction/inventory/lcd-adapter.jpg
    :height: 2cm
..  |adafruitAdapterx| image:: oldconstruction/inventory/adafruit-lcd-adapter.jpg
    :height: 2cm
..  |piggypackAdapterx| image:: oldconstruction/inventory/piggyback-lcd-adapter.jpg
    :height: 2cm
..  |fourConductorx| image:: oldconstruction/inventory/fm-4cable.jpg
    :height: 2cm

There may be other items in the class kit. Set these aside;
you will not need them for this prelab, though they may be used in a specific lab.

Assembling the Class Kit
------------------------

You will assemble the hardware in the following steps.
**At various checkpoints, you should pause to have a TA or classmate double-check your work.**
When you do so, update the *checkpoints.txt* file to indicate who checked your work and when they did so.

You may want to store your partially- and fully-completed kit in a plastic food container or some other container to prevent jumper wires from being pulled out while in your backpack.

..  NOTE::
    The following pages include diagrams and some photographs of the assembly.
    The wire colors in the diagrams do not match the wire colors in the assembly.
    The wire colors in the diagrams are coded by the purpose they serve, whereas the wire colors in the photographs are the colors of wires removed from the male-to-male rainbow cable.

..  NOTE::
    The circuit you build by following these instructions will look a bit like a rat's nest by the time that you are finished.
    This is because the jumper wires you remove from the male-to-male rainbow cable are not cut to length and generally will be longer than they need to be (which is much better than being shorter than they need to be).
    If you have prior experience with building circuits on a solderless breadboard, and if you have solid-core wires and wire cutters, then optionally you may build the circuit with cut-to-length solid core wires.

    ..  image:: oldconstruction/completed-kit-lcd1602.jpg
        :width: 90%
        :align: center

    \
        \
            Cow Pi mk1d that was constructed using 10cm and 20cm jumper wires.


Modified Cow Pi mk1d
====================

