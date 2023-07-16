..  include:: ../mk1ef.txt

Connect Power and Ground to Power Bus Strips
============================================
*Cow Pi mk1e/f: Arduino Nano form factor*

The columns marked with red and blue stripes are the power bus strips, also known as the power rails.
You will now provide power to the bus strips so that the other components can use power.

..  IMPORTANT::
    Before proceeding further, disconnect the USB cable from the |developmentBoard|.


:\:[   ]: Take the male-to-male rainbow cable, and peel off two wires.

:\:[   ]: Insert one end of a wire into contact point |mcuFiveVoltContactPoint|
    (notice that contact point |mcuFiveVoltContactPoint| is electrically connected to the |developmentBoard|'s ``5V`` pin, which is in contact point |mcuFiveVolt|).

:\:[   ]: Insert the other end of the ``5V`` wire into the upper |power| marked with a red stripe.

:\:[   ]: Now insert one end of the other wire into contact point |mcuUpperGroundContactPoint|
    (notice that contact point |mcuUpperGroundContactPoint| is electrically connected to one of the |developmentBoard|'s ``GND`` pins, which is in contact point |mcuUpperGround|).

:\:[   ]: Insert the other end of the ``GND`` wire into the upper |ground| marked with a blue stripe.
    See :numref:`powerConnections`.

..   _powerConnections:
..  figure:: power.jpg
    :height: 6cm

    Tapping power and ground from the |developmentBoard|.

..  NOTE::
    The lower |power| and the lower |ground| are *not* connected to anything.
    This is because we want to keep the rat's nest of jumper wires away from the slide-switches and pushbuttons.
    If you later attempt to use the lower |power| and the lower |ground| for power & ground, that will be ineffective.

..  ATTENTION::
    **CHECKPOINT 3**
    | Before proceeding further, have a TA or a classmate verify that you have correctly connected the |developmentBoard| to the upper |power| and the upper |ground|.
    Update *checkpoints.txt* file to indicate who checked your work and when they did so.



