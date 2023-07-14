Communication Protocols for Display Modules
===========================================

..  contents:: \

No Protocol
-----------

..  seealso::
    -   :struct:`cowpi_display_module_protocol_t`
    -   :func:`cowpi_configure_single_pin`

Principally, the :enumerator:`NO_PROTOCOL` choice is there to be a default value to detect that the application programmer failed to chose :enumerator:`SPI` or :enumerator:`I2C`.
The :enumerator:`MORSE_CODE` "display," however, legitimately uses neither SPI nor |i2c|.
If the protocol is :enumerator:`NO_PROTOCOL` and the display module is any option other than :enumerator:`MORSE_CODE`, then :func:`cowpi_add_display_module` will return ``NULL``.


SPI
---

..  seealso::
    -   :struct:`cowpi_display_module_protocol_t`
    -   :func:`cowpi_configure_spi`

.. For some reason, this convinces breathe/sphinx that there's a reference to be had, but no link is generated---
.. The Serial-Parallel Interface (SPI) protocol requires that the :c:member:`cowpi_display_module_protocol_t.data_pin`, ``clock_pin``, and the ``select_pin`` fields be specified;

The Serial-Parallel Interface (SPI) protocol requires that the ``cowpi_display_module_protocol_t.data_pin``, ``clock_pin``, and the ``select_pin`` fields be specified;
however, the ``data_pin`` and the ``clock_pin`` have default values, meaning that only the ``select_pin`` must be specified in all cases.

-   If the default bit-banged implementation is used, then the data and clock pins can be any available pins.
-   If the microcontroller’s SPI hardware is used, then your choice of data and clock pins may be limited.
-   The ``select_pin`` can still be any available pin, regardless of the implementation being used;
    this gives you the option of having multiple SPI devices.

Even if the bit-banged implementation is used, the default ``data_pin`` and ``clock_pin`` values are the pins that the microcontroller’s hardware uses (or uses by default when the hardware allows options).

For HD44780-based LCD character displays, the ``adapter_mapping`` field may also be specified;
its default value is :enumerator:`COWPI_DEFAULT`.

Terminology
"""""""""""

The data pin historically has been called ``MOSI`` (there is also ``MISO``, but not for the purposes of this library).
In 2020, the Open Source Hardware Association (OSHWA) proposed changing this to ``SDO`` (Serial Data Out) for devices that are strictly data-out on this pin, and to ``COPI`` (Controller-Out/Peripheral-In) for devices whose pin direction changes depending on their role as controller or peripheral.
In 2022, OSHWA changed its proposal to ``SDO`` and ``PICO`` (Peripheral-In/Controller-Out) after discovering that the abbreviation for Controller-In/Peripheral-Out is a vulgar and offensive word in some parts of the world.
Unfortunately, the potential for confusion with the "Pico" shorthand for "Raspberry Pi Pico" dissuades us from using ``PICO``.
Fortunately, this library uses the data pin in only one direction, and so we may refer to it as ``SDO`` but will typically refer to it as the "data pin".
The clock pin has been, and continues to be, referred to as ``SCK`` or ``CLK``.
The select pin historically has been called ``SS``, and the OSHWA’s proposal renames it as ``CS`` (Chip Select).

As of June 2023, Arduino has adopted "COPI" on the hardware side but still uses "MOSI" on the software side.
The Raspberry Pi Pico uses "TX" (Transmit).
Legacy datasheets still have the legacy terminology.


|i2c|
-----

..  seealso::
    -   :struct:`cowpi_display_module_protocol_t`
    -   :func:`cowpi_configure_i2c`

The Inter-Integrated Circuit (|i2c| or IIC) protocol, also known as the Two-Wire Interface (TWI) protocol, requires that the ``data_pin`` (SDA), ``clock_pin`` (SCL) and ``i2c_address`` fields be specified;
however, the ``data_pin`` and the ``clock_pin`` have default values, meaning that only the ``i2c_address`` must be specified in all cases.

-   If the default bit-banged implementation is used, then the data and clock pins can be any available pins.
-   If the microcontroller’s |i2c| hardware is used, then your choice of data and clock pins may be limited.
-   You have the option of having multiple I2C devices if the devices have different addresses.

Even if the bit-banged implementation is used, the default ``data_pin`` and ``clock_pin`` values are the pins that the microcontroller’s hardware uses (or uses by default when the hardware allows options).

For HD44780-based LCD character displays, the ``adapter_mapping`` field may also be specified;
its default value is :enumerator:`COWPI_DEFAULT`.

Specifying the Peripheral’s I2C Address
"""""""""""""""""""""""""""""""""""""""

When specifying the display module’s’s I2C address, you may, of course, hard-code the address if you know it.
Alternatively, if only one peripheral is on the I2C bus, then you may use the :func:`cowpi_discover_i2c_address` function inline to assign the address;
see the *scan_i2c* example for a demonstration of :func:`cowpi_discover_i2c_address`\ ’s functionality.

..  doxygenfunction:: cowpi_discover_i2c_address

..  NOTE::
    If there are multiple peripherals on the I2C bus then :func:`cowpi_discover_i2c_address` does not return a usable address.
    (Similarly, if there are no peripherals on the I2C bus, then it does not return a usable address, either.)

    If you need to determine the addresses of multiple peripherals, then we recommend that you run the Arduino Wire library’s
    `i2c_scanner <https://github.com/arduino/ArduinoCore-avr/blob/master/libraries/Wire/examples/i2c_scanner/i2c_scanner.ino>`__
    example to print the addresses of all devices on the I2C bus.