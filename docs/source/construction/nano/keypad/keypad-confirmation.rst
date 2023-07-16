..  ATTENTION::
    **CHECKPOINT 7**
    | Before proceeding further, have a TA or a classmate verify that you have correctly inserted and wired the matrix keypad.
    Update *checkpoints.txt* file to indicate who checked your work and when they did so.

..  WARNING::
    Do not press more than one key on the matrix keypad at a time.
    There are certain combinations of keys that could result in a short-circuit from power to ground, possibly damaging your |developmentBoard|.
    Your |developmentBoard| has some safety measures to prevent damage in that situation, but it would be better for you not to test those safety measures.

Connect your |developmentBoard| to the computer.
In the IDE's Serial Monitor,
notice that there is normally no character after ``Keypad:``, and that
Column pins is normally 1111.
Press the 5 key on the matrix keypad.
Notice that the first line of the message from the |developmentBoard| is now

::

       Keypad:      5        Column pins:  1011    Keypad NAND: 1

In general, when you press a key on the keypad, the corresponding character will be displayed after ``Keypad:``.
When you press 1, 4, 7, or \*, Column pins becomes 0111;
similarly, pressing a key in the :math:`2^{nd}` column causes Column pins to become 1011;
in the :math:`3^{rd}` column, 1101;
and in the :math:`A^{th}` column, 1110.
Be sure to test all 16 keys.
