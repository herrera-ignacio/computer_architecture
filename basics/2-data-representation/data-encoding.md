# Data Encoding

* Codes for Data Recording and Transmission
    * Data Encoding definition

## Codes for Data Recording and Transmission

ASCII, EBCDIC, and Unicode are represented unambiguously in computer memories. However,
when data is written to some sort of recording medium (such as a tape or disk),
or transmitted over long distances, binary signals can become blurred. This blurring
is partly attributable to timing drifts that occur between senders and receivers. Signal
transitions between the "high" and "low" states of digital signals help to maintain 
synchronization in data recording and communication devices.

To this end, ASCII, EBCDIC and Unicode are __translated into other codes before they
are transmitted or recorded__. This translation is carried out by control
electronics within data recording and transmission devices. __Neither the user nor the
host computer is ever aware that this translation has taken place__.
 
Bytes are sent and received by telecommunications devices by using "high" and "low"
pulses in the transmission media (copper wire, for example). Magnetic storage devices
record data using changes in magnetic polarity called _flux reversals_. __Certain
coding methods are better suited for data communications than for data recording__.

#### Data Encoding

For the sake of brevity, we will use the term __Data encoding__ to mean the process of
converting a simple character code such as ASCII to some other code that better lends
itself to storage or transmission. _Encoded data_ will be used to refer to character
codes so encoded.
