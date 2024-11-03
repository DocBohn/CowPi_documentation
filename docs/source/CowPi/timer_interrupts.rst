..  `_timer_interrupts`

Timer Interrupts
================

Configuring timer interrupts tends to be microcontroller-specific (see, for example, the section on the ATmega328P's :ref:`atmega328pTIMERS` and the RP2040's :ref:`rp2040TIMERS`).
The availability of convenience functions can be hit-or-miss.
For example, avr-libc offers no convenience functions to configure timers and enable timer interrupts, and it and offers only its primitive `ISR()` macro for registering timer ISRs.
On the other hand, Mbed OS provides convenience functions to manage timer interrupts and their ISRs, for both one-off timer events and for periodic timer events.

The Cow Pi library offers convenience functions to configure timers, enable interrupts, and register timer ISRs for periodic timer events.
The particulars are, nonetheless, dependent on the target's architecture.
There currently is no support for any microcontrollers' underlying waveform generation modes;
however, waveforms can easily be created with periodic timer interrupts.

..  IMPORTANT::

    As with all ISRs, you want to keep your interrupt handler short.
    An ISR that requires a significant fraction of the timer's period (or longer) to execute will cause undesirable behavior!


Sharing data with ISRs
----------------------

Regardless of whether you configure interrupts using the ``register_periodic_ISR`` function or a platform-specific mechanism,
data cannot be passed to the interrupt-handling code through parameters,
and the interrupt-handling code cannot return data through a return value.
This necessitates the use of global variables to provide data to, and obtain data from, the interrupt-handling code.

Because the compiler cannot detect any definition-use pairs for these global variables –
they are updated in one function and read in another, and no call chain exists between the two functions –
the compiler will optimize-away these variables and the code that accesses them in the interest of reducing the program's memory footprint.
The way to prevent this mis-optimization is to use the ``volatile`` keyword.

..  IMPORTANT::
    Any global variables that interrupt-handling code reads from and/or writes to *must* have the ``volatile`` modifier.

|

Differences in target architecture require differences in how the timer interrupts are set up.

Configuring AVR Timers and Registering ISRs for Interrupts
----------------------------------------------------------

AVR targets have multiple timers, each of which can support two or three periodic interrupts, depending on exactly how it's configured.
The ``configure_timer`` function provides a convenient way to configure any timer except TIMER0.
The timer period is not limited to a whole number of microseconds, and so the timer period (measured in microseconds) can be passed as a ``float`` value.
Unfortunately, the timers cannot take on arbitrary timer periods;
indeed, there are many intervals that *are* a whole number of microseconds that cannot be accurately assigned.
For this reason, ``configure_timer`` returns the timer's *actual* period, which will be the closet-possible timer period.

See the microcontroller-specific details (ATmega328P: :ref:`atmega328pTIMERS`) if you wish to determine the possible exact timer periods and which timer periods would permit three periodic interrupts for the timer.

..  doxygenfunction:: configure_timer
    :project: CowPi_AVR

After the timer is configured, ISRs can be registered with the ``register_periodic_timer`` function by specifying the timer, the ISR slot, and the ISR.
The function will return ``false`` if ISR slot 2 is specified but is unavailable, or if the timer has not been configured.
**The return value must be checked.**

..  doxygenfunction:: register_periodic_ISR
    :project: CowPi_AVR


Configuring ARM Timers and Registering ISRs for Interrupts
----------------------------------------------------------

ARM targets have a single timer that can support multiple interrupts.
Unlike AVR targets, only integer values can be used to specify the interrupt period (in microseconds);
however, every representable positive 32-bit integer (1 ≤ *T* < 4,294,967,296) can be used exactly as the timer period.
Because the hardware timer itself does not need to be configured, configuring the virtual timer and registering the ISR is accomplished with a single function.

..  doxygendefine:: MAXIMUM_NUMBER_OF_TIMERS
    :project: CowPi_MBED

8

..  doxygenfunction:: register_periodic_ISR
    :project: CowPi_MBED


Resetting the Timer Interrupt Period
------------------------------------

From time to time, you may have an application that requires you to "reset" the timer period;
that is, postpone the next interrupt until a full timer period after *now*.
On AVR targets, this can be accomplished simply by writing a 0 to the timer's counter register.
On ARM targets, writing a 0 to the timer's counter register is inadvisable since the (only) timer's counter is generally assumed to increment monotonically.

The CowPi library provides a platform-independent mechanism to accomplish this reset that will produce the desired effect in a manner consistent with the platform's requirements.

..  doxygenfunction:: reset_timer
    :project: CowPi


Counting TIMER0 Overflows on AVR Targets
----------------------------------------

You might wish to create a function that returns the elapsed time since the system was booted up.
On ARM targets, this can be implemented simply by reading the timer's counter value.
On AVR targets, the timers' counters overflow too frequently for this to be useful.

Instead, the CowPi library offers a way to obtain the number of times that TIMER0 has overflowed.
Based on the way that the Arduino framework configures TIMER0, we know that each increment of the counter corresponds to 4µs, and each overflow corresponds to 1024µs.

..  doxygenfunction:: initialize_timer0_overflow_count
    :project: CowPi_AVR

..  doxygenfunction:: get_timer0_overflow_count
    :project: CowPi_AVR
