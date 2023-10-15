Input Devices
=============

Unless implementing :doc:`../expansion`, all inputs in the Cow Pi circuit are either simple passive input devices, described here, or timers that are part of the microcontroller, described in the :doc:`../microcontroller` Section.

Switches and Buttons
--------------------

There are two pushbuttons and two slide-switches in the Cow Pi circuit.

Theory of Operation
^^^^^^^^^^^^^^^^^^^

The pushbuttons, or tactile switches,\ [#]_ are normally-open, momentary switches.
When a button is in the "up" position, that is, it is not being pressed, there is an open circuit between the contacts.
When the button is pressed and is in the "down" position, it closes the circuit between the contacts.

..  _pushbutton:
..  tikz:: The pushbuttons used in the Cow Pi are normally-open, momentary switches.
    :align: center

    \begin{tikzpicture}[x=.05in, y=.05in]
        \draw (-4,0) -- (-1.5,0);
        \draw[black, fill=black] (-1.5,0) circle (.5);
        \draw (4,0) -- (1.5,0);
        \draw[black, fill=black] (1.5,0) circle (.5);
        \draw (-2,1.5) -- (2,1.5);
        \draw (0,3.5) -- (0,1.5);
    \end{tikzpicture}


The slide-switches are technically single-pole, double-throw switches, but we treat them as single-pole, single-throw switches.
In the Cow Pi circuit, when a switch is in the "right" position, there is an open circuit between the contacts.
When the switch is in the "left" position, it closes the circuit between the contacts.

..  _slideSwitch:
..  tikz:: We treat the slide-switches used in the Cow Pi as single-pole, single-throw switches.
    :align: center

    \begin{tikzpicture}[x=.05in, y=.05in]
        \draw(0,5) -- (0,2);
        \draw[black, fill=black] (0,2) circle (0.5);
        \draw (0,-5) -- (0,-2);
        \draw[black, fill=black] (0,-2) circle (0.5);
        \draw (0,-2) -- (2,2);
    \end{tikzpicture}


As shown in :numref:`electricalView`, the devices are placed in the circuit with one pole grounded and the other attached to a microcontroller input pin.
The microcontroller is configured to place its operating voltage on the pin with a "pull-up resistor."
This pull-up resistor has a very high resistance, typically 10kΩ-20kΩ, so that when the switch is closed, only a very small amount of current flows.

..  _electricalView:
..  tikz:: Tactile switches and slide switches have one pole grounded and the other connected to a pin with a pull-up resistor.
    :align: center

    \begin{tikzpicture}[x=.05in, y=.05in]
        \draw (-24,0) -- (-21.5,0);
        \draw[black, fill=black] (-21.5,0) circle (.5);
        \draw (-16,0) -- (-18.5,0);
        \draw[black, fill=black] (-18.5,0) circle (.5);
        \draw (-18.5,-2.5) node {\rotatebox{-90}{\tiny pin}};
        \draw (-22,1.5) -- (-18,1.5);
        \draw (-20,3.5) -- (-20,1.5);
        \draw (-24,0) -- (-24,-5);
        \draw (-22.5,-5) -- (-25.5,-5);
        \draw (-23,-5.5) -- (-25,-5.5);
        \draw (-23.5,-6) -- (-24.5,-6);
        \draw (-16,0) -- (-16,5) -- ++(.5,.25) -- ++(-1,.5) -- ++(1,.5) -- ++(-1,.5) -- ++(1,.5) -- ++(-1,.5) -- ++(.5,.25) -- ++(0,1) -- ++(1,0) -- ++(-1,1) -- ++(-1,-1) -- ++(1,0);

        \draw(20,5) -- (20,2);
        \draw[black, fill=black] (20,2) circle (0.5);
        \draw(17.5,2) node {\tiny pin};
        \draw (20,-5) -- (20,-2);
        \draw[black, fill=black] (20,-2) circle (0.5);
        \draw (20,-2) -- (22,2);
        \draw (18.5,-5) -- (21.5,-5);
        \draw (19,-5.5) -- (21,-5.5);
        \draw (19.5,-6) -- (20.5,-6);
        \draw (20,5) -- ++(.5,.25) -- ++(-1,.5) -- ++(1,.5) -- ++(-1,.5) -- ++(1,.5) -- ++(-1,.5) -- ++(.5,.25) -- ++(0,1) -- ++(1,0) -- ++(-1,1) -- ++(-1,-1) -- ++(1,0);
    \end{tikzpicture}


When the circuit is open (button in the "up" position or slide-switch in the "right" position), no current flows through the resistor.
Because no current flows through the resistor, there is no voltage drop across the resistor, and so the voltage measured at the pin is the microcontroller's operating voltage.
As shown in :numref:`logicHigh`, This is interpreted as logic high (boolean 1).

..  _logicHigh:
..  tikz:: When a switch is open, the pin reads high.
    :align: center

    \begin{tikzpicture}[x=.05in, y=.05in]
        \draw (-24,0) -- (-21.5,0);
        \draw[black, fill=black] (-21.5,0) circle (.5);
        \draw (-16,0) -- (-18.5,0);
        \draw[black, fill=black] (-18.5,0) circle (.5);
        \draw (-18.5,-2.5) node {1};
        \draw (-22,1.5) -- (-18,1.5);
        \draw (-20,3.5) -- (-20,1.5);

        \draw(20,5) -- (20,2);
        \draw[black, fill=black] (20,2) circle (0.5);
        \draw(18,2) node {1};
        \draw (20,-5) -- (20,-2);
        \draw[black, fill=black] (20,-2) circle (0.5);
        \draw (20,-2) -- (22,2);
    \end{tikzpicture}

On the other hand, when the circuit is closed (button in the "down" position or slide-switch in the "left" position), current flows through the resistor.
Because there is no other appreciable resistance in the circuit, all of the voltage drop is across the resistor, and so 0V is measured at the pin.
As shown in :numref:`logicLow`, This is interpreted as logic low (boolean 0).


..  _logicLow:
..  tikz:: When a switch is closed, the pin reads low.
    :align: center

    \begin{tikzpicture}[x=.05in, y=.05in]
        \draw (-24,0) -- (-21.5,0);
        \draw[black, fill=black] (-21.5,0) circle (.5);
        \draw (-16,0) -- (-18.5,0);
        \draw[black, fill=black] (-18.5,0) circle (.5);
        \draw (-18.5,-2.5) node {0};
        \draw (-22,.6) -- (-18,.6);
        \draw (-20,2.6) -- (-20,.6);

        \draw(20,5) -- (20,2);
        \draw[black, fill=black] (20,2) circle (0.5);
        \draw(18,2) node {0};
        \draw (20,-5) -- (20,-2);
        \draw[black, fill=black] (20,-2) circle (0.5);
        \draw (20,-2) -- (20.7,2.5);
    \end{tikzpicture}



Reading the Devices' Positions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To read these input devices, the pins must be configured as input pins with the microcontroller's internal pullup resistors enabled.
(Alternatively, external pullup resistors could be used -- but won't be in the Cow Pi for passive input devices.)
The CowPi library's :func:`cowpi_setup` function takes care of this along with other configuration settings.

That done, reading a devices' position is as simple as reading the pin's logic value.
If you are not writing code using memory-mapped I/O, then you would do this with Arduino's ``digitalRead()`` function or the Raspberry Pi SDK's ``gpio_get()`` function.
If you are writing code using memory-mapped I/O, then you would examine the pin's bit in the I/O bank's input register, as described in the :doc:`../microcontroller` Section.
If the bit's value is 0, then the button is pressed, or the switch is in the left position.
If the bit's value is 1, then the button is not pressed, or the switch is in the right position.


To Learn More
^^^^^^^^^^^^^

SparkFun has a webpage that discusses `Button and Switch Basics <https://learn.sparkfun.com/tutorials/button-and-switch-basics>`_\ .


Matrix Keypad
-------------

The numeric keypad consists of sixteen keys, labeled ``0``-``9``, ``A``-``D``, ``#``, and ``*``.
Rather than requiring sixteen distinct pins on the microcontroller (one for each key), it is wired so that it only requires eight pins: one for each column and one for each row.

Theory of Operation
^^^^^^^^^^^^^^^^^^^

Each key on a matrix keypad is a normally-open, momentary button that resides at the intersection of a row and a column;
see :numref:`matrixKeypad`.
When pressed, the key closes an electrical connection between that row and column.
On the Cow Pi, each row is connected to an output pin on the microcontroller, and each column is connected to an input pin with a pull-up resistor.

..  _matrixKeypad:
..  tikz:: Each key on the keypad is at the intersection of a row and a column.
    :align: center

    \begin{tikzpicture}[x=.1in, y=.1in]
        \draw (7,10) node {1} +(3,0) node {2} +(6,0) node {3} +(9,0) node {A}
            +(0,-3) node {4} +(3,-3) node {5} +(6,-3) node {6} +(9,-3) node {B}
            +(0,-6) node {7} +(3,-6) node {8} +(6,-6) node {9} +(9,-6) node {C}
            +(0,-9) node {*} +(3,-9) node {0} +(6,-9) node {\#} +(9,-9) node {D};
        \draw (0,9) node {row1} ++(3,0) -- ++(15,0);
        \draw (0,6) node {row4} ++(3,0) -- ++(15,0);
        \draw (0,3) node {row7} ++(3,0) -- ++(15,0);
        \draw (0,0) node {row*} ++(3,0) -- ++(15,0);
        \draw (6,15) node {\rotatebox{-90}{col1}} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (6,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (9,15) node {\rotatebox{-90}{col2}} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (9,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (12,15) node {\rotatebox{-90}{col3}} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (12,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (15,15) node {\rotatebox{-90}{colA}} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (15,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
    \end{tikzpicture}

Because the input pins that the columns are connected to use pull-up resistors, the logic value on these pins will normally read high (boolean 1).
A column will read as logic low (boolean 0) only when it is electrically connected to a row that is set low.
An application developer can take advantage of this by setting all of the rows' pins to logic low (boolean 0);
see :numref:`keypadAndMicrocontroller`.
When a key is pressed, its column will then become low.

..  _keypadAndMicrocontroller:
..  tikz:: Detecting a keypress is possible by setting each row low and monitoring whether any column becomes low.
    :align: center

    \begin{tikzpicture}[x=.1in, y=.1in]
        \draw (7,10) node {1} +(3,0) node {2} +(6,0) node {3} +(9,0) node {A}
        +(0,-3) node {4} +(3,-3) node {5} +(6,-3) node {6} +(9,-3) node {B}
        +(0,-6) node {7} +(3,-6) node {8} +(6,-6) node {9} +(9,-6) node {C}
        +(0,-9) node {*} +(3,-9) node {0} +(6,-9) node {\#} +(9,-9) node {D};
        \draw (0,5) node {\rotatebox{-90}{$\mu$C outputs set low}};
        \draw (0,9) +(2,0) node {0} ++(3,0) -- ++(15,0);
        \draw (0,6) +(2,0) node {0} ++(3,0) -- ++(15,0);
        \draw (0,3) +(2,0) node {0} ++(3,0) -- ++(15,0);
        \draw (0,0) +(2,0) node {0} ++(3,0) -- ++(15,0);
        \draw (9,15) node {$\mu$C inputs with pull-up resistors};
        \draw (6,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (6,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (9,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (9,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (12,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (12,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (15,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (15,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
    \end{tikzpicture}

A keypress, thus, can be detected based on the values read from the columns' pins.
An application programmer can poll the four columns' pins.
If, collectively, they produce the bit vector 0xF, then no key is being pressed;
however, if the bit vector is anything other than 0xF (such as in :numref:`keypressDetected`, then at least one key is being pressed.
As an alternative to polling, an interrupt that is triggered by a change on the columns' pins can be used to indicate that a key has been pressed (see the Section discussing :ref:`atmega328pInterrupts`).

..  _keypressDetected:
..  tikz:: Pressing a key, such as "8", causes the column bit vector to be something other than 0xF.
    :align: center

    \begin{tikzpicture}[x=.1in, y=.1in]
        \draw (7,10) node {1} +(3,0) node {2} +(6,0) node {3} +(9,0) node {A}
        +(0,-3) node {4} +(3,-3) node {5} +(6,-3) node {6} +(9,-3) node {B}
        +(0,-6) node {7} +(3,-6) node {8} +(6,-6) node {9} +(9,-6) node {C}
        +(0,-9) node {*} +(3,-9) node {0} +(6,-9) node {\#} +(9,-9) node {D};
        \draw (0,5) node {\rotatebox{-90}{$\mu$C outputs set low}};
        \draw (0,9) +(2,0) node {0} ++(3,0) -- ++(15,0);
        \draw (0,6) +(2,0) node {0} ++(3,0) -- ++(15,0);
        \draw (0,3) +(2,0) node {0} ++(3,0) -- ++(15,0);
        \draw (0,0) +(2,0) node {0} ++(3,0) -- ++(15,0);
        \draw (9,15) node {$\mu$C inputs with pull-up resistors};
        \draw (6,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (6,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (9,15) +(0,-2) node {0} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (9,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (12,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (12,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (15,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (15,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw[gray, fill=red] (9,3) circle (.5);
    \end{tikzpicture}

Once it has been determined that a key is pressed, code that scans the keypad should execute.
If every row is made logic-high *except* for one row, then the code can determine whether the key that was pressed is in that row.
For example, as shown in
:numref:`scanningUnpressedRow`, if the "8" key is pressed and "row4" is the only logic-low row, then the column bit vector is 0xF, and so the pressed key is not in that row.

..  _scanningUnpressedRow:
..  tikz:: Examining a row that does not have a pressed key.
    :align: center

    \begin{tikzpicture}[x=.1in, y=.1in]
        \draw (7,10) node {1} +(3,0) node {2} +(6,0) node {3} +(9,0) node {A}
        +(0,-3) node {4} +(3,-3) node {5} +(6,-3) node {6} +(9,-3) node {B}
        +(0,-6) node {7} +(3,-6) node {8} +(6,-6) node {9} +(9,-6) node {C}
        +(0,-9) node {*} +(3,-9) node {0} +(6,-9) node {\#} +(9,-9) node {D};
        \draw (0,5) node {\rotatebox{-90}{$\mu$C outputs set high,}};
        \draw (-1.5,5) node {\rotatebox{-90}{except one}};
        \draw (0,9) +(2,0) node {1} ++(3,0) -- ++(15,0);
        \draw (0,6) +(2,0) node {0} ++(3,0) -- ++(15,0);
        \draw (0,3) +(2,0) node {1} ++(3,0) -- ++(15,0);
        \draw (0,0) +(2,0) node {1} ++(3,0) -- ++(15,0);
        \draw (9,15) node {$\mu$C inputs with pull-up resistors};
        \draw (6,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (6,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (9,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (9,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (12,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (12,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (15,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (15,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw[gray, fill=red] (9,3) circle (.5);
    \end{tikzpicture}

But, as shown in :numref:`scanningPressedRow`, if "row7" is the only logic-low row, then the column bit vector is not 0xF, and so the pressed key is in that row; moreover, because "col2" is now logic-low, the code can establish that the pressed key is at the intersection of "row7" and "col2," *i.e.*, the "8" key.

.. _scanningPressedRow:
..  tikz:: Examining a row that does have a pressed key.
    :align: center

    \begin{tikzpicture}[x=.1in, y=.1in]
        \draw (7,10) node {1} +(3,0) node {2} +(6,0) node {3} +(9,0) node {A}
        +(0,-3) node {4} +(3,-3) node {5} +(6,-3) node {6} +(9,-3) node {B}
        +(0,-6) node {7} +(3,-6) node {8} +(6,-6) node {9} +(9,-6) node {C}
        +(0,-9) node {*} +(3,-9) node {0} +(6,-9) node {\#} +(9,-9) node {D};
        \draw (0,5) node {\rotatebox{-90}{$\mu$C outputs set high,}};
        \draw (-1.5,5) node {\rotatebox{-90}{except one}};
        \draw (0,9) +(2,0) node {1} ++(3,0) -- ++(15,0);
        \draw (0,6) +(2,0) node {1} ++(3,0) -- ++(15,0);
        \draw (0,3) +(2,0) node {0} ++(3,0) -- ++(15,0);
        \draw (0,0) +(2,0) node {1} ++(3,0) -- ++(15,0);
        \draw (9,15) node {$\mu$C inputs with pull-up resistors};
        \draw (6,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (6,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (9,15) +(0,-2) node {0} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (9,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (12,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (12,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw (15,15) +(0,-2) node {1} ++(0,-3) -- ++(0,-2.5) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2) ++(0,-1) -- ++(0,-2);
        \draw (15,9.5) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5] ++(0,-2) arc [start angle=90, end angle=-90, radius=.5];
        \draw[gray, fill=red] (9,3) circle (.5);
    \end{tikzpicture}

After the code has determined which row and column the pressed key is on, it can return a value or assign a value to a variable accordingly.
This might be a ``char`` corresponding to the character on the key's face, as is the case for :func:`cowpi_get_keypress`.
Or this might be an ``int`` corresponding to the value of the numeral on the key's face.
Or this might even be some value unrelated to whatever is printed on the key's face.


Scanning the Keypad
^^^^^^^^^^^^^^^^^^^

There are a few options for obtaining the value corresponding to a key that is pressed on the keypad.
The most efficient for a simple application is to use a lookup table.
For example, if you need to return a character that corresponds to the face value of the key that was pressed, then the lookup table would be:

.. math::

    keys :=
        \left(\begin{array}{cccc}
            '1' & '2' & '3' & 'A' \\
            '4' & '5' & '6' & 'B' \\
            '7' & '8' & '9' & 'C' \\
            '*' & '0' & '\#' & 'D'
        \end{array}\right)

If the keypad is wired to the microcontroller such that four contiguous output pins are connected to the rows and four contiguous input pins are connected to the columns (as is the case for the Cow Pi), then this pseudocode will scan the keypad and determine which key, if any, is pressed.

.. code-block:: pascal
    :linenos:

    for each row do
        row_bit_vector := 0b1111    (* set all rows to 1 *)
        row_bit_vector(row) := 0    (* except the row we're currently examining *)
        wait at least one microcontroller clock cycle
        for each column do
            if (column_bit_vector(column) = 0) then
                key_pressed := keys(row,column)
    row_bit_vector := 0b0000        (* set all rows to 0 to detect the next keypress *)

.. NOTE::
    This pseudocode will report at most one key pressed;
    it would have to be modified to report multiple keys pressed.

    This software limitation is not a limitation for mark 1 Cow Pis, as mark 1 Cow Pis have a hardware limitation:
    their keypads have no protection against shorting power to ground when two keys are pressed simultaneously.

..  TIP::
    The ``for each`` expressions in the pseudocode should be understood to be the mathematical :math:`\forall` operator.
    Write a loop, or don't, based on what makes sense to you in terms of readability and ease of modification.
    We have seen successful implementations that use a loop to iterate over the columns,
    and we have seen successful implementations that instead have a ``switch`` statement or four ``if`` statements.


The delay shown in line 4 is sometimes, but not always necessary.
There is a slight delay between setting a pin's output value and being able to detect the change by reading a different pin's input value.
Some realizations of the pseudocode attempt to read the change before it can be read reliably;
this usually manifests as one of the keypad's columns not being readable.
The fix is to introduce a delay of at least one clock cycle (strictly speaking, one clock cycle is more than enough, but a shorter delay is not possible).
For our purposes, this should be managed by introducing a 1µs delay using the Arduino core library's ``delayMicroseconds()``.

|

----

..  [#] Tactile switches are so-called because a "bump" in the plunger's travel provides tactile feedback when you press and release it.