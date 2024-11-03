********************************
Microcontroller-Specific Details
********************************

Where the functions and data structures described in the :doc:`library` and :doc:`stdio` sections are applicable to any microcontroller that might be found on a Cow Pi board,
the discussion in this section focuses on details that are particular to a specific microcontroller or family of microcontrollers.
For each supported  microcontroller, we discuss I/O registers and the CowPi library's memory-mapped I/O data structures for them,
we discuss interrupts (going beyond the CowPi library's :doc:`CowPi/pin_interrupts` functions),
and we also discuss some uses of the microcontroller's timers.

.. toctree::
    :maxdepth: 2

    CowPi_atmega328p/io_registers
    CowPi_rp2040/io_registers
