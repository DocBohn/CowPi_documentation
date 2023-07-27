Input Functions
===============

While one of the purposes of the Cow Pi boards is to teach memory-mapped I/O,
the CowPi library provides functions that work with the peripheral input/output devices for bootstrapping/scaffolding purposes.
These functions can, of course, also be used when memory-mapped I/O is not a required part of an assignment.

Even if you are working with memory-mapped I/O, you will benefit from using the :ref:`debouncing` code.

..  contents::


Simple Inputs
-------------

Using the pushbuttons and slide switches are straight-forward.

..  doxygenfunction:: cowpi_left_button_is_pressed
    :project: CowPi

..  doxygenfunction:: cowpi_right_button_is_pressed
    :project: CowPi

..  doxygenfunction:: cowpi_left_switch_is_in_left_position
    :project: CowPi

..  doxygenfunction:: cowpi_right_switch_is_in_left_position
    :project: CowPi

..  doxygenfunction:: cowpi_left_switch_is_in_right_position
    :project: CowPi

..  doxygenfunction:: cowpi_right_switch_is_in_right_position
    :project: CowPi

|

----


Scanned Inputs
--------------

We provide a function to scan the matrix keypad, returning the character for up to one pressed key.
This function will work with any Cow Pi board.

..  doxygenfunction:: cowpi_get_keypress
    :project: CowPi

|

We also provide a function to scan the matrix keypad, returning a bit vector that indicates the position of *each* of the sixteen keys.
This function is suitable only for Cow Pi mk3 and mk4 boards.

..  doxygenfunction:: cowpi_get_keypresses
    :project: CowPi

|

----

..  _debouncing:

Debouncing
----------

Mechanical inputs suffer from switch bounce.
As a cost-savings measure, hardware debouncing circuits are not present on the Cow Pi boards.
Consequently, debouncing must be implemented in software.

The two debouncing functions we provide are identical except for the size of the datatype they work with.
They require two inputs:
the first is an expression to determine the input's non-debounced value,
and the second is an enumerated value that uniquely identifies which input is being debounced.

..  seealso::
    The :ref:`io_test` example demonstrates the use of these debouncing functions.

..  doxygenfunction:: cowpi_debounce_byte
    :project: CowPi

..  doxygenfunction:: cowpi_debounce_short
    :project: CowPi

|

..  doxygenenum:: input_names
    :project: CowPi
