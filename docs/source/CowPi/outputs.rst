Output Functions
================

While one of the purposes of the Cow Pi boards is to teach memory-mapped I/O,
the CowPi library provides functions that work with the peripheral input/output devices for bootstrapping/scaffolding purposes.
These functions can, of course, also be used when memory-mapped I/O is not a required part of an assignment.

..  NOTE::
    LEDs are handled by the CowPi library, and their functions are described here.

    Display modules are handled by the :doc:`../stdio` library.

|

..  doxygenfunction:: cowpi_illuminate_right_led
    :project: CowPi
 
..  doxygenfunction:: cowpi_illuminate_left_led
    :project: CowPi
 
..  doxygenfunction:: cowpi_deluminate_right_led
    :project: CowPi
 
..  doxygenfunction:: cowpi_deluminate_left_led
    :project: CowPi
 
..  doxygenfunction:: cowpi_illuminate_internal_led
    :project: CowPi
 
..  doxygenfunction:: cowpi_deluminate_internal_led
    :project: CowPi
