Output Devices
==============

Unless implementing :doc:`../expansion`, the Cow Pi circuit's output devices are simple light emitting diodes and a display module, described here.

..  _LEDs:

Light Emitting Diodes (LEDs)
----------------------------

An idealized diode allows current to flow in only one direction,\ [#reverseCurrent]_ which is why we keep track of which end is tha anode and which is the cathode.

..  _diode:
..  tikz:: In a diode, conventional current flows from the anode to the cathode (or, equivalently, electrons enter through the cathode and leave through the anode).
    :align: center

    \begin{tikzpicture}[x=.05in, y=.05in]
        \draw (5,0) -- (2,0);
        \draw (-5,0) -- (-2,0);
        \draw (-2,2) -- (-2,-2) -- (2,0) -- (-2,2);
        \draw (2,2) -- (2,-2);
        \draw (8.8,0) node {\tiny cathode};
        \draw (-8,0) node {\tiny anode};
    \end{tikzpicture}

A light emitting diode, or LED, is a diode designed to emit light.\ [#goodName]_

..  _led:
..  tikz:: A light emitting diode emits light when current flows
    :align: center

    \begin{tikzpicture}[x=.05in, y=.05in]
        \draw (5,0) -- (2,0);
        \draw (-5,0) -- (-2,0);
        \draw (-2,2) -- (-2,-2) -- (2,0) -- (-2,2);
        \draw (2,2) -- (2,-2);
        \draw (1,2) -- ++(1,1) -- ++(.25,-.25) -- ++(.25,.75) -- ++(-.75,-.25) -- ++(.25,-.25);
        \draw (.1,2.5) -- ++(1,1) -- ++(.25,-.25) -- ++(.25,.75) -- ++(-.75,-.25) -- ++(.25,-.25);
    \end{tikzpicture}

Theory of Operation
^^^^^^^^^^^^^^^^^^^

A full discussion of the material science behind semiconductors is beyond the scope of this datasheet.
The short version is that when making solid state electronics, the extrinsic semiconductor metal is *doped* with impurities.
Some dopants cause the semiconductor material to have excess electrons in the valent shell, creating a region with excess negative charge ("N-type").
Other dopants cause the semiconductor material to a shortage of electrons in the valent shell -- typically expressed as an excess of *holes* -- creating a region with excess positive charge ("P-type").

In a diode, when the voltage at the anode is sufficiently higher than the voltage at the cathode, electrons in the N region are able to leave the valent shell, cross the depletion region at the PN junction, and fill a hole.
Meanwhile, new electrons enter through the cathode, replacing those that crossed the PN junction, and electrons leave through the anode, causing new holes to replace those that were filled.
The mental image is of electrons moving away from the cathode toward the PN junction, and of holes moving away from the anode toward the PN junction.

Because of the quantum nature of electron shells, light will *always* be emitted when an electron fills a hole.
In ordinary diodes, we don't see this light because it might not be in the visible spectrum, most of the light is "lost" to internal reflection in the semiconductor material, and the opaque casing blocks what little light might be emitted.
In LEDs, the dopants are selected to cause the emission to be at a very particular frequency.\ [#blueLED]_
Additional material is added to the semiconductor material to reduce internal reflection at that frequency.
And, of course, the casing is translucent.

To avoid damaging the LED, the amount of current flowing through it must be limited -- each LED's datasheet specifies the maximum forward current.
A very conventional approach, which is used in the Cow Pi circuit, is to add a current limiting resistor.
Ohm's Law allows us to determine the minimum resistance needed: :math:`R \geq \frac{V_{CC}}{I_{f_{max}}}`
Your actual choice of resistance strikes a balance between the desired brightness, not stressing the microcontroller's ability to dissipate heat at the pins, and not dipping too deep into your electrical current budget. [#currentBudget]_


Illuminating/Deluminating an LED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have an external power source other than the microcontroller board's voltage regulator, then using a transistor to enable and disable current flow through the LED is a good way to reduce the current at the microcontroller's pins to a few microamps.
If all current is sourced from a USB cable through the microcontroller board, then using a transistor in that manner only adds to the circuit's complexity while offering little benefit.
For this reason, we drive the LEDs directly from the microcontroller board's pins.

There are advantages to designing the circuit so that placing the pin at logic high causes the LED to illuminate,
and there are advantages to designing the circuit so that placing the pin at logic low causes the LED to illuminate.
In the end, we chose to be consistent with the built-in LEDs on the microcontroller boards used for the Cow Pi:
logic high (boolean 1) causes the LED to illuminate, and logic low (boolean 0) causes the LED to deluminate.

The CowPi library's :func:`cowpi_setup` function configures the pins that drive the LEDs as output pins, along with other configuration settings.
That done, illuminating/deluminating an LED is as simple as setting the pin's logic value.
If you are not writing code using memory-mapped I/O, then you would do this with Arduino's ``digitalWrite()`` function or the Raspberry Pi SDK's ``gpio_put()`` function.
If you are writing code using memory-mapped I/O, then you would set the pin's bit in the I/O bank's output register, as described in the :doc:`../microcontroller` Section.
If the LED should be dark, then set the bit to 0.
If the LED should be lit up, then set the bit to 1.

..  NOTE::
    When using the Arduino Nano or Arduino Uno microcontroller board, the pin used for the internal LED (the Cow Pi's left LED) is also used as the clock pin for SPI communication.
    If you are making frequent updates to the display module through SPI, this will likely render the left LED unusable.
    You can safely assume that any lab assignments will take this into account.

..  NOTE::
    When using the Arduino Nano or Arduino Uno microcontroller board, the pin used for the Cow Pi's right LED is also used as the data pin for the Controller-In/Peripheral-Out SPI mode.
    Unless needed for one of the :doc:`../expansion`, we will not use this particular SPI mode.
    However, when SPI is enabled, the SPI hardware overrides that pin's settings, changing it to an input pin.

    As described in the :ref:`atmega328pSPI` Section for the ATmega328P, the CowPi_stdio library handles this by enabling SPI only long enough to transmit data to the display module, and disabling SPI immediately thereafter.
    You may notice the right LED briefly dimming when you send updates to the display module through the SPI.

To Learn More
^^^^^^^^^^^^^

Adafruit and SparkFun have pages where you can learn more about LEDs:

-   `All About LEDs <https://learn.adafruit.com/all-about-leds?view=all>`_ at Adafruit
-   `Light-Emitting Diodes (LEDs) <https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds>`_ at SparkFun

|

Display Modules
---------------

While it is possible to perform textual output (and input) through the serial terminal, we find it more interesting -- and usually more meaningful -- to provide textual and numerical output on a display module in the Cow Pi circuit, leaving the serial terminal for debugging and logging purposes.
While the :doc:`../stdio` provides functions for fine-grained control of the display modules, we recommend using the higher-level interface that makes use of C file streams.

Each of the display modules described below makes use of the Serial-Parallel Interface (SPI) and/or the Inter-Integrated Circuit (|i2c|) protocol to send data to the display modules using as few wires as possible.
We have found that an interesting memory-mapped I/O exercise is to manipulate the registers for these communication protocols to send data to the display modules.

Specific Display Modules
^^^^^^^^^^^^^^^^^^^^^^^^

The overall Cow Pi hardware design is largely flexible for the choice of display module.
We generally assume there is only one display module in the circuit, but this is not a hard-and-fast requirement.
The CowPi_stdio library, however, only supports a limited number of display modules --
those currently available are so either because we have used them in lab assignments (such as the 8-digit/7-segment display and the LCD character display)
or because they are relatively low-hanging fruit from earlier efforts put into the library (such as the LED matrix display).

|

..  _hd44780:

HD44780-driven LCD Character Display
""""""""""""""""""""""""""""""""""""

..  seealso::
    :doc:`../CowPi_stdio/lcd_character`

The |hd44780Reference|_ "dot-matrix liquid crystal display controller and driver LSI displays alphanumerics, Japanese kana characters, and symbols."
It can receive updates with 12 bits (4 control bits plus a byte to be acted upon) or with 8 bits (4 control bits plus a halfbyte to be acted upon).
While these display modules *can* be driven directly from a microcontroller, Cow Pi circuits use a serial adapter (either a |74hc595Reference|_ or |74ahct595Reference|_ shift register for SPI, or a |pcf8574Reference|_, or an |adafruitAdapterReference|_).

The CowPi_stdio :func:`add_display_module` function (which is called by the CowPi :func:`cowpi_setup` function) configures a HD44780-based display module so that it can be controlled with 8 bits in parallel.
One of the tradeoffs is that each character or command byte must be transmitted as two halfbytes.
The CowPi_stdio library takes care of dividing the full byte into two halfbytes and passing each halfbyte to :var:`cowpi_hd44780_send_halfbyte` in the appropriate order.

..  IMPORTANT::
    When a halfbyte is passed to :var:`cowpi_hd44780_send_halfbyte`, it will be in the lower 4 bits of the ``halfbyte`` argument, regardless of which of the two halfbytes it is.

The serial adapter converts the serial data coming from the microcontroller into the parallel data that the display module requires.
For this to be effective, the function must pack the bits in the order that the serial adapter expects.

Data Byte for LCD1602 Display Module
''''''''''''''''''''''''''''''''''''

The ``COWPI_DEFAULT`` bit order is described in :numref:`tableHD44780Bits`.
When constructing a byte to place in the SPI or |i2c| Data Register:

..  _tableHD44780Bits:
..  flat-table:: The ``COWPI_DEFAULT`` mapping of |i2c| data bits to HD44780 bits.
    :stub-columns: 1
    :align: center

    *   -   Data Register
        -   Bit7
        -   Bit6
        -   Bit5
        -   Bit4
        -   Bit3
        -   Bit2
        -   Bit1
        -   Bit0
    *   -   HD44780 Bit
        -   D7
        -   D6
        -   D5
        -   D4
        -   BT
        -   EN
        -   RW
        -   RS
    *   -   Bit source
        -   :cspan:`3` ``halfbyte << 4``
        -   backlight on/off
        -   latch data
        -   read/write
        -   ``!is_command``

Bits 7..4
    The upper four bits are the ``halfbyte`` argument passed to **COWPI_HD44780_SEND_HALFBYTE()**, left-shifted four places.

Bit 3
    Bit 3 is a 1 if you want the display module's backlight to illuminate, or 0 if you want it deluminated.\ [#backlight]_

Bit 2
    As described below, bit 2 is used to send a pulse to the HD44780 that instructs the display module that it should latch-in the halfbyte that it has received.

Bit 1
    Bit 1 informs the HD44780 whether data is being sent to it, or if a data request is being made of it;
    while it is possible to query the display module's memory, the CowPi_stdio library does not support this feature, and bit 1 should always be 0.

Bit 0
    Bit 0 informs the HD44780 whether the halfbyte that it receives is part of a command or is part of a character;
    if the ``is_command`` argument passed to **COWPI_HD44780_SEND_HALFBYTE()** is ``true``, then bit 0 should be 0; otherwise, bit 0 should be 1.


Data Byte Sequence
''''''''''''''''''

..  IMPORTANT::
    If you are going to write code to transmit data to a display module, see the :doc:`../microcontroller` for the specific mechanism to transmit a data byte for your particular microcontroller.

When the function executes the SPI Controller-Out/Peripheral-In sequence or the |i2c| controller-transmitter sequence (see the pseudocode in the :ref:`atmega328pControllerTransmitterSequence` Section), it will have three (3) data bytes to transmit.

#.  First, the halfbyte needs to be sent *without* yet instructing the display module to latch-in the halfbyte:

    ..  code-block:: pascal

        bitwise_or(
            (halfbyte << 4),
            ((1 if backlight_on else 0) << 3),
            (0 << 2), (* not yet latching halfbyte *)
            (0 << 1),
            ((0 if is_command else 1) << 0)
        )

#.  Second, the start of the "latch pulse" needs to be sent:

    ..  code-block:: pascal

        bitwise_or(
            (halfbyte << 4),
            ((1 if backlight_on else 0) << 3),
            (1 << 2), (* latch the halfbyte *)
            (0 << 1),
            ((0 if is_command else 1) << 0)
        )

    -   **The pulse needs to stay active for at least 0.5𝜇s.**
        While there is a low-level `AVR-libc function <https://www.nongnu.org/avr-libc/user-manual/group__util__delay.html>`_ that can introduce a delay of nearly exactly 0.5𝜇s,
        we recommend introducing a 1𝜇s delay using the |delayMicroseconds|_, which is portable across all devices using the Arduino framework.

#.  Third, the end of the "latch pulse" needs to be sent:

    ..  code-block:: pascal

        bitwise_or(
            (halfbyte << 4),
            ((1 if backlight_on else 0) << 3),
            (0 << 2), (* complete the latch *)
            (0 << 1),
            ((0 if is_command else 1) << 0)
        )

|

MAX7219-driven 8-Digit/7-Segment Display
""""""""""""""""""""""""""""""""""""""""

..  TODO:: \

..  seealso::
    :doc:`../CowPi_stdio/seven_segment`

MAX7219-driven LED Matrix
"""""""""""""""""""""""""

..  TODO:: \

..  seealso::
    :doc:`../CowPi_stdio/led_matrix`

SSD1306-driven OLED Graphic Display
"""""""""""""""""""""""""""""""""""

..  TODO:: \

Communication Protocols
^^^^^^^^^^^^^^^^^^^^^^^

..  TODO:: \

Serial-Parallel Interface (SPI)
"""""""""""""""""""""""""""""""

..  TODO:: \

Inter-Integrated Circuit (|i2c|)
""""""""""""""""""""""""""""""""

..  TODO:: \

|

----

..  |hd44780Reference|          replace:: HD44780
..  _hd44780Reference:          https://www.sparkfun.com/datasheets/LCD/HD44780.pdf

..  |74hc595Reference|          replace:: 74HC595
..  _74hc595Reference:          https://www.ti.com/lit/ds/symlink/sn74hc595.pdf

..  |74ahct595Reference|        replace:: 74AHCT595
..  _74ahct595Reference:        https://www.ti.com/lit/ds/symlink/sn74ahct595.pdf

..  |pcf8574Reference|          replace:: PCF8574-based |i2c| adapter
..  _pcf8574Reference:          http://www.handsontec.com/dataspecs/module/I2C_1602_LCD.pdf

..  |adafruitAdapterReference|  replace:: Adafruit I2C/SPI Adapter
..  _adafruitAdapterReference:  https://www.adafruit.com/product/292

..  |delayMicroseconds|         replace:: Arduino ``delayMicroseconds()`` function
..  _delayMicroseconds:         https://www.arduino.cc/reference/en/language/functions/time/delaymicroseconds/



..  [#reverseCurrent] In practice, diodes will almost always allow a few microamps of reverse current, and under the right conditions, diodes will allow significant current to flow in the reverse direction.
        For some types of diodes, reverse current is a feature and happens at relatively-low reverse voltages.
        For other types of diodes, the necessary reverse voltage is much higher, and the resulting reverse current will flow only briefly before no current can flow at all.
        Since we do not apply reverse voltages to any diodes in the Cow Pi, these are not concerning matters at the moment.

..  [#goodName] See? It *is* possible to come up with meaningful names.

..  [#blueLED] You may take it for granted that white LEDs exist, and that we have "LED lights" that can produce any visible color.
        LEDs that emit blue light that are inexpensive and sufficiently bright are a relatively recent development.
        "White LEDs" are actually three LEDs (red, green, and blue) in a single casing.
        Similarly, variable-color LED lights are comprised of red, green, and blue LEDs in which the current passing through each of the LEDs is adjusted to change its brightness;
        each color is the result of the relative contributions of each of the primary colors.

..  [#currentBudget] There are two considerations for how much current to allow.
        The first is that, if you are driving the LED directly from a microcontroller pin, there is an upper limit to the amount of current that a pin can safely source, and an upper limit to the amount of current that a pin can safely sink.
        The other consideration is that if your circuit has no power source other than a USB cable, you should expect no more than 500mA at 5V (or about 750mA at 3.3V if losslessly stepped-down) to be available for the microcontroller and all of the peripherals.

..  [#backlight]
    While the ``cowpi_hd44780_set_backlight()`` function can be used to turn the backlight on and off, bit 3 needs to preserve the appropriate setting.
