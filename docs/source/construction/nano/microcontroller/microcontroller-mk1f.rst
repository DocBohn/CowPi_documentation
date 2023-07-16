..  include:: ../mk1ef.txt

Inserting the Microcontroller into the Breadboard
=================================================
*Cow Pi mk1f: Arduino Nano form factor*

A microcontroller, such as the |microcontrollerReference|_ on the |developmentBoard|, is a very simple processor when compared to a microprocessor designed for general-purpose computing.
At the same time, a microcontroller has some features not present on a microprocessor, such as built-in analog-to-digital converters (ADCs). [#noADC]_
A microcontroller board, such as the |developmentBoard|, combines the microcontroller with other components [#otherComponents]_ in a form factor convenient for experimentation.


..  include:: microcontroller-common.rst


:\:[   ]: Gently press on both ends of the |developmentBoard| to insert the pins into the contact points, using a slight rocking motion if necessary
   (:numref:`mk1fInsertingMicrocontroller`\ (a)).

:\:[   ]: Press the |developmentBoard| into the breadboard until it physically cannot be inserted any deeper
   (:numref:`mk1fInsertingMicrocontroller`\ (b)).


..  _mk1fInsertingMicrocontroller:
..  figure:: ../../../blank.png

    Inserting the microcontroller board into the breadboard.

    +---------------------------------------------------------+-----------------------------------------+
    | a                                                       | b                                       |
    +=========================================================+=========================================+
    | .. image:: inserting-nano.jpg                           | .. image:: nano-fully-inserted.jpg      |
    |    :height: 4cm                                         |    :height: 4cm                         |
    |    :align: center                                       |    :align: center                       |
    +---------------------------------------------------------+-----------------------------------------+
    | Press gently on both ends of the microcontroller board. | A microcontroller board fully inserted. |
    +---------------------------------------------------------+-----------------------------------------+


..  ATTENTION::
    **CHECKPOINT 1**
    | Before proceeding further, have a TA or a classmate verify that you have correctly inserted the |developmentBoard| into the breadboard.
    Update *checkpoints.txt* file to indicate who checked your work and when they did so.



..  [#noADC]
    | We will not use the ADCs in the I/O labs.
..  [#otherComponents]
    | Typically, a voltage regulator, a crystal oscillator, and a USB interface.