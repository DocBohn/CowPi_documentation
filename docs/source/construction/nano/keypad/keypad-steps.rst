
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

        ..  image:: keypad-pullingwires.png
            :scale: 150%
            :align: center


:\:[   ]: Peel off two 4-conductor cables from the male-to-male rainbow cable.
    While you *can* use individual wires, having these 4-conductor cables will simplify keeping track of the wires.

    ..  TIP::
        Taping the each ends' four leads together may make it easier to manage the 4-conductor cables.
        (It is not necessary that you do so.)
        Ordinary household adhesive tape will suffice.

        ..  image:: keypad-cables.jpg
            :align: center


:\:[   ]: Insert one end of one of the 4-conductor cables in contact points |keypadRowRange|, in the same breadboard rows as the keypad's row pins.

:\:[   ]: Insert the other end of the cable in contact points |mcuKeypadRowContacts|.

    You want the |developmentBoard|'s |mcuRow1Pin| pin to connect to the keypad's ``row1`` pin, |mcuRow4Pin| to ``row4``, |mcuRow7Pin| to ``row7``, and |mcuRowStarPin| to ``row*``;
    you can use the wires' colors to make sure that you do so.

:\:[   ]: Insert one end of another 4-conductor cable in contact points |keypadColumnRange|, in the same breadboard rows as the keypad's column pins.

:\:[   ]: Insert the other end in contact points |mcuKeypadColumnContacts| (electrically connected to the |developmentBoard|'s |mcuColumnPinRange| pins).

    You want the |developmentBoard|'s |mcuColumn1Pin| to connect to the keypad's ``column1`` pin, |mcuColumn2Pin| to ``column2``, |mcuColumn3Pin| to ``column3``, and |mcuColumnAPin| to ``columnA``;
    you can use the wires' colors to make sure that you do so.
