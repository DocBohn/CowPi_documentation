Input Devices
=============

TODO

Switches and Buttons
--------------------

TODO

Theory of Operation
^^^^^^^^^^^^^^^^^^^

TODO

Reading the Devices' Positions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO

Matrix Keypad
-------------

TODO

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
As an alternative to polling, an interrupt that is triggered by a change on the columns' pins can be used to indicate that a key has been pressed (see Section XXXXX).

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
This might be a ``char`` corresponding to the character on the key's face, as is the case for **``cowpi_get_keypress``** (Section `2.4 <#subsec:ScannedInputs>`__).
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

.. code-block::
    :linenos:

    ∀row:
        row_bit_vector := 0b1111    (* set all rows to 1 *)
        row_bit_vector(row) := 0    (* except the row we're currently examining *)
        wait at least one microcontroller clock cycle
        ∀column:
            if (column_bit_vector(column) = 0):
                key_pressed := keys(row,column)
    row_bit_vector := 0b0000        (* set all rows to 0 to detect the next keypress *)

.. NOTE::
    This pseudocode will report at most one key pressed;
    it would have to be modified to report multiple keys pressed.

    This software limitation is not a limitation for mark 1 Cow Pis, as mark 1 Cow Pis have a hardware limitation:
    their keypads have no protection against shorting power to ground when two keys are pressed simultaneously.


The delay shown in line 4 is sometimes, but not always necessary.
There is a slight delay between setting a pin's output value and being able to detect the change by reading a different pin's input value.
Some realizations of the pseudocode attempt to read the change before it can be read reliably;
this usually manifests as one of the keypad's columns not being readable.
The fix is to introduce a delay of at least one clock cycle (strictly speaking, one clock cycle is more than enough, but a shorter delay is not possible).
For our purposes, this should be managed by introducing a 1\ :math:`\mu`\ s delay using the Arduino core library's ``delayMicroseconds()``.
