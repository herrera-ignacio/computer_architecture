# Data Representation

## Glossary

#### bit (1 or 0)

The most basic unit of information in a digital computer. In the
concrete sense, a bit is nothing more than a state of "on" or "off"
within a computer circuit.

#### byte

In 1964 established a convention of using groups of 8 bits as the
basic unit of addressable computer storage. They called this collection
of 8 bits as byte_.

#### word

Consist of __two or more adjacent bytes__ that are sometimes
addressed and almost always are manipulated collectively.

The __word size__ represents the data size that is handled most
efficiently by a particular architecture.

#### nibbles

8-bit bytes can be divided into 4-bit halves called nibbles/nybbles.
The nibble containing the least-valued binary digit is called low-order nibble.

## Positional Numbering Systems

| Decimal 	| 4-Bit     	| Hexadecimal 	|
|---------	|--------------	|-------------	|
| 0       	| 0000         	| 0           	|
| 1       	| 0001         	| 1           	|
| 2       	| 0010         	| 2           	|
| 3       	| 0011         	| 3           	|
| 4       	| 0100         	| 4           	|
| 5       	| 0101         	| 5           	|
| 6       	| 0110         	| 6           	|
| 7       	| 0111         	| 7           	|
| 8       	| 1000         	| 8           	|
| 9       	| 1001         	| 9           	|
| 10      	| 1010         	| A           	|
| 11      	| 1011         	| B           	|
| 12      	| 1100         	| C           	|
| 13      	| 1101         	| D           	|
| 14      	| 1110         	| E           	|
| 15      	| 1111         	| F           	|

#### Converting Unsigned Whole Numbers

A binary number with __N bits__ can represent unsigned integers
from 0 to (2^N)-1.

For example, 4 bits can represent the decimal values 0 through 15.

* repeated subtraction
* division-reminder method

#### overflow

The range of values that can be represented by a given number of bits
is extremely important when doing arithmetic operations on
binary numbers. If we wish to add 1111 (15) to 1111 (15), we cannot represent
the result (30) using only 5 bits.

This is an example of a condition known as __overflow__, which occurs
in unsigned binary representation when the result of an arithmetic
operation is outside the range of allowable precision
for the given number of bits.
