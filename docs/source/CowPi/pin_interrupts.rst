Pin Interrupts
==============

The Arduino framework's `attachInterrupt()` function is more convenient than the low-level mechanisms provided by avr-libc and other bare-metal frameworks.
Unfortunately, for some microcontroller boards, including the Arduino Uno and Nano, it is limited to working with only some pins.
For some other microcontroller boards, including the Raspberry Pi Pico, it appears to be buggy.

The CowPi library addresses this by providing functions to register and deregister interrupt service routines for any digital input pin.
No debouncing is provided, however, the :ref:`pin_interrupts` example demonstrates a macro.

Sharing data with ISRs
----------------------

Regardless of whether you configure interrupts using the :func:`cowpi_register_pin_ISR` function or a platform-specific mechanism,
data cannot be passed to the interrupt-handling code through parameters,
and the interrupt-handling code cannot return data through a return value.
This necessitates the use of global variables to provide data to, and obtain data from, the interrupt-handling code.

Because the compiler cannot detect any definition-use pairs for these global variables –
they are updated in one function and read in another, and no call chain exists between the two functions –
the compiler will optimize-away these variables and the code that accesses them in the interest of reducing the program's memory footprint.
The way to prevent this mis-optimization is to use the ``volatile`` keyword.

..  IMPORTANT::
    Any global variables that interrupt-handling code reads from and/or writes to *must* have the ``volatile`` modifier.


Registering ISRs for Interrupts
-------------------------------

The CowPi library's :func:`cowpi_register_pin_ISR` function allows for pin-based interrupts on any pin configured for digital input and abstracts away the configuration details.

To handle an interrupt, first write a function, such as ``handle_buttonpress()`` or ``handle_keypress()``.
This function must not have any parameters, and its return type must be ``void``.
Then, in the ``setup()`` function (or in one of its helper functions), register the interrupt with this code:

..  code-block:: c

    cowpi_register_pin_ISR(1L << pin_number, interrupt_handler_name);

or

..  code-block:: c

    cowpi_register_pin_ISR((1L << first_pin_number) | (1L << second_pin_number) | (1L << et_cetera), interrupt_handler_name);

This will configure all of the necessary registers to call the function whenever the input value on the pin ``pin_number`` (or on the pins ``first_pin_number``, ``second_pin_number``, ..., ``et_cetera``) goes from 0 to 1 or from 1 to 0.
The first argument is a bit vector that identifies which pin(s) are to be associated with the ISR:
if bit *n* is a 1, then pin *n* will be associated with the ISR.

As with all ISRs, you want to keep your interrupt handler short.
See the CowPi library's :ref:`pin_interrupts` example for demonstrations.


..  doxygenfunction:: cowpi_register_pin_ISR
    :project: CowPi

..  doxygenfunction:: cowpi_deregister_pin_ISR
    :project: CowPi
