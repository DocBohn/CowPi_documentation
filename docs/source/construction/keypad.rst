..  include:: mk1d.rst

Matrix Keypad
=============

Observe that the matrix keypad has sixteen buttons has eight pins in its female connector.
As shown in :numref:`annotatedKeypad`\ (a), when the keypad is face-up and oriented for reading, the four pins on the left are the *row* pins, and the four pins on the right are the *column* pins.
From left-to-right, we will name these pins ``row1``, ``row4``, ``row7``, ``row*``, ``column1``, ``column2``, ``column3``, ``columnA``.
:numref:`annotatedKeypad`\ (b) shows the membrane contacts and which |developmentBoard| pin will be connected to each keypad pin.

.. _annotatedKeypad:
.. figure:: ../blank.png

    The numeric keypad's header has four row pins and four column pins

    +----------------------------------------+-------------------------------------+
    | a                                      | b                                   |
    +========================================+=====================================+
    | .. image:: keypad/keypad-annotated.jpg | .. image:: keypad/keypad-matrix.png |
    |    :height: 7cm                        |    :height: 7cm                     |
    |    :align: center                      |    :align: center                   |
    +----------------------------------------+-------------------------------------+
    | Front of matrix keypad.                | Keypad's underlying contact matrix. |
    +----------------------------------------+-------------------------------------+


:numref:`figureKeypadDiagram` shows a diagram of the wiring for the matrix keypad.

..  _figureKeypadDiagram:
..  figure:: fritzing_diagrams/keypad.png
    :alt: Diagram of wiring associated with matrix keyboard input.
    :width: 90.0%

    Diagram of wiring associated with matrix keyboard input.


..  IMPORTANT::
    Before proceeding further, disconnect the USB cable from the |developmentBoard|.


:\:[   ]: If your 8-pin male-male header strip is not already inserted into the keypad's female connectors, insert it into the female connectors now.
    If your male-male header strip has more than eight pins, position the excess pins to the right of the column pins.

:\:[   ]: Connect your keypad to your breadboard such that
    ``row1`` is in contact point |keypadRow1Insertion|,
    and ``columnA`` is in contact point |keypadColumnAInsertion|
    (and any unused pins on the male-male header are in contact points |keypadExcessInsertions|).

    ..  TIP::
        If you used 20cm wires to connect your slide-switches and/or pushbuttons to the |developmentBoard|, then you can use the matrix keypad's ribbon cable to pull these wires away from the circuit, reducing clutter near the controls.

        ..  image:: keypad/keypad-pullingwires.png
            :scale: 150%
            :align: center


:\:[   ]: Peel off two 4-conductor cables from the male-to-male rainbow cable.
    While you *can* use individual wires, having these 4-conductor cables will simplify keeping track of the wires.

    ..  TIP::
        Taping the each ends' four leads together may make it easier to manage the 4-conductor cables.
        (It is not necessary that you do so.)
        Ordinary household adhesive tape will suffice.

        ..  image:: keypad/keypad-cables.jpg
            :align: center


:\:[   ]: Insert one end of one of the 4-conductor cables in contact points |keypadRowRange|, in the same breadboard rows as the keypad's row pins.

:\:[   ]: Insert the other end of the cable in contact points |mcuKeypadRowContacts|.

    You want the |developmentBoard|'s |mcuRow1Pin| pin to connect to the keypad's ``row1`` pin, |mcuRow4Pin| to ``row4``, |mcuRow7Pin| to ``row7``, and |mcuRowStarPin| to ``row*``;
    you can use the wires' colors to make sure that you do so.

:\:[   ]: Insert one end of another 4-conductor cable in contact points |keypadColumnRange|, in the same breadboard rows as the keypad's column pins.

:\:[   ]: Insert the other end in contact points |mcuKeypadColumnContacts| (electrically connected to the |developmentBoard|'s |mcuColumnPinRange| pins).

    You want the |developmentBoard|'s |mcuColumn1Pin| to connect to the keypad's ``column1`` pin, |mcuColumn2Pin| to ``column2``, |mcuColumn3Pin| to ``column3``, and |mcuColumnAPin| to ``columnA``;
    you can use the wires' colors to make sure that you do so.

When you have finished setting up the keypad wiring, there should be the electrical paths described in :numref:`tableKeypadConnections`.

..  _tableKeypadConnections:
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


..  ATTENTION::
    **CHECKPOINT 7**
    | Before proceeding further, have a TA or a classmate verify that you have correctly inserted and wired the matrix keypad.
    Update *checkpoints.txt* file to indicate who checked your work and when they did so.

..  WARNING::
    Do not press more than one key on the matrix keypad at a time.
    There are certain combinations of keys that could result in a short-circuit from power to ground, possibly damaging your |developmentBoard|.
    Your |developmentBoard| has some safety measures to prevent damage in that situation, but it would be better for you not to test those safety measures.

Connect your |developmentBoard| to the computer.
In the IDE's Serial Monitor,
notice that there is normally no character after ``Keypad:``, and that
Column pins is normally 1111.
Press the 5 key on the matrix keypad.
Notice that the first line of the message from the |developmentBoard| is now

::

       Keypad:      5        Column pins:  1011    Keypad NAND: 1

In general, when you press a key on the keypad, the corresponding character will be displayed after ``Keypad:``.
When you press 1, 4, 7, or \*, Column pins becomes 0111;
similarly, pressing a key in the 2\ :math:`^{nd}` column causes Column pins to become 1011;
in the 3\ :math:`^{rd}` column, 1101;
and in the A\ :math:`^{th}` column, 1110.
Be sure to test all 16 keys.
