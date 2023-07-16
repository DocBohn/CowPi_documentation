The |developmentBoard| has a USB port to connect to a computer and/or to provide power to the |developmentBoard|.
|icspDescription|

|pinDescription|

-   |usartDescription|

-   |digitalPinDescription|

-   |analogPinDescription|

-   |regulatedVoltageDescription|

-   |unregulatedVoltageDescription|

-   The ``GND`` pins are for the common ground;
    the ground portions of external circuitry and of external power supplies must be electrically connected to the Arduino Nano's ground.

-   Finally, the ``RESET`` pins will reset the |developmentBoard| if grounded (pressing the button in the middle of the |developmentBoard| will also reset it).
    Note that, unlike a general-purpose computer, when a microcontroller is reset it will restart its program when the reset is released.

The |microcontroller| microcontroller on the |developmentBoard| is |microcontrollerProcessorAndMemory|.
|microcontrollerIntegerTiming|
|microcontrollerDivisionAndFloats|

|memoryModelDescription|
|pipelineDescription|
If you have already read Chapter 10, the |microcontroller| does not have cache memory; however, the data memory is SRAM, the same memory technology used in microprocessors' memory caches.
If you have already read Chapter 10, the |microcontroller| does not have a memory management unit for virtual memory; instead, the |microcontroller| uses only physical addressing.


Breadboard Terminology
----------------------

..  TIP::
    If you are not familiar with solderless breadboards, read the
    `Breadboards for Beginners <https://learn.adafruit.com/breadboards-for-beginners?view=all>`_
    Guide at adafruit.com.

Even though breadboards are often viewed in "landscape" orientation (such as in the photo in the inventory and as seen in the diagram figures) instead of "portrait" orientation,
the numbered sections are called rows and the lettered sections are called columns.
In the interest of preserving common usage, we will use this terminology.
We will refer to specific contact points using the letter-number combination.

Install the |developmentBoard| onto the Breadboard
--------------------------------------------------

:\:[   ]: Orient the breadboard in front of you so that row 1 is on your left and row 63 is on your right;
    column a should be at the bottom, and column j should be at the top.


:\:[   ]: Remove the anti-static foam from the |developmentBoard|'s pins.

You will place the |developmentBoard| on the left side of the breadboard with the USB connector on the left (that is, facing away from the breadboard).

:\:[   ]: Position the upper row of pins on contact points |mcuUpperRow| and the lower row of pins on contact points |mcuLowerRow|.

:\:[   ]: Double-check that:

   -  the pin labeled |mcuUpperLeftPin|  is in the upper-left, on contact point |mcuUpperLeft|
   -  the pin labeled |mcuLowerLeftPin|  is in the lower-left, on contact point |mcuLowerLeft|
   -  the pin labeled |mcuLowerRightPin| is in the lower-right, on contact point |mcuLowerRight|
   -  the pin labeled |mcuUpperRightPin| is in the upper-right, on contact point |mcuUpperRight|
