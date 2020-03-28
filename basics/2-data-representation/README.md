# Data Representation

* Glossary
* Positional Number Systems
    * Unsigned whole numbers
    * Signed whole numbers 
        * Signed magnitude
        * Complement system
        * Rule for detecting overflow

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

## Unsigned Whole Numbers

A binary number with __N bits__ can represent unsigned integers
from 0 to (2^N)-1.

For example, 4 bits can represent the decimal values 0 through 15.

#### Conversion methods

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

## Signed Integer Representation

Many programming languages automatically allocate a storage area
that includes a sin as the first bit of the storage location.

By convention a "1" in the high-order bit indicates a negative number.

The storage location can be as small as a byte or as several words.

Common representations:

1. Signed magnitude
2. One's complement
3. Two's complement

### Signed Magnitude

Has a __sign as its left-most__ bit (high-order or most significant bit),
while the remaining bits represent the magnitude (absolute value) of the
numeric value.

For example, in an 8-bit word, `-1` would be represented as `10000001`.

In 8-bit words, 7 bits can be used for the actual representation of the magnitude,
this means that largest magnitude an 8-bit word can represent is 2^7 - 1 (127).

### Complement Systems

Let's say we wanted to find `167 - 52`. Taking the difference of `999 - 52 = 947`.
In nine's complement arithmetic we have `167 - 52 = 167 + 947 = 114`. The "carry"
from the hundreds column is added back to the units place, giving us a correct
`167 - 52 = 115`. This method was commonly called "casting out 9s". The advantage
that complement systems give us over signed magnitude is that there is no need to
process sign bits separately, but we can still easily check the sign of a number
by looking at its high-order bit.

We know the numbers 501-999 represent the radix complements of the numbers 001-500
and are being used to represent negative magnitudes.

### One's Complement

Given a number `N` in base `r` having `d` digits, the diminished radix complement
of `N` is defined to be `(r^d - 1) - N`.

For decimal numbers, `r = 10`, and the diminished radix is 9.

For example, the nine's complement of 2468 is `9999 - 2468 = 7531`. As
`r^d - 1 = 9999`.

For an equivalent operation in binary, we subtract from one less that the base (2), which is 1.

For example, the one's complement of `0101` is `1111 - 0101 = 1010`. This is because `r=2`, `d=4`
and `r^d = 2^4 = 10000 (16)`. And then `r^d - 1 = 1111`.

We could do this operations but a few experiments will convince you that forming
the one's complement of a binary number amounts to nothing more than
__switching all of the 1s with 0s and vice versa__. This sort of bit-flipping is very
simple to implement in computer hardware.

We are most interested in using complement notation to represent negative numbers. We know
that performing a subtraction, such as `10 - 7`, can be also though of as "adding the opposite"
as in `10 + (-7)`.

Complement notation allows us to simplify subtraction by turning it into addition, but it also
give us a method to represent negative numbers, without the need to use a special bit to
represent the sign. We need to remember that if a number is negative, we should convert it
to its complement. The result should have a 1 in the leftmost bit position to indicate the
number is negative. If the number is positive, we don't have to convert it to its complement.
All positive numbers should have a zero in the leftmost bit position.

For example `23 = +(00010111) = 00010111`, and `-9 = -(00001001) = 11110110`.

Now if we wish to subtract 9 from 23, we can carry out a one's complement subtraction. First
by expressing the subtrahend (9) in one's complement, then add it to the minuend (23). We are effectively
now doing `-9 + 23`. The high-order bit will have a 1 or a 0 carry, which is added to the low-order bit of the sum. This
is called __end carry-around__ and results from using the diminished radix complement.

```
23 + (-9):
  00010111 (23)
+ 11110110 (-9)
= 00001101
+ 00000001 (end carry-around)
= 00001110 (14)
```

```
9 + (-23)
  00001001 (9)
+ 11101000 (-23)
= 11110001 (-14)
```

How do we know that `11110001` is actually -14? We simply need to
take the one's complement of this binary number (remembering it must be
negative because the left-most bit is negative). The one's complement is
`00001110` which is 14.

The primary disadvantage of one's complement is that we still have two
representations for zero (`0000 0000` and `1111 1111`). For this and other
reasons, computer engineers long ago stopped using one's complement in favor
of the more efficient two's complement representation for binary numbers.

### Two's Complement

Given a number `N` in base `r` having `d` digits, the radix complement of N is
defined to be `r^d - N` for N != 0 and 0 for N = 0. The radix complement is often
more intuitive than the diminished radix complement.

The two's complement of the 4-bit number `0011` is `2^4 - 0011`, which is the same
as `10000 - 0011 = 1101`.

Upon closer examination, you will discover that two's complement is nothing more
than one's complement increased by 1. Then you can flip bits and add 1.

This simplifies addition and subtraction as well. Since the subtrahend (number
we complement and add) is incremented at the outset, however, there is
no end carry-around to worry about. We simply discard carries involving the
high-order- bits.

Remember, only negative numbers need to be converted to two's complement notation.

* `23 = 0001 0111 = 0001 0111` 
* `-23 = 0001 0111 = 1110 1000 + 1 = 1110 1001`

Finding the sum of two numbers:

```
  0001 0111 (23)
+ 1111 0111 (-9)
= 0000 1110 (14)
```

Notice that the discarded carry in previous example did not cause an erroneous result.

An __overflow__ occurs if two positive numbers are added and the result is negative,
or if two negative numbers are added and the result is positive. It is not possible to have
overflow when using two's complement notation if a positive and a negative number
are being added together.


#### Rule for detecting an overflow condition

Simple computer circuits can easily detect an overflow condition using a rule that is
easy to remember. In previous example you'll notice that the __carry going into the sign bit
is the same as the carry going out of the sign bit__ (a 1 is carried out and discarded). When
__these carries are equal, no overflow occurs__. When they differ, an overflow indicator
is set in the arithmetic logic unit, indicating the result is incorrect.

Example:

```
0 <- 1         (carries)
     0111 1110 (126)
   + 0000 1000 (8)
     1000 0110 (-122?) OVERFLOW
```
