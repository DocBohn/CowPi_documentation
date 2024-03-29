**************************************************************************************************************
Cow Pi mark 4b Assembly Instructions (Raspberry Pi Pico, SSD1306 OLED graphic display via |i2c| communication)
**************************************************************************************************************

..  image:: mk4b-images/certification-mark-US002586-stacked.png
    :alt: OSHW Certification US002586
    :target: https://www.oshwa.org/cert/
    :align: right
    :width: 25%

This is a minimal set of instructions but should be sufficient if you are using a fully-populated Cow Pi mk4b.
A more detailed set of instructions that include other options will be available soon.

..  contents::
    :depth: 2

----

Prepare to Assemble the Cow Pi mark 4b
======================================

Required and Optional Components
--------------------------------

..  _mk4bComponents:
..  figure:: mk4b-images/components.jpeg
    :alt: various electronic components that are described in the accompanying text
    :align: center
    :width: 90%

    Components for a Cow Pi mk4b development board, prior to final assembly.

The components for a Cow Pi mk4b development board are:

-   One (1) Cow Pi mk4b printed circuit board, populated at a PCBA facility

    -   `Gerber files <https://github.com/DocBohn/CowPi_hardware/blob/main/mark-4/CowPi-mk4b-natural-gerber.zip>`_
    -   `BOM file <https://github.com/DocBohn/CowPi_hardware/blob/main/mark-4/CowPi-mk4b-natural.csv>`_ (optimized for JLCPCB)
    -   `Pick & Place file <https://github.com/DocBohn/CowPi_hardware/blob/main/mark-4/CowPi-mk4b-natural-top-pos.csv>`_ (optimized for JLCPCB)
    -   `KiCad files <https://github.com/DocBohn/CowPi_hardware/tree/main/mark-4/CowPi-mk4b-natural>`_

-   Six (6) PCB "feet", *or* adhesive rubber or silicone "bumper pads"

    -   Both options are shown
    -   Nylon spacers are show for the "feet" option; many other options are viable.

-   One (1) mini-breadboard with adhesive backing


Tools
-----

-   Diagonal cutters *or* end cutters

    -   Both options are shown


Final Assembly Instructions
===========================

:\:[   ]: The display module's header pins extend a few millimeters beyond the backside of the PCB.
        Using the diagonal cutters or end cutters, trim the display module's header pins so that they are shorter than the PCB feet or bumper pads.

..  _mk4bCutterOptions:
.. figure:: ../../blank.png

    Trimming the display module's headers using (a) diagonal cutters or (b) end cutters

    +-------+-------------------------------------------------+-------+-----------------------------------------+
    |       | .. image:: mk4b-images/diagonal-cutters.jpg     |       | .. image:: mk4b-images/end-cutters.jpeg |
    | **a** |    :align: center                               | **b** |    :align: center                       |
    |       |    :width: 90%                                  |       |    :width: 90%                          |
    +-------+-------------------------------------------------+-------+-----------------------------------------+


:\:[   ]: Attach the PCB feet or bumper pads:

        -   If you have PCB feet, insert them into the mounting holes.

        -   If you have rubber or silicone adhesive bumper pads, attach four of them on the backside of the PCB near the corner mounting holes.
            Attach the remaining two bumper pads longitudinally center, near the edges of the PCB; you can use the through-holes that run along the edges of the Raspberry Pi Pico as a guide.

..  _mk4bFeet:
..  figure:: mk4b-images/feet-and-bumpers.jpeg
    :alt: a development board with nylon spacers as "feet", and another board with adhesive bumper pads
    :align: center
    :width: 60%

:\:[   ]: Remove the covering from the mini-breadboard's adhesive backing

:\:[   ]: Place the mini-breadboard in the rectangle labeled "Mini-Breadboard"

..  _mk4bBreadboard:
..  figure:: mk4b-images/breadboard.jpeg
    :alt: a mini-breadboard being held above a development board
    :align: center
    :width: 60%

|

----

Assembly is Complete
====================

You have now finished assembling the Cow Pi mark 4b.

..  _mk4bComplete:
..  figure:: mk4b-images/complete.jpeg
    :alt: a fully populated and assembled development board
    :align: center
    :width: 90%

    A fully populated and assembled Cow Pi mk4b development board.

|

..  _mk4bSchematic:
..  figure:: mk4b-images/CowPi-mk4b-schematic.jpg
    :alt: The schematic diagram of the Cow Pi mark 4b
    :align: center
    :width: 90%

    The schematic diagram of the Cow Pi mark 4b.
