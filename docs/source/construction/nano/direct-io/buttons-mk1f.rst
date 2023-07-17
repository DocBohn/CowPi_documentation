..  include:: ../mk1ef.txt
..  include:: ../mk1f.txt

Install the Momentary Pushbuttons
=================================
*Cow Pi mk1f: Arduino Nano form factor,* |i2c-italics| *communication*

..  include:: buttons-preamble.rst

Install the Buttons
-------------------

These are "normally open" momentary "switches" that close when pressed and re-open when released.
We will wire the pushbuttons such that they normally produce a 1, and when pressed will produce a 0.
:numref:`mk1fButtonDiagram` shows a diagram of the wiring for the pushbuttons.

.. _mk1fButtonDiagram:
.. figure:: ../../../blank.png

    Diagram of wiring associated with momentary pushbutton input.

    +-------+-------------------------------------------------------------------+
    |       | .. image:: ../fritzing_diagrams/CowPi-mk1ef-pushbutton-2lead.png  |
    | **a** |    :width: 90.0%                                                  |
    |       |                                                                   |
    |       | 2-lead pushbuttons                                                |
    +-------+-------------------------------------------------------------------+
    |       | .. image:: ../fritzing_diagrams/CowPi-mk1ef-pushbutton-4prong.png |
    | **b** |    :width: 90.0%                                                  |
    |       |                                                                   |
    |       | 4-prong pushbuttons                                               |
    +-------+-------------------------------------------------------------------+

..  _mk1fFigureButton:
.. figure:: ../../../blank.png

    Wiring the momentary pushbuttons

    +-------+---------------------------------+-------+----------------------------------+
    |       | .. image:: pushbutton-2lead.jpg |       | .. image:: pushbutton-4prong.jpg |
    | **a** |                                 | **b** |                                  |
    |       | Pushbuttons with two leads.     |       | Pushbuttons with four prongs.    |
    +-------+---------------------------------+-------+----------------------------------+
    |       | .. image:: pushbutton-wired.png                                            |
    | **c** |    :width: 90.0%                                                           |
    |       |                                                                            |
    |       | The momentary pushbuttons, wired to the |developmentBoard|.                |
    +-------+----------------------------------------------------------------------------+


..  include:: buttons-steps.rst


When you have finished setting up the pushbuttons' wiring, there should be the electrical paths described in :numref:`mk1fTablePushbuttons`.

..  _mk1fTablePushbuttons:
..  table:: Electrical Paths for Momentary Pushbuttons.

    +----------------+------------------------+-------------------+
    | Pushbutton     | |developmentBoard| pin | Power/Ground Rail |
    +================+========================+===================+
    | Left button's  |                        | |ground|          |
    | grounded lead  |                        |                   |
    +----------------+------------------------+-------------------+
    | Left button's  | |mcuLeftButtonPin|     |                   |
    | ungrounded     |                        |                   |
    | lead           |                        |                   |
    +----------------+------------------------+-------------------+
    | Right button's |                        | |ground|          |
    | grounded lead  |                        |                   |
    +----------------+------------------------+-------------------+
    | Right button's | |mcuRightButtonPin|    |                   |
    | ungrounded     |                        |                   |
    | lead           |                        |                   |
    +----------------+------------------------+-------------------+

..  include:: buttons-confirmation.rst
