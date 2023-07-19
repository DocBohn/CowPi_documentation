..  include:: ../mk1ef.txt
..  include:: ../mk1f.txt

Install the Display Module
==========================
*Cow Pi mk1f: Arduino Nano form factor,* |i2c-italics| *communication*

Examine the I2C-LCD serial interface.
Notice that the header has |numberOfSerialPins| pins (:numref:`i2cDisplayModuleHeader`): ``VCC`` (common collector voltage), ``GND`` (ground), |serialPins|.
When the display module is oriented for viewing, these header pins will be on the left.

..  _i2cDisplayModuleHeader:
..  figure:: i2c-module-header.jpg
    :width: 5cm
    :align: center

    The display module's header has |numberOfSerialPins| pins.

:numref:`lcd1602FigureDisplayDiagram` shows a diagram of the wiring to connect the display module to the breadboard.

..  _lcd1602FigureDisplayDiagram:
..  figure:: ../fritzing_diagrams/CowPi-mk1f-display-lcd1602.png
    :alt: Diagram of display module's connections to the breadboard.
    :width: 90.0%

    Diagram of display module's connections to the breadboard.

..  _i2cFigureConnections:
..  figure:: display-connections-mk1f.jpg
    :alt: SPI connections on at the microcontroller.
    :width: 90.0%

    SPI connections on at the microcontroller.


..  IMPORTANT:: |unplug|


:\:[   ]: Look at :numref:`i2cFigureDisplays` to determine which display module you have:


..  _i2cFigureDisplays:
.. figure:: ../../../blank.png

    Display modules that use the Serial-Parallel Interface protocol

    +-------+---------------------------------------------------+-------+---------------------------------------------------+
    |       | .. image:: hd44780-character-floating-display.jpg |       | .. image:: hd44780-character-pinned-display.jpg   |
    |       |    :align: center                                 |       |    :align: center                                 |
    | **a** |    :width: 90%                                    | **b** |    :width: 90%                                    |
    |       |                                                   |       |                                                   |
    |       | HD44780-driven LCD character display.             |       | HD44780-driven LCD character display.             |
    |       |  (attached to serial adapter)                     |       |  (not attached to serial adapter)                 |
    +-------+---------------------------------------------------+-------+---------------------------------------------------+
    |       | .. image:: ssd1306-oled-graphic-display.jpg                                                                   |
    |       |    :align: center                                                                                             |
    | **c** |    :width: 45%                                                                                                |
    |       |                                                                                                               |
    |       | SSD1306-driven OLED graphic display.                                                                          |
    +-------+---------------------------------------------------------------------------------------------------------------+


-   If you have an LCD character display, it might be attached to the serial adapter (:numref:`i2cFigureDisplays`\ (a)) or the adapter might not be attached to the display (:numref:`i2cFigureDisplays`\ (b))

    -   If your I2C-LCD serial interface is **NOT** attached to the LCD display module, then you will use the breadboard to provide the electrical connections between the serial interface and the display module.

        :\:[   ]: Insert the LCD display module's sixteen pins into contact points |lcd1602Range|.

        :\:[   ]: With the four header pins pointing to the left, insert the I2C-LCD serial interface's sixteen downward-pointing pins into contact points |serialAdapterRange|.

        :\:[   ]: Take the |numberOfSerialPins|-conductor female-to-male rainbow cable and attach the |numberOfSerialPins| female connectors to the display module’s |numberOfSerialPins| header pins.

    -   If your I2C-LCD serial interface **IS** attached to the LCD display module, then the sixteen pins connecting the serial adapter to the display module do not need to be inserted into the breadboard.

        :\:[   ]: Take the |numberOfSerialPins|-conductor female-to-male rainbow cable and attach the |numberOfSerialPins| female connectors to the display module’s |numberOfSerialPins| header pins.

        :\:[   ]: *Optionally* place a jumper wire looped from a63 to j63 to prevent the display module from sliding around.

-   If you have an OLED graphic display (:numref:`i2cFigureDisplays`\ (c)):

        :\:[   ]: Insert the header pins into |numberOfSerialPins| adjacent breadboard rows.

        :\:[   ]: Take a |numberOfSerialPins|-conductor male-to-male rainbow cable and insert one end into the same rows as the display module’s |numberOfSerialPins| header pins.

|

:\:[   ]: Identify the wire that is connected to the display module's |serialClockPin| pin;
    insert the male end of this wire in contact point |mcuClockPoint| (electrically connected to the |developmentBoard|'s |mcuClockPin| pin).

:\:[   ]: Insert the male end of the |serialDataPin| wire into contact point |mcuDataPoint| (electrically connected to the |developmentBoard|'s |mcuDataPin| pin).

:\:[   ]: Insert the ``GND`` wire into the upper |ground|, and the ``VCC`` wire into the upper |power|.


When you have finished connecting the display module, there should be the electrical connections described in :numref:`i2cDisplayModuleConnections`.

..  _i2cDisplayModuleConnections:
..  table:: Electrical Connections for Display Module.

    ====================== ====================== ====================
    Display Module pin     |developmentBoard| pin Power/Ground Rail
    ====================== ====================== ====================
    |serialClockPin|       |mcuClockPin|
    |serialDataPin|        |mcuDataPin|
    ``GND``                                       |ground|
    ``VCC``                                       |power|
    ====================== ====================== ====================

..  ATTENTION::
    **CHECKPOINT 8**
    | |checkpoint| connected the display module to the breadboard. |updateCheckpointsTXT|


:\:[   ]: In the Arduino IDE, open the *File* ⟶ *Examples* ⟶ *CowPi* ⟶ |displayModuleHelloWorld| example.

:\:[   ]: Find these lines in the ``setup()`` function:

   ::

      //    protocol = SPI;
          protocol = I2C;

:\:[   ]: Make sure that the ``protocol = I2C`` line is uncommented and that the ``protocol = SPI`` line is commented-out.

:\:[   ]: Compile the program and upload it to your Arduino Nano.

    You should see the display module's backlight blink on and off.
    If so, then you have correctly connected the display module and serial adapter even if you don't see a message on the display module.

:\:[   ]: Using a screwdriver, turn the trim potentiometer on the serial adapter until you can see the "Hello, world!" message.

    ..  image:: animations/lcd1602.gif
        :height: 5cm
        :align: center



Kit Assembly is Complete
========================

You have now finished assembling the class kit.
In the upcoming I/O labs, you will use the kit to learn about memory-mapped I/O and about handling low-level interrupts.

..  image:: ../fritzing_diagrams/CowPi-mk1f-lcd1602-complete.png
    :alt: Diagram of completed Cow Pi mk1f circuit with LCD1602 character display.
    :width: 90.0%
