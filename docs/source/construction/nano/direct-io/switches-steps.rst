..  IMPORTANT::
    Before proceeding further, disconnect the USB cable from the |developmentBoard|.


:\:[   ]: Insert one slider switch into contact points |leftSwitchRange|.

:\:[   ]: Place the other slider switch into contact points |rightSwitchRange|.

For the two wires that will connect the switches to the |developmentBoard|, you can use 10cm jumpers (especially if that is all that you have);
however, if you use 20cm jumpers, then when you |referenceKeypadSection| a couple of pages after this one, we will show how to keep some wires away from the controls.

:\:[   ]: Peel off one wire from the male-to-male rainbow cable and use it to connect contact point |leftSwitchLeftPin| (electrically connected to the left switch's left pin)
    to contact point |mcuLeftSwitchPoint| (electrically connected to the |developmentBoard|'s |mcuLeftSwitchPin| pin).

:\:[   ]: Peel off another wire from the male-to-male rainbow cable and use it to connect contact point |rightSwitchLeftPin| (electrically connected to the right switch's left pin)
    to contact point |mcuRightSwitchPoint| (electrically connected to the |developmentBoard|'s |mcuRightSwitchPin| pin).

:\:[   ]: Peel off two more wires from the male-to-male rainbow cable.

You will use these to connect the switches center pins to the upper |ground|.
Specifically,

:\:[   ]: Place the end of one wire into contact point |leftSwitchCenterPin|.

:\:[   ]: Place the other end of that wire into the upper |ground|.

:\:[   ]: Now place the end of the other wire into contact point |rightSwitchCenterPin|.

:\:[   ]: Place the other end of that wire into the upper |ground|.

The switches' right pins will not be electrically connected to anything.
