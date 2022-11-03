# ACSL Concept 3

## What does This Program Do?

This section is *mostly* about reading, understanding, and parsing ACSL's pseudocode. From the ACSL site, here are some examples of problems:

# Example Problems

## Problem 1

After this program is executed, what is the value of `B` that is printed if the input values are 50 and 10?

```lua
input H, R
B = 0
if H>48 then
	B = B + (H - 48) * 2 * R
	H = 48
end if
if H>40 then
	B = B + (H - 40) * (3/2) * R
	H = 40
end if
B = B + H * R
output B
```

***

## Problem 2

After the following program is executed, what is the final value of `NUM`?

```lua
A = “BANANAS”
NUM = 0: T = “”
for J = len(A) - 1 to 0 step –1
	T = T + A[j]
next
for J = 0 to len(A) - 1
	if A[J] == T[J] then NUM = NUM + 1
next
```

***

## Problem 3

After the following program is executed, what is the final value of `C[4]`?

```lua
A(0) = 12: A(1) = 41: A(2) = 52
A(3) = 57: A(4) = 77: A(5) = -100
B(0) = 17: B(1) = 34: B(20) = 81
J = 0: K = 0: N = 0
while A(J) > 0
	while B(K) <= A(J)
		C(N) = B(K)
		N = N + 1
		k = k + 1
	end while
	C(N) = A(J): N = N + 1: J = J + 1
end while
C(N) = B(K)
```

***

## Problem 4

What is printed when this program is run?

```lua
a = 1: b = 2: c = 3: d = 4: e = 4: f = 6
if (d / b) < (f / a) then d = d / b
a = f ↑ b / c ↑ (d / b)
if (a <= f) && (b > e) then a = f else b = e
if abs(c - f) != int(f / c) then c = f / c else f = f / c
if (a = = b) | | (c = = d) then a = a + b
c = c + d
output (b * c) * (f + d) / a / 2 * d - c + e ↑ (b - 2 * d)
```

***

# Solutions

## Problem 1

This program computes an employee’s weekly salary, given the hourly rate (R) and the number of hours worked in the week (H). The employee is paid an hourly rate for the number of hours worked, up to 40, time and a half for the overtime hours, up to 48 hours, and double for all hours over 48. The table monitors variables B and H:


| B   | H  |
| --- | -- |
| 0   | 50 |
| 40  | 48 |
| 160 | 40 |
| 560 | 40 |

Therefore, the final value of B is **560**:

`2*2*10 + 8*3/2*10 + 40*10 = 40 + 120 + 400 = 560`

***

## Problem 2

The program first stores the reverse of variable `A` into variable `T` and then counts the number of letters that are in the same position in both strings. Variable `NUM` is incremented each time a character at position `x` of `A` is the same as the character in position `x` of string `T`. **There are 5 such positions: 1, 2, 3, 4, and 5.**

***

## Problem 3

The following table traces the variables through the execution of the program.


| J | K | N | A(J) | B(K) | C(N) |
| - | - | - | ---- | ---- | ---- |
| 0 | 0 | 0 | 12   | 17   | 12   |
| 1 | 0 | 1 | 41   | 17   | 17   |
| 1 | 1 | 2 | 41   | 34   | 34   |
| 1 | 2 | 3 | 41   | 81   | 41   |
| 2 | 2 | 4 | 52   | 81   | 52   |
| 3 | 2 | 5 | 57   | 81   | 57   |
| 4 | 2 | 6 | 77   | 81   | 77   |
| 5 | 2 | 7 | -100 | 81   | 81   |

Thus, the value of `C(4)` is **52**. Note that this program merges two arrays in increasing order into one array until a negative number is input.

***

## Problem 4

The following table contains the values of `a`, `b`, `c`, `d`, `e`, and `f` after each line:

| a  | b | c | d | e | f |
| -- | - | - | - | - | - |
| 1  | 2 | 3 | 4 | 4 | 6 |
| 1  | 2 | 3 | 2 | 4 | 6 |
| 12 | 2 | 3 | 2 | 4 | 6 |
| 12 | 4 | 3 | 2 | 4 | 6 |
| 12 | 4 | 2 | 2 | 4 | 6 |
| 16 | 4 | 2 | 2 | 4 | 6 |
| 16 | 4 | 4 | 2 | 4 | 6 |

```py
(b * c) * (f + d) / a / 2 * d - c + e ↑ (b - 2 * d)
= (4 * 4) *(6 + 2) / 16 / 2 * 4 - 4 + 4 ↑ (4 - 2 * 2)
= 16 * 8 / 16 / 2 * 4 - 4 + 40
= 128 / 16 / 2 * 2 - 4 + 1 = 8 / 2 * 2 - 4 + 1 = 5
```

Output: **5**