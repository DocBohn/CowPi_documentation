.. |i2c| replace:: :math:`\mathrm{I}^2\mathrm{C}`

Input Devices
=============

TODO

Switches and Buttons
--------------------

TODO

Theory of Operation
^^^^^^^^^^^^^^^^^^^

TODO

Reading the Devices' Positions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO

Matrix Keypad
-------------

TODO

Theory of Operation
^^^^^^^^^^^^^^^^^^^


After the code has determined which row and column the pressed key is on, it can return a value or assign a value to a variable accordingly.
This might be a ``char`` corresponding to the character on the key's face, as is the case for **``cowpi_get_keypress``** (Section `2.4 <#subsec:ScannedInputs>`__).
Or this might be an ``int`` corresponding to the value of the numeral on the key's face.
Or this might even be some value unrelated to whatever is printed on the key's face.


Scanning the Keypad
^^^^^^^^^^^^^^^^^^^

There are a few options for obtaining the value corresponding to a key that is pressed on the keypad.
The most efficient for a simple application is to use a lookup table.
For example, if you need to return a character that corresponds to the face value of the key that was pressed, then the lookup table would be:

.. math::

    keys :=
        \left(\begin{array}{cccc}
            '1' & '2' & '3' & 'A' \\
            '4' & '5' & '6' & 'B' \\
            '7' & '8' & '9' & 'C' \\
            '*' & '0' & '\#' & 'D'
        \end{array}\right)

If the keypad is wired to the microcontroller such that four contiguous output pins are connected to the rows and four contiguous input pins are connected to the columns (as is the case for the Cow Pi), then this pseudocode will scan the keypad and determine which key, if any, is pressed.

.. code-block::
    :linenos:

    ∀row:
        row_bit_vector := 0b1111    (* set all rows to 1 *)
        row_bit_vector(row) := 0    (* except the row we're currently examining *)
        wait at least one microcontroller clock cycle
        ∀column:
            if (column_bit_vector(column) = 0):
                key_pressed := keys(row,column)
    row_bit_vector := 0b0000        (* set all rows to 0 to detect the next keypress *)

.. NOTE::
    This pseudocode will report at most one key pressed;
    it would have to be modified to report multiple keys pressed.

    This software limitation is not a limitation for mark 1 Cow Pis, as mark 1 Cow Pis have a hardware limitation:
    their keypads have no protection against shorting power to ground when two keys are pressed simultaneously.


The delay shown in line 4 is sometimes, but not always necessary.
There is a slight delay between setting a pin's output value and being able to detect the change by reading a different pin's input value.
Some realizations of the pseudocode attempt to read the change before it can be read reliably;
this usually manifests as one of the keypad's columns not being readable.
The fix is to introduce a delay of at least one clock cycle (strictly speaking, one clock cycle is more than enough, but a shorter delay is not possible).
For our purposes, this should be managed by introducing a 1\ :math:`\mu`\ s delay using the Arduino core library's ``delayMicroseconds()``.
