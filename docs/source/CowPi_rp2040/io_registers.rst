RP2040 (Raspberry Pi Pico)
==========================

..  contents::
    :depth: 3

Input/Output Register Descriptions
----------------------------------

The RP2040 microcontroller has a robust set of memory-mapped input/output registers.
While many of these might be seen on nearly any microcontroller, some exist specifically to support the presence of two processor cores.

The tables below include each register's address in the RP2040's data memory address space.

External Pins Input/Output
""""""""""""""""""""""""""

..  _tableRP2040IORegisters:
..  flat-table:: Abbreviated set of RP2040 external pin I/O registers. Original data from |microcontrollerReference|_\ , §2.3.1.
    :header-rows: 1

    *   -   Name
        -   Address
        -   Bits 31..30
        -   Bits 29..0
    *   -   CPUID
        -   0xD0000000
        -   :cspan:`1` Processor core identifier
    *   -   GPIO_IN
        -   0xD0000004
        -   Unused
        -   Input values for GPIO pins
    *   -   GPIO_OUT
        -   0xD0000010
        -   Unused
        -   Output values for GPIO pins
    *   -   GPIO_OUT_SET
        -   0xD0000014
        -   Unused
        -   Atomic bit-set on GPIO_OUT (atomically perform ``GPIO_OUT |= data``)
    *   -   GPIO_OUT_CLR
        -   0xD0000018
        -   Unused
        -   Atomic bit-clear on GPIO_OUT (atomically perform ``GPIO_OUT &= ~data``)
    *   -   GPIO_OUT_XOR
        -   0xD000001C
        -   Unused
        -   Atomic bitwise XOR on GPIO_OUT (atomically perform ``GPIO_OUT ^= data``)
    *   -   GPIO_OE
        -   0xD0000020
        -   Unused
        -   Enable output for GPIO pins
    *   -   GPIO_OE_SET
        -   0xD0000024
        -   Unused
        -   Atomic bit-set on GPIO_OE
    *   -   GPIO_OE_CLR
        -   0xD0000028
        -   Unused
        -   Atomic bit-clear on GPIO_OE
    *   -   GPIO_OE_XOR
        -   0xD000002C
        -   Unused
        -   Atomic bitwise XOR on GPIO_OE


..  _`rp2040MmapIOStruct`:

Structure for Memory-Mapped Input/Output
''''''''''''''''''''''''''''''''''''''''

The CowPi library provides data structures to access the memory-mapped I/O registers in a more readable form.
Specifically, the |ioport|_ structure is used to communicate with peripheral devices attached to the I/O pins that do not make use of a particular communication protocol.

..  _`rp2040_ioport_t`:

..  doxygenstruct:: cowpi_ioport_t
    :project: CowPi_rp2040
    :no-link:
    :members:

The |ioport|_ structure can be made to overlay the external pins' registers by creating a pointer to the lowest-addressed register (``0xD0000000``, per :numref:`tableRP2040IORegisters`).
Hypothetically, if ``GP22`` were an input pin, then we could determine the pin's logic level with C code similar to this:

..  code-block:: c
    :linenos:

    volatile cowpi_ioport_t *ioport = (cowpi_ioport_t *)(0xD0000000);
    uint32_t logic_level = ioport->input & (1 << 22);

In the first line, we created a pointer to a |ioport|_ structure and assigned the structure's base address to ``0xD0000000``.
Most likely, you would only need to do this once per program.
In the second line, we select the ``input`` field because in this hypothetical, pin ``GP22`` is an input pin.
We use a bitmask so that we only capture the logic level of the pin we're interested in.
Both ``0x0040'0000`` and ``0b0000'0000'0100'0000'0000'0000'0000'0000`` would be entirely suitable literal masks.
Here we a mask created from a bitshift (*i.e.*, ``(1 << 22)``) to reduce the likelihood of making an error.

Of course, in this example, ``logic_level`` would take on either a zero or non-zero value, which is fine for most applications.
If ``logic_level`` must take on either zero or one, then you could either shift the bits:

..  code-block:: c
    :lineno-start: 3

    uint32_t logic_level = (ioport->input & (1 << 22)) >> (1 >> 22);

or double-negate:

..  code-block:: c
    :lineno-start: 3

    uint32_t logic_level = !!(ioport->input & (1 << 22));

On the other hand, if ``GP22`` were an output pin, then we could set the pin's logic level with C code similar to this:

..  code-block:: c
    :linenos:

    volatile cowpi_ioport_t *ioport = (cowpi_ioport_t *)(0xD0000000);
    // to clear pin 22 to a 0:
    ioport->output &= ~(1 << 22);
    // to set pin 22 to a 1:
    ioport->output |= 1 << 22;
    // to toggle pin 22's value:
    ioport->output ^= 1 << 22;

This code uses the read/modify/write pattern:
Obtain the existing output values for the relevant bank of pins,
then create a bit vector that can be used to set 0 or 1 in the specific bit while preserving all of the other pins' output values,
and then finally assign the resulting bit vector to the bank's output register.
If the new logic level is in a variable and you don't know whether you're assigning a 0 or a 1,
a good choice would be to clear the relevant bit to 0 and then use a bitwise OR to assign the appropriate value to the specific bit:

..  code-block:: c
    :lineno-start: 3

    uint32_t logic_level = ... // assume logic_level is strictly 0 or 1
    ioport->output = (ioport->output & ~(1 << 22)) | (logic_level << 22);


Special Consideration for Concurrency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The read/modify/write pattern is three distinct operations:

-   Loading loading the content of the ``output`` register into one of the processor's general-purpose registers,
-   Applying a bitwise operation, and
-   Storing the result in the ``output`` register

For example,

..  code-block:: c
    :lineno-start: 5

    ioport->output |= 1 << 22;

compiles to

..  code-block:: asm
    :lineno-start: 8
    :emphasize-lines: 2, 4, 5

    movs    r2, #128
    ldr     r1, [r3, #16]
    lsls    r2, r2, #15
    orrs    r2, r1
    str     r2, [r3, #16]

When running bare-metal on most microcontrollers, and when running bare-metal on the RP2040 if only one processor core is used, this would not be a problem.
With the RP2040, concurrency is possible by two mechanisms:

-   The RP2040 has two processor cores, so two processes can execute concurrently when running bare-metal
-   The official Arduino toolchain for the RP2040 is built on top of Mbed OS, which supports threading

To prevent race conditions, three atomic output registers are available.
Assigning a bit vector to one of these will atomically set one or more output pins to 1 (``ioport->atomic_set``), to 0 (``ioport->atomic_clear``), or to its/their opposite logic value(s) (``ioport->atomic_toggle``):

..  code-block:: c
    :linenos:

    volatile cowpi_ioport_t *ioport = (cowpi_ioport_t *)(0xD0000000);
    // to clear pin 22 to a 0:
    ioport->atomic_clear = 1 << 22;
    // to set pin 22 to a 1:
    ioport->atomic_set = 1 << 22;
    // to toggle pin 22's value:
    ioport->atomic_toggle = 1 << 22;


Mapping Input/Output Devices to I/O Port Array
''''''''''''''''''''''''''''''''''''''''''''''

The :ref:`rp2040MmapIOStruct` Section describes a structure definition that can be used to access the inputs and outputs attached to the Raspberry Pi Pico's pins.
:numref:`PicoPinout` shows which input/output devices are attached to the various Raspberry Pi Pico pins.
Combining this information, we arrive at the mapping in :numref:`tableRP2040MapDevicesToStruct` that is suitable for the Cow Pi mk3c and for the Cow Pi mk4b.

..  _tableRP2040MapDevicesToStruct:
..  flat-table:: A mapping of input/output devices to fields in the I/O ports structure.
    :header-rows: 1

    *   -   Field
        -   :cspan:`3` \
    *   -
        -   **Bit 31**
        -   **Bit 30**
        -   **Bit 29**
        -   **Bit 28**
    *   -   ``input``
        -   :rspan:`1` :cspan:`1` Unused
        -
        -
    *   -   ``output``
        -
        -
    *   -
        -   **Bit 27**
        -   **Bit 26**
        -   **Bit 25**
        -   **Bit 24**
    *   -   ``input``
        -
        -
        -
        -
    *   -   ``output``
        -
        -
        -   Internal LED
        -
    *   -
        -   **Bit 23**
        -   **Bit 22**
        -   **Bit 21**
        -   **Bit 20**
    *   -   ``input``
        -
        -
        -
        -
    *   -   ``output``
        -
        -
        -   Left LED
        -   Right LED
    *   -
        -   **Bit 19**
        -   **Bit 18**
        -   **Bit 17**
        -   **Bit 16**
    *   -   ``input``
        -
        -   :rspan:`1` SPI Clock Pin
        -   :rspan:`1` SPI Latch Pin
        -   SPI Data In
    *   -   ``output``
        -   SPI Data Out
        -
    *   -
        -   **Bit 15**
        -   **Bit 14**
        -   **Bit 13**
        -   **Bit 12**
    *   -   ``input``
        -   Right Switch
        -   Left Switch
        -   Keypad Column A
        -   Keypad Column 3
    *   -   ``output``
        -
        -
        -
        -
    *   -
        -   **Bit 11**
        -   **Bit 10**
        -   **Bit 9**
        -   **Bit 8**
    *   -   ``input``
        -   Keypad Column 2
        -   Keypad Column 1
        -
        -
    *   -   ``output``
        -
        -
        -   Keypad Row *
        -   Keypad Row 7
    *   -
        -   **Bit 7**
        -   **Bit 6**
        -   **Bit 5**
        -   **Bit 4**
    *   -   ``input``
        -
        -
        -   :rspan:`1` :cspan:`1` controlled by |i2c| for display module
    *   -   ``output``
        -   Keypad Row 4
        -   Keypad Row 1
    *   -
        -   **Bit 3**
        -   **Bit 2**
        -   **Bit 1**
        -   **Bit 0**
    *   -   ``input``
        -
        -
        -
        -
    *   -   ``output``
        -   Right Button
        -   Left Button
        -
        -

..  NOTE::
    If you are using a Raspberry Pi Pico-W instead of a Raspberry Pi Pico, then Bit 25 does *not* control the internal LED.

|

..  _rp2040SPI:

Serial-Parallel Interface
"""""""""""""""""""""""""

The RP2040 has two sets of SPI registers;
however, only one is available for use in a Cow Pi circuit.
In this datasheet, we use the conventional terms "Serial-Parallel Interface," or SPI, as does |microcontrollerReference|_ in general; however,
the SPI controllers are based on an ARM PrimeCell Synchronous Serial Port PL022, as described in |sspReference|_
We mention this because the SPI registers, have names derived from "SSP."
The registers include:

``SSPCR0``
    The SPI Control Register 0 is used to configure the SPI hardware.

``SSPCR1``
    The SPI Control Register 1 is used to configure the SPI hardware.

``SSPDR``
    The SPI Data Register is used to transfer data to and from an SPI peripheral device.

``SSPSR``
    The SPI Status Register is used to indicate the status of a data transfer.

``SSPCPSR``
    The SPI Prescale Register is used to configure the SPI hardware.

We omit discussion of the remaining registers, which are used for SPI interrupts, SPI direct memory access, and ARM's PrimeCell Synchronous Serial Port identification.

The SPI hardware has four modes of operation: controller output/peripheral input and controller input/peripheral output as the controller; and controller output/peripheral input and controller input/peripheral output as the peripheral.\ [#terminology]_
The discussion in this datasheet will focus on the controller output/peripheral input mode with the microcontroller as the controller.
See Chapter 18 of the |microcontrollerReference|_\ , §4.4 for other modes.

.. _`rp2040SPIStruct`:

Structure for Memory-Mapped Input/Output
''''''''''''''''''''''''''''''''''''''''

The CowPi library provides data structures to access the memory-mapped I/O registers in a more readable form.
Specifically, the |spiStruct|_ structure provides meaningfully-named fields in place of the multi-letter register names.

..  _`rp2040_spi_t`:

..  doxygenstruct:: cowpi_spi_t
    :project: CowPi_rp2040
    :no-link:
    :members:

After you create a pointer to a |spiStruct|_ structure that points to the lowest-addressed register (SSPCR0, ``0x4003C000``, per :numref:`tableRP2040SPIRegisters`).
For example, if we wanted to determine if there is room in the transmit queue, and then enable the SPI hardware as an controller with a 500kHz bit rate and an 8-bit data word, then we could do so with C code similar to this:

..  code-block:: c
    :linenos:

    volatile cowpi_spi_t *spi = (cowpi_spi_t *)(0x4003C000);
    uint32_t status = spi->status & 0x2;    // mask-off the irrelevant bits
    spi->prescaler = 250;                   // 125MHz / 250 = 500kHz
    spi->control = (1LL << 33) | 0x7;       // Enable bit | 8-bit data word

You may have noticed that this code does not use the read/modify/write pattern.
Because of the particular uses of the control and prescaler bits, you may find it easier to explicitly assign each control bit value afresh, rather than modify the pre-existing values.


.. _`rp2040SPIBits`:

SPI Register Bits
'''''''''''''''''

:numref:`tableRP2040SPIRegisters` identifies the particular bits in each of the SPI registers.


..  _tableRP2040SPIRegisters:

..  flat-table:: RP2040 "Synchronous Serial Port" registers. Adapted from original data in |microcontrollerReference|_, §4.4.4 and in |sspReference|_\ .
    :header-rows: 1

    *   -   Register Name
        -   SPI0 Address
        -   Bits 31..16
        -   Bit 15
        -   Bit 14
        -   Bit 13
        -   Bit 12
        -   Bit 11
        -   Bit 10
        -   Bit 9
        -   Bit 8
        -   Bit 7
        -   Bit 6
        -   Bit 5
        -   Bit 4
        -   Bit 3
        -   Bit 2
        -   Bit 1
        -   Bit 0
    *   -   | Control Register 0
            | SPPCR0
        -   0x4003C000
        -   Unused
        -   :cspan:`7` SCR
        -   SPH
        -   SPO
        -   :cspan:`1` FRF
        -   :cspan:`3` DSS
    *   -   | Control Register 1
            | SPPCR1
        -   0x4003C004
        -   :cspan:`12` Unused
        -   SOD
        -   MS
        -   SSE
        -   LBM
    *   -   | Data Register
            | SSPDR
        -   0x4003C008
        -   Unused
        -   :cspan:`15` DATA
    *   -   | Status Register
            | SSPSR
        -   0x4003C00C
        -   :cspan:`11` Unused
        -   BSY
        -   RFF
        -   RNE
        -   TNF
        -   TFE
    *   -   | Prescale Register
            | SSPCPSR
        -   0x4003C010
        -   :cspan:`8` Unused
        -   :cspan:`7` CPSDVSR


The CowPi_stdio library configures the SPI hardware to transmit 8-bit data words at 500kbps.
In this section we focus on the needs of the application programmer.
If you need information about the setting the bit rate, or configuring the peripheral address and address mask,
see Section 4.4.4 of the |microcontrollerReference|_ for the bit descriptions, and Section 4.4 generally for the bits' uses.

Data Bits
^^^^^^^^^

The CowPi_stdio library configures the SPI hardware to use 8-bit data words.
Using these eight data bits is straight-forward.
When in controller output/peripheral input mode, place the byte that needs to be transmitted into the SPI Data Register (or the ``data`` field of a |spiStruct|_ variable);
there is generally no need to use the distinct bits.
The byte will then be added to the transmit queue.
Similarly, when in controller input/peripheral output mode, the byte at the head of the receive queue can be found in the SPI Data Register.

Status Bits
^^^^^^^^^^^

There are five bits in the SPI Status Register that allow a program to learn when it is safe to control the hardware.

Bit 4, SSP Busy Flag
    The SPI hardware sets this flag to 1 when it is transmitting or receiving,
    and clears it to 0 when the SPI hardware is idle.

Bit 3, SSP Receive FIFO Full
    The SPI hardware sets this flag to 1 when the receive queue is full,
    and clears it to 0 when there is room to receive another data word.

Bit 2, SSP Receive FIFO Not Empty
    The SPI hardware clears this flag to 0 when the receive queue is empty,
    and sets it to 1 when there is at least one data word in the queue.

    *If and only if this bit is 1, then there is data that can be read from the Data Register.*

Bit 1, SSP Transmit FIFO Not Full
    The SPI hardware clears this flag to 0 when the transmit queue is full,
    and sets it to 1 when there is room for at least one data word in the queue.

    *If and only if this bit is 1, then it is safe to write data to the Data Register.*

Bit 0, SSP Transmit FIFO Empty
    The SPI hardware sets this flag to 1 when the transmit queue is empty,
    and clears it to 0 when there is at least one data word in the queue.

Control Bits
^^^^^^^^^^^^

There are two SPI Control Registers, which we have combined into a single 64-bit field in |spiStruct|_\ .
Within these registers are five bits to control the mode,
one bit to partially control the data rate,
four bits to set peripheral-specific parameters,
and four bits to set the width of the data word.

Bit 35 (SSPCR1 Bit 3), Peripheral-mode output disable
    This particular feature is very unlikely to be useful with the Cow Pi.
    See |microcontrollerReference|_ or |sspReference|_ for the notional use case.

Bit 34 (SSPCR1 Bit 2), Controller/Peripheral Select
    When this bit is 0, the microcontroller's SPI hardware is in controller mode;
    when this bit is 1, the SPI hardware is in peripheral mode.
    Note that this bit should only be changed when the SPI hardware is disabled.

Bit 33 (SSPCR1 Bit 1), SPI Enable
    When this bit is 1, the SPI hardware controls pins GP16, GP17, GP18, and GP19.

Bit 32 (SSPCR1 Bit 0), Loopback Mode
    When this bit is 1, the microcontroller's SPI hardware is in loopback mode,
    and the output of the microcontroller's transmit queue feeds directly into its own receive queue.

Bits 15..8 (SSPCR0 Bits 15..8), Serial Clock Rate
    A value in the range 0-255 that, when combined with the system clock and prescaler (see :ref:`rp2040SPIPrescaler`), determines the data rate.

Bit 7 (SSPCR0 Bit 7), Clock Phase
    \

Bit 6 (SSPCR0 Bit 6), Clock Polarity
    Orthogonal to the controller output/peripheral input and controller input/peripheral output modes,
    there are another four modes based on the clock's attributes when using the Motorola frame format.
    See |microcontrollerReference|_ or |sspReference|_\ .

Bits 5..4 (SSPCR0 Bits 5..4), Frame Format
    Orthogonal to the controller output/peripheral input and controller input/peripheral output modes,
    there are three frame formats.
    See |microcontrollerReference|_ or |sspReference|_\ .

Bits 3..0 (SSPCR0 Bits 3..0), Data Size Select
    The RP2040's SPI hardware can be configured to have a data word of any width between 4 bits and 16 bits (inclusive).
    The value to place in these four bits is :math:`width-1`

.. _`rp2040SPIPrescaler`:

Prescaler Bits
^^^^^^^^^^^^^^

The clock prescaler, when combined with the system clock and the serial clock rate, determines the data rate.
The value to place in the SPI Prescale Register (or the ``prescaler`` field of a |spiStruct|_ variable) is an even value in the range 2-254, such that:

..  math::

    data\_rate\ \mathrm{(bps)} = \frac{system\_clock\ \mathrm{(Hz)}}{prescaler \times \left( serial\_clock\_rate + 1 \right)}

For example, the CowPi_stdio library configures the SPI hardware for 500kbps when the system clock is 125MHz by setting the prescaler to 250 and the serial clock rate to 0:

..  math::

    \frac{125,000,000}{250 \times \left( 0 + 1 \right)} = 500,000


..  _`rp2040COPISequence`:

Controller Output/Peripheral Input Sequence
'''''''''''''''''''''''''''''''''''''''''''

The typical SPI controller output/peripheral input sequence is:

-   if necessary, enabling the SPI hardware
-   signaling the peripheral to receive data by setting the chip select pin to 0
-   transmitting one or more data bytes
-   signaling the peripheral to latch the data into its permanent register by setting the chip select pin to 1
-   if necessary, disabling the SPI hardware

Unlike some other microcontrollers, the RP2040's SPI hardware controls the chip select pin;
the program does not need to do so.

..  TODO:: It does not

Before writing a byte to the |spiStruct|_'s ``data`` field, the program should busy-wait until there is room in the transmit queue (indicated by bit 1 of the |spiStruct|_'s ``status`` field).

The pseudocode for this sequence is:

..  code-block:: pascal
    :linenos:

    (* assume variable spi is a reference to a cowpi_spi_t structure *)
    (* assume variable bit_order indicates whether the peripheral expects MSB first (0) or LSB first (1) *)
    (* assume variable select_pin is an integer identifying the chip select pin *)

-   if necessary, enable the SPI hardware

..  code-block:: pascal
    :lineno-start: 4

            (* set clock rate 500kHz *)
    spi->prescaler := 250
            (* Enable SPI, 8-bit data word*)
    spi->control := bitwise_or((1LL << 33), 7)


-   transmit one or more data bytes:

..  code-block:: pascal
    :lineno-start: 8

    for each byte of data do
                (* RP2040 SPI hardware only transmits MSB first, so reverse bits if LSB first is required *)
        if bit_order = 1 then
            data_byte := reverse_bits(data_byte)
                (* make sure the queue isn't full *)
        busy_wait_while(bit 1 of spi->status = 0)
                (* send the data that the peripheral needs *)
        spi->data := data_byte


-   if necessary, disable the SPI hardware

..  code-block:: pascal
    :lineno-start: 16

            (* make sure all transmissions are complete *)
    busy_wait_while(bit 0 of spi->status = 0)
            (* Disable SPI *)
    spi->control := 0


..  TIP::
    The ``for each`` expression in the pseudocode should be understood to be the mathematical :math:`\forall` operator.
    If there are several bytes that are handled identically, then writing a loop probably makes sense.
    On the other hand, if there are a small number of bytes, each of which must be handled differently,
    then it probably makes more sense to write straight-line code.

..  TIP::
    If you do not need to change the SPI mode or other SPI settings, you do not need to disable the SPI hardware between uses.
    By choosing to leave the SPI hardware active, the transmit queue can empty while your program takes other actions.

|

..  ATTENTION::
    The specific data byte sequence to be transmitted is described in the :doc:`../hardware/outputs` Section.

    -   :ref:`hd44780`
    -   :ref:`max7219digit`
    -   :ref:`max7219matrix`

|

Inter-Integrated Circuit Protocol
"""""""""""""""""""""""""""""""""

The RP2040 has two sets of |i2c| registers.
The CowPi_stdio library uses I2C0 to communicate with display modules.
If your intended application is simplified by placing peripherals on a separate set of |i2c| registers, then I2C1 can be exposed through GP18 \& GP19 (boosted to 5Von on the Cow Pi mk3c and mk4b) or through GP26 \& GP27 (operating at 3.3V on all Pico-based Cow Pi circuits).
The registers include:

``IC_CON``
    The |i2c| Control Register.
``IC_SS_SCL_HCNT``
    The |i2c| Standard Speed SCL High Count Register.
``IC_SS_SCL_LCNT``
    The |i2c| Standard Speed SCL Low Count Register.
``IC_FS_SCL_HCNT``
    The |i2c| Fast Mode SCL High Count Register.
``IC_FS_SCL_LCNT``
    The |i2c| Fast Mode SCL Low Count Register.
``IC_ENABLE``
    The |i2c| Enable Register

    *You do not need to configure I2C0;
    the CowPi_stdio library takes care of all necessary configuration for controller-transmitter mode at 100kbps.*

``IC_TAR``
    The |i2c| Target Address Register.
    Writing the target peripheral's address in the ``IC_TAR`` register will cause the microcontroller to transmit a "Start Bit".

``IC_SAR``
    The |i2c| Peripheral Address Register.
    If the |i2c| hardware is configured to act as a peripheral, then its address can be set through this register;
    the default address is 0x55.

``IC_DATA_CMD``
    The |i2c| Data and Command Register.
    Write data (or commands) to this register to place them in the transmit queue;
    Read data from this register to retrieve them from the receive queue.

``IC_STATUS``
    The |i2c| Status Register.
    Reading particular bits from the ``IC_STATUS`` register indicates the status of a data transfer.

``IC_TXFLR``
    The |i2c| Transmit Level Register.
    This register indicates the number of entries in the transmit queue.

``IC_RXFLR``
    The |i2c| Receive Level Register.
    This register indicates the number of entries in the receive queue.

The |i2c| hardware has four modes of operation: controller transmitter, controller receiver, peripheral transmitter, and peripheral receiver.\ [#terminology]_
In the Cow Pi's typical usage, the controller transmitter mode will be used to drive the display module.
For this reason, the discussion in this datasheet will focus on the controller transmitter mode.

The nature of |i2c| allows for uses other than the display module without compromising the ability to work with the display module.
If you choose to expand the Cow Pi in such a manner that other |i2c| modes are necessary, see Section 4.3 of the |microcontrollerReference|_ for details.

*If you use the RP2040 as a peripheral while it is in the Cow Pi circuit, we strongly advise using ICR1 for that purpose.*


.. _`rp2040I2CStruct`:

Structure for Memory-Mapped Input/Output
''''''''''''''''''''''''''''''''''''''''

The CowPi library provides data structures to access the memory-mapped I/O registers in a more readable form.
Specifically, the |i2cStruct|_ structure provides meaningfully-named fields in place of the multi-letter register names.

..  _`rp2040_i2c_t`:

..  doxygenstruct:: cowpi_i2c_t
    :project: CowPi_rp2040
    :no-link:
    :members:

After you create a pointer to a |i2cStruct|_ structure that points to the lowest-addressed register (I2C0.IC_CON at ``0x40044000``, or I2C1.IC_CON at ``0x40048000``, per :numref:`tableRP2040I2CRegisters`).
For example, if we wanted to determine if there is room in the transmit queue, and then enable the |i2c| hardware as an controller, then we could do so with C code similar to this:

..  code-block:: c
    :linenos:

    volatile cowpi_i2c_t *i2c = (cowpi_spi_t *)(0x4003C000);
    uint32_t status = i2c->status & 0x2;    // mask-off the irrelevant bits
    i2c->enable = 1;                        // Enable bit

You may have noticed that this code does not use the read/modify/write pattern.
Because of the particular uses of these registers, you may find it easier to explicitly assign each control bit value afresh, rather than modify the pre-existing values.


.. _`rp2040I2CBits`:

Status and Data Bits
'''''''''''''''''''''

:numref:`tableRP2040I2CRegisters` identifies the particular bits in some of the |i2c| registers.


..  _tableRP2040I2CRegisters:

..  flat-table:: RP2040 "Inter-Integrated Circuit" registers. Adapted from original data in |microcontrollerReference|_, §4.4.3.
    :header-rows: 1

    *   -   Register Name
        -   | I2C0 Address
            | I2C1 Address
        -   Bits 31..12
        -   Bit 11
        -   Bit 10
        -   Bit 9
        -   Bit 8
        -   Bit 7
        -   Bit 6
        -   Bit 5
        -   Bit 4
        -   Bit 3
        -   Bit 2
        -   Bit 1
        -   Bit 0
    *   -   | Control Register
            | IC_CON
        -   | 0x40044000
            | 0x40084000
        -   :cspan:`1` Unused
        -   STOP_DET_IF_CONTROLLER_ACTIVE
        -   RX_FIFO_FULL_HLD_CTRL
        -   TX_EMPTY_CTRL
        -   STOP_DET_IFADDRESSED
        -   IC_PERIPHERAL_DISABLE
        -   IC_RESTART_EN
        -   IC_10BITADDR_CONTROLLER
        -   IC_10BITADDR_PERIPHERAL
        -   :cspan:`1` SPEED
        -   CONTROLLER_MODE
    *   -   | Target Address Register
            | IC_TAR
        -   | 0x40044004
            | 0x40048004
        -   Unused
        -   SPECIAL
        -   GC_OR_START
        -   :cspan:`9` IC_TAR
    *   -   | Peripheral Address Register
            | IC_SAR
        -   | 0x40044008
            | 0x40048008
        -   :cspan:`2` Unused
        -   :cspan:`9` IC_SAR
    *   -   | Tx/Rx Data Buffer and Command Register
            | IC_DATA_CMD
        -   | 0x40044010
            | 0x40048010
        -   Unused
        -   FIRST_DATA_BYTE
        -   RESTART
        -   STOP
        -   CMD
        -   DAT
    *   -   | Enable Register
            | IC_ENABLE
        -   | 0x4004406C
            | 0x4004806C
        -   :cspan:`9` Unused
        -   TX_CMD_BLOCK
        -   ABORT
        -   ENABLE
    *   -   | Status Register
            | IC_STATUS
        -   | 0x40044070
            | 0x40048070
        -   :cspan:`5` Unused
        -   PERIPHERAL_ACTIVITY
        -   CONTROLLER_ACTIVITY
        -   RFF
        -   RFNE
        -   TFE
        -   TFNF
        -   ACTIVITY

The CowPi_stdio library configures the I2C0 hardware to transmit at 100kbps.
In this section we focus on the needs of the application programmer working with a display module connected to I2C0 and shall describe only the status and data bits.
If you need information about the setting the bit rate, addressing a target peripheral, configuring the peripheral address, or shutting down and enabling the |i2c| hardware,
see Section 4.3.2 of the |microcontrollerReference|_ for the bit descriptions.

Data Bits
^^^^^^^^^

The eight data bits are straight-forward.
When in controller transmitter mode, place the byte that needs to be transmitted into the Data Register (or the ``data`` field of a |i2cStruct|_ variable);
there is generally no need to use the distinct bits.
Similarly, when in controller receiver mode, the head of the receive queue can be found by reading from the Data Register.

Bits 11..8 have particular uses.
Most significantly, the last data byte placed into the transmit queue should be bitwise-ORed with a 1 in bit 9, to instruct the |i2c| hardware to transmit a STOP bit.

Status Bits
^^^^^^^^^^^

There are seven bits in the SPI Status Register that allow a program to learn when it is safe to control the hardware.

Bit 6, Peripheral FSM Activity Status
    \

Bit 5, Controller FSM Activity Status
    The |i2c| hardware sets an FSM Activity Status flag to 1 when the corresponding FSM is busy.

Bit 4, Receive FIFO Full
    The |i2c| hardware sets this flag to 1 when the receive queue is full,
    and clears it to 0 when there is room to receive another data word.

Bit 3, Receive FIFO Not Empty
    The |i2c| hardware clears this flag to 0 when the receive queue is empty,
    and sets it to 1 when there is at least one data word in the queue.

    *If and only if this bit is 1, then there is data that can be read from the Data Register.*

Bit 2, Transmit FIFO Empty
    The |i2c| hardware sets this flag to 1 when the transmit queue is empty,
    and clears it to 0 when there is at least one data word in the queue.

Bit 1, Transmit FIFO Not Full
    The |i2c| hardware clears this flag to 0 when the transmit queue is full,
    and sets it to 1 when there is room for at least one data word in the queue.

    *If and only if this bit is 1, then it is safe to write data to the Data Register.*

Bit 0, Activity Flag
    The |i2c| hardware sets this flag to 1 when it is transmitting or receiving,
    and clears it to 0 when the |i2c| hardware is idle.


..  _`rp2040ControllerTransmitterSequence`:

Controller Transmitter Sequence
'''''''''''''''''''''''''''''''

Generally speaking, the |i2c| controller transmitter sequence consists of:

-   contacting the peripheral by transmitting a start bit followed by the desired peripheral's address
-   transmitting one or more data bytes
-   transmitting a stop bit

Before writing a byte to the |i2cStruct|_'s ``data`` field, the program should busy-wait until there is room in the transmit queue (indicated by bit 1 of the |i2cStruct|_'s ``status`` field).
**To transmit the STOP bit, the last byte placed in the transmit queue should be bitwise-ORed with a 1 in bit 9!**


The pseudocode for this sequence is:

..  code-block:: pascal
    :linenos:

    (* assume variable i2c is a reference to a cowpi_i2c_t structure *)

-   contact the peripheral by transmitting a start bit followed by the desired peripheral's address

..  code-block:: pascal
    :lineno-start: 2

            (* "To generate a START BYTE, the CPU needs to write only once into these bits." *)
    i2c->target_address := peripheral_address


-   transmit one or more data bytes

..  code-block:: pascal
    :lineno-start: 4

            (* send the data that the peripheral needs *)
    for each byte of data do
                (* determine whether the stop bit should be queued *)
        if data_byte is the last byte then
            stop_bit := 1 << 9
        else
            stop bit := 0
                (* make sure the queue isn't full *)
        busy_wait_while(bit 1 of i2c->status = 0)
                (* send the data that the peripheral needs *)
        i2c->data := bitwise_or(data_byte, stop_bit)


-   transmit a stop bit

..  code-block:: pascal
    :lineno-start: 15

            (* the stop bit is in the queue; we just need to wait for it to be transmitted *)
    busy_wait_while(bit 2 of i2c->status = 0)

..  TIP::
    The ``for each`` expression in the pseudocode should be understood to be the mathematical :math:`\forall` operator.
    If there are several bytes that are handled identically, then writing a loop probably makes sense.
    On the other hand, if there are a small number of bytes, each of which must be handled differently,
    then it probably makes more sense to write straight-line code.

|

..  ATTENTION::
    The specific data byte sequence to be transmitted is described in the :doc:`../hardware/outputs` Section.

    -   :ref:`hd44780`
    -   :ref:`ssd1306`

|

----

|

Interrupts
----------

Most interrupts on the RP2040 are handled by registering specific functions as interrupt service routines (ISRs).
In the specific case of pin-based interrupts, the ISR *can* be registered by using the |attachInterrupt|_ function if you are using the Arduino toolchain,
or by using the ``gpio_set_irq_enabled_with_callback()`` function if you are using the Raspberry Pi Pico SDK.
However, we very strongly recommend using the CowPi library's :func:`cowpi_register_pin_ISR` function for increased portability across microcontrollers and across toolchains.


Sharing data with ISRs and Interrupt Handlers
"""""""""""""""""""""""""""""""""""""""""""""

Regardless of whether you create an ISR using the macro or register an interrupt handler using the :func:`cowpi_register_pin_ISR` or the ``attachInterrupt()`` function,
data cannot be passed to the interrupt-handling code through parameters,
and the interrupt-handling code cannot return data through a return value.
This necessitates the use of global variables to provide data to, and obtain data from, the interrupt-handling code.

Because the compiler cannot detect any definition-use pairs for these global variables –
they are updated in one function and read in another, and no call chain exists between the two functions –
the compiler will optimize-away these variables and the code that accesses them in the interest of reducing the program's memory footprint.
The way to prevent this mis-optimization is to use the ``volatile`` keyword.

..  IMPORTANT::
    Any global variables that interrupt-handling code reads from and/or writes to *must* have the ``volatile`` modifier.


Registering Pin Change Interrupt Handlers using :func:`cowpi_register_pin_ISR`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

..  TODO:: Implement ``cowpi_register_pin_ISR()`` for RP2040

The RP2040 allows for pin-based interrupts on any pin configured for digital input.
The CowPi library's :func:`cowpi_register_pin_ISR` function abstracts away the configuration details.

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

As all ISRs, you want to keep your interrupt handler short.
See the CowPi library's :ref:`pin_interrupts` example for demonstrations.


Registering External Interrupt Handlers using ``attachInterrupt()``
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Pin-based interrupts can also be manually configured and handled through the ``ISR()`` macro.
Just as the CowPi library's :func:`cowpi_register_pin_ISR` function abstracts away the configuration details for pin interrupts,
so does the |attachInterrupt|_\ .

To handle an interrupt, first write a function, such as ``handle_buttonpress()`` or ``handle_keypress()``.
This function must not have any parameters, and its return type must be ``void``.
Then, in the ``setup()`` function (or in one of its helper functions), register the interrupt with this code:

..  code-block:: c

    attachInterrupt(digitalPinToInterrupt(pin_number), interrupt_handler_name, mode);

This will configure all of the necessary registers to call the function whenever the input value on the pin *pin_number* satisfies the *mode*.
The *mode* is one of:

LOW
   to trigger the interrupt whenever the pin is 0

RISING
   to trigger the interrupt whenever the pin goes from 0 to 1

FALLING
   to trigger the interrupt whenever the pin goes from 1 to 0

CHANGE
   to trigger the interrupt whenever the pin rises or falls

As with all ISRs, you want to keep your interrupt handler short.

|

----

|

Timers
------

The RP2040 has a single general-purpose system timer and a small handful of specialized timers.
As with the other I/O registers, the registers used by these timers are mapped into the data memory address space.

For now, we will focus on the general-purpose timer (|microcontrollerReference|_, §4.6).


Structure for Memory-Mapped Timer Registers
"""""""""""""""""""""""""""""""""""""""""""

The CowPi library provides a data structure for the 64-bit timer, allowing access to the memory-mapped timer registers in a more readable form.
The registers can be access by creating pointer a to ``0x40054000``.

..  doxygenstruct:: cowpi_timer_t
    :project: CowPi_rp2040
    :members:

..  TODO:: bare-metal alarm interrupts

..  CAUTION::

    The RP2040 provides registers that permit an application programmer to change the timer's counter.
    The structure provided by the CowPi library does not expose these registers, replacing their addresses in the structure with padding.
    This is because nearly every framework assumes monotonically-increasing time.

The seven fields in the structure are:

``upper_word``
    \

``lower_word``
    Upper and lower 32-bit words of the 64-bit counter; these fields should be read if the application requires *consistent* time while running for more than an hour

``alarms``
    An array of four alarms; an alarm will trigger an interrupt when the counter's lower word matches the corresponding alarm register.
    Writing a value to an alarm register will set the corresponding bit in ``alarm_status``

``alarm_status``
    Indicates whether a particular alarm is armed (1) or not (0).
    A pending alarm can be cancelled by writing a 0 to the corresponding bit.

``raw_upper_word``
    \

``raw_lower_word``
    Upper and lower 32-bit words of the 64-bit counter; these fields should be read when no side-effects are desired and consistency between the upper and lower words is immaterial.

``pause``
    Set high to pause the timer.


Reading the Timer Counter
"""""""""""""""""""""""""

The timer increments its counter once per microsecond.
Thus, assuming the timer is never paused, the 64-bit counter contains the number of microseconds since the system was powered-up.

Reading the 64-bit Counter
''''''''''''''''''''''''''

The 64-bit counter cannot overflow during the span of a typical academic term:

..  math::

    2^{64} \mu s \approx 584,542\ \mathrm{years}

However, the RP2040 has a 32-bit data bus and cannot read the full 64 bits from the counter in a single cycle;
instead, the upper and lower word are accessed separately.
The 32-bit lower word *can* overflow during the span of a typical lab period:

..  math::

    2^{32} \mu s = 71\ \mathrm{minutes}\ 34.967,296\ \mathrm{seconds}

Unless otherwise anticipated, if the lower word happens to overflow between reading one of the counter's words and reading the other word,
then the upper and lower words will be inconsistent: depending on which word is read first, the measured time will either be fast or slow by about :math:`71\frac{1}{2}` minutes.

To address this, whenever a program reads from ``lower_word``, the consistent upper word is latched so that it is available to be read from ``upper_word`` in the next cycle.

..  NOTE::

    This latching occurs *only* if the lower word is read first

The pseudocode to obtain the full 64-bit counter is thus:

..  code-block:: pascal
    :linenos:

            (* assume variable timer is a reference to a cowpi_timer_t structure at 0x40054000 *)
    lower_32bits = timer->lower_word
    upper_32bits = timer->upper_word
    counter_64bits = bitwise_or((uint64_t)upper_32bits << 32, lower_32_bits)

..  NOTE::

    The preceding pseudocode has a race condition if two processes (or threads) attempt to read the timer concurrently.

..  NOTE::

    The C standard does not specify the evaluation order of the sub-expressions in a bitwise-OR expression.
    We recommend that you explicitly read the lower word first to ensure that it is, in fact, read before the upper word.

Reading a 32-bit Counter
''''''''''''''''''''''''

If you are not concerned about the possibility of overflow every :math:`71\frac{1}{2}` minutes, then you can read from ``raw_upper_word`` and ``raw_lower_word``.

If you only need a 32-bit microsecond counter, then reading from ``raw_lower_word`` will provide you with the number of microseconds since power-up, modulo :math:`2^{32}`.

..  code-block:: pascal
    :lineno-start: 5

    counter_32bits = timer->raw_lower_word;

A somewhat less likely scenario can make use of the ``raw_upper_word``:
Because the lower word overflows every :math:`2^{32}` microseconds, the upper word increments approximately once every :math:`\frac{1}{20}\mathrm{day}`.

..  code-block:: pascal
    :lineno-start: 6

    days_since_powerup = timer->raw_upper_word / 20;
            (* has error of about 3 minutes per day *)

..  NOTE::

    There are no race conditions inherent in two processes (or threads) reading the "raw" timer words concurrently.


Scheduling Alarms
"""""""""""""""""

We advise against directly accessing the alarm registers while using the official Arduino toolchain, which is based on the Mbed OS,
as it is not clear how the Mbed OS uses the alarms.
We recommend instead using the Mbed OS ``Ticker`` and ``Timeout`` APIs.

..  TODO:: Wrap and document the `Ticker <https://os.mbed.com/docs/mbed-os/v6.16/apis/ticker.html>`_ and `Timeout <https://os.mbed.com/docs/mbed-os/v6.16/apis/timeout.html>`_ APIs.

    See also

    -    `<https://os.mbed.com/teams/TVZ-Mechatronics-Team/wiki/Timers-interrupts-and-tasks>`_
    -   `<https://os.mbed.com/media/uploads/robt/mbed_course_notes_-_timers_and_interrupts.pdf>`_
    -   `<https://os.mbed.com/users/4180_1/notebook/using-hardware-timers/>`_
    -   `Timer <https://os.mbed.com/docs/mbed-os/v6.16/apis/timer.html>`_

|

----

|

..  TODO:: Watchdog Timer

..  TODO:: Real-Time Clock

..  TODO:: PWM

..  TODO:: ADC

..  TODO:: Temperature

    Probably as an "Extension Option"

..  TODO:: UART

|

----

|

..  _rp2040concurrency:

Bare-Metal Concurrency
----------------------

This is a placeholder section.
Currently the only toolchain for RP2040 that the CowPi library supports is the official Arduino toolchain, built on top of Mbed OS.

..  WARNING::

    For the time being, we advise against using the memory-mapped communication & synchronization registers,
    as the official Arduino toolchain does not support dual-core operation, and
    it is not clear which (if any) of the spinlocks are used by Mbed OS and would require deconfliction with application code.


Structure for Memory-Mapped Interprocess Communication & Synchronization Registers
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

..  doxygenstruct:: cowpi_concurrency_t
    :project: CowPi_rp2040
    :members:

|

----

|

..  |ioport|                    replace:: ``cowpi_ioport_t``
..  _ioport:                    #rp2040-ioport-t

..  |spiStruct|                 replace:: ``cowpi_spi_t``
..  _spiStruct:                 #rp2040-spi-t

..  |i2cStruct|                 replace:: ``cowpi_i2c_t``
..  _i2cStruct:                 #rp2040-i2c-t

..  |microcontrollerReference|  replace:: RP2040 datasheet
..  _microcontrollerReference:  https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf

..  |sspReference|              replace:: ARM PrimeCell Synchronous Serial Port (PL022) Technical Reference Manual
..  _sspReference:              https://developer.arm.com/documentation/ddi0194/latest

..  |attachInterrupt|           replace:: Arduino ``attachInterrupt()`` function
..  _attachInterrupt:           https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/


..  [#terminology]
    The RP2040 datasheet uses the legacy SPI and |i2c| master/slave terminology.
    In the Cow Pi datasheet, we use the terminology recommended by the Open Source Hardware Association, as we find "controller" and "peripheral" to be the best-descriptive alternatives of those that have been suggested.
