..  include:: ../mk1ef.txt
..  include:: ../mk1f.txt

..  _mk1fKeypadSection:

Install the Matrix Keypad
=========================
*Cow Pi mk1f: Arduino Nano form factor,* |i2c-italics| *communication*


Observe that the matrix keypad has sixteen buttons has eight pins in its female connector.
As shown in :numref:`mk1fAnnotatedKeypad`\ (a), when the keypad is face-up and oriented for reading, the four pins on the left are the *row* pins, and the four pins on the right are the *column* pins.
From left-to-right, we will name these pins ``row1``, ``row4``, ``row7``, ``row*``, ``column1``, ``column2``, ``column3``, ``columnA``.
:numref:`mk1fAnnotatedKeypad`\ (b) shows the membrane contacts and which |developmentBoard| pin will be connected to each keypad pin.

.. _mk1fAnnotatedKeypad:
.. figure:: ../../../blank.png

    The numeric keypad's header has four row pins and four column pins

    +---------------------------------+-------------------------------------+
    | a                               | b                                   |
    +=================================+=====================================+
    | .. image:: keypad-annotated.jpg | .. image:: keypad-matrix.png        |
    |    :height: 7cm                 |    :height: 7cm                     |
    |    :align: center               |    :align: center                   |
    +---------------------------------+-------------------------------------+
    | Front of matrix keypad.         | Keypad's underlying contact matrix. |
    +---------------------------------+-------------------------------------+


:numref:`mk1fFigureKeypadDiagram` shows a diagram of the wiring for the matrix keypad.

..  _mk1fFigureKeypadDiagram:
..  figure:: ../fritzing_diagrams/CowPi-mk1ef-keypad.png
    :alt: Diagram of wiring associated with matrix keyboard input.
    :width: 90.0%

    Diagram of wiring associated with matrix keyboard input.


..  include:: keypad-steps.rst


When you have finished setting up the keypad wiring, there should be the electrical paths described in :numref:`mk1fTableKeypadConnections`.

..  _mk1fTableKeypadConnections:
..  table:: Electrical Paths for Matrix Keypad.

    =========== ========================
    Keypad pin  Arduino Nano pin
    =========== ========================
    ``row1``    |mcuRow1Pin|
    ``row4``    |mcuRow4Pin|
    ``row7``    |mcuRow7Pin|
    ``row*``    |mcuRowStarPin|
    ``column1`` |mcuColumn1Pin|
    ``column2`` |mcuColumn2Pin|
    ``column3`` |mcuColumn3Pin|
    ``columnA`` |mcuColumnAPin|
    =========== ========================

..  include:: keypad-confirmation.rst
