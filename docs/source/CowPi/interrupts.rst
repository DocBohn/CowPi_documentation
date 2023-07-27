Pin Interrupts
==============

The Arduino framework's `attachInterrupt()` function is more convenient than the low-level mechanisms provided by avr-libc.
Unfortunately, for some microcontroller boards, including the Arduino Uno and Nano, it is limited to working with only some pins.

The CowPi library addresses this by providing functions to register and deregister interrupt service routines for any digital input pin.
No debouncing is provided, however, the :ref:`pin_interrupts` example demonstrates a macro

..  doxygenfunction:: cowpi_register_pin_ISR
    :project: CowPi

..  doxygenfunction:: cowpi_deregister_pin_ISR
    :project: CowPi
