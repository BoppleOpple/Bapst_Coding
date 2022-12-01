# ACSL Concept 4

## Bit-String Flicking

This section is about performing bitwise operations (`NOT`, `AND`, `OR`, and `XOR`) and bit-shifting on binary numbers by evaluating each digit of the number as a boolean, with `1 = true` and `0 = false`. For instance, `NOT` `25` would be solved as follows: 25 = 11001<sub>2</sub> so `NOT` 25 = `NOT` 11001<sub>2</sub> = 00110<sub>2</sub> = 6. In pseudocode, this is essentially equivalent to
```lua
input binaryString
outputString = ""
for i = 0 to len(binaryString) - 1
	if binaryString[i] = "0" then
		outputString = outputString + "1"
	else
		outputString = outputString + "0"
	end if 
next
```
Here are examples of each operation:
### `NOT`
The boolean expression `NOT` (shown as `~` or `¬`) inverts the value of the following boolean, so `NOT true` is `false` and `NOT false` is `true`:

| `A` | `~A` |
| --- | ---- |
| 0   | 1    |
| 1   | 0    |

### `AND`
`AND`(`&`) takes two arguments (just like addition or subtraction) and returns `true` if and only if both arguments are `true`:

| `A` | `B` | `A & B` |
| --- | --- | ------- |
| 1   | 1   | 1       |
| 1   | 0   | 0       |
| 0   | 1   | 0       |
| 0   | 0   | 0       |

Because it takes two arguments, its respective bitwise operator behaves differently to `NOT`, and takes two arguments and compares their bits simultaneously. Consider 18 and 7:
|  Number  | Bit 5 (16) | Bit 4 (8) | Bit 3 (4) | Bit 2 (2) | Bit 1 (1) |
| -------- | ---------- | --------- | --------- | --------- | --------- |
| 18       | 1          | 0         | 0         | 1         | 0         |
| 7        | 0          | 0         | 1         | 1         | 1         |
| 18 `&` 7 | 0          | 0         | 0         | 1         | 0         |

so 18 `&` 7 is 2.

### `OR`
`OR`(`|`) is similar to `AND`, but the operation returns `true` if either of the two inputs are `true`, and `false` when they are both `false`. Again, consider 18 and 7:
|  Number  | Bit 5 (16) | Bit 4 (8) | Bit 3 (4) | Bit 2 (2) | Bit 1 (1) |
| -------- | ---------- | --------- | --------- | --------- | --------- |
| 18       | 1          | 0         | 0         | 1         | 0         |
| 7        | 0          | 0         | 1         | 1         | 1         |
| 18 `|` 7 | 1          | 0         | 1         | 1         | 1         |
 1
so 18 `|` 7 is 23.

### `XOR` (eXclusive OR)
Finally, `XOR`(`⊕`) is basically just a stricter `OR`: it returns `true` when **ONLY ONE** of the two inputs is `true`, and `false` otherwise. For the last time, consider 18 and 7:
| Number | Bit 5 (16) | Bit 4 (8) | Bit 3 (4) | Bit 2 (2) | Bit 1 (1) |
| ------ | ---------- | --------- | --------- | --------- | --------- |
| 18     | 1          | 0         | 0         | 1         | 0         |
| 7      | 0          | 0         | 1         | 1         | 1         |
| 18 ⊕ 7 | 1          | 0         | 1         | 0         | 1         |

so 18 `⊕` 7 is 21.

## Bit Shifting

Another set of binary operations uinvolves shifting the bits of a number to the left or right a certain number of bits. The for commands are `LSHIFT`, `RSHIFT`, `LCIRC`, and `RCIRC`. `LSHIFT` and `RSHIFT` insert zeroes, but keep the same number of digits (so `LSHIFT-2` 101 = **10100**, which is truncated to 100, and `RSHIFT-2` 101 = **001** because the last two digits are dropped) but `LCIRC` and `RCIRC` operations "wrap around" the number so `LCIRC-2` 101 = **110**, because the two digits which are dropped by `LSHIFT` are appended to the end instead of zeroes, and `RSHIFT-2` 101 = **011** for the same reason).

## Order of Operations
Bitwise operations, like other numerical operations, are performed in a certain order:

1. `NOT`
2. `LSHIFT`, `RSHIFT`, `LCIRC`, or `RCIRC`
3. `AND`
4. `XOR`
5. `OR`

# Problems

## Problem 1

Evaluate the following expression:

> (101110 `AND` `NOT` 110110 `OR` (`LSHIFT-3` 101010))

## Problem 2

Evaluate the following expression:

> (`RSHIFT-1` (`LCIRC-4` (`RCIRC-2` 01101)))

## Problem 3

List all possible values of x (5 bits long) that solve the following equation.

> (`LSHIFT-1` (10110 `XOR` (`RCIRC-3` **x**) AND 11011)) = 01100

# Solutions

## Problem 1

The expression evaluates as follows: 

> (101110 `AND` 001001 `OR` (`LSHIFT-3` 101010))
>
> (001000 `OR` (`LSHIFT-3` 101010))
>
> (001000 `OR` 010000)
>
> 011000

## Problem 2

The expression evaluates as follows, starting at the innermost parentheses:

> (`RCIRC-2` 01101) => 01011
>
> (`LCIRC-4` 01011) => 10101
>
> (`RSHIFT-1` 10101) = 01010

## Problem 3

Since `x` is a string 5 bits long, represent it by abcde.

> (`RCIRC-3` abcde) => cdeab
>
> (cdeab `AND` 11011) => cd0ab
>
> (10110 `XOR` cd0ab) => Cd1Ab (the capital letter is the `NOT` of its lower case)

> (`LSHIFT-1` Cd1Ab) => d1Ab0

So, d1Ab0 = 01100.

Meaning, we must have d=0, A=1 (hence a=0), b=0. Thus, the solution must be in the form 00*0*, where * is an “I-don’t-care”.

The four possible values of x are: 00000, 00001, 00100 and 00101. 

## Problem 4

The problem can be rewritten as

> A `|` B `&` C

The `AND` has higher precedence than the OR.

The evaluation of expression A can be done in a straightforward way: (`LCIRC-23` 01101) is the same as (`LCIRC-3` 01101) which has a value of 01011, and (`RCIRC-14` 01011) is the same as (`RCIRC-4` 01011) which has a value of 10110. Another strategy is to offset the left and right circulates. So, ((`RCIRC-14` (`LCIRC-23` 01101)) has the same value as (`LCIRC-9` 01101), which has the same value as (`LCIRC-4` 01101) which is also 11010.

Expressions B and C are pretty easy to evaluate:

> B = (`LSHIFT-1` 10011) = 00110
>
> C = (`RSHIFT-2` 10111) = 00101

The expression becomes

> A `|` B `&` C = 10110 `|` 00110 `&` 00101 = 10110 `|` 00100 = 10110