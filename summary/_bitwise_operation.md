## Basic

```python
# And
x & y

# Or
x | y

# XOR
x ^ y

# NOT
~x # ~1 -> -2

# Bit shift
x << 1
y >> 2
```

|operator | and   |  or |  xor  | not  |
|---------|:-----:|:---:|:-----:|-----:|
|keep same|   &1  | \|0 |  ^0   |      |
|special  |&0 dump to 0| \|1 raise to 1| ^1 toggle bit | ~x+1 = -x

**Example**

For any number x,  x & `0xffffffff` will be the first 32 bit of x, 32 bit to 64 bit will be dumped to 0. Since python number is 64 bit. Use mask `0xffffffff` to truncate bit will be commonly used.

Use xor to for finding the only unpair elements in a list:
```python
arr = [1,2,1,3,2]
r = 0
for x in arr:
    r ^= x
return r

# r = 3
```

## Letter <-> ascii

```python
# char -> ascii
ord('a') # 97

# ascii -> char
chr(97) # 'a'

```

## XOR

```python
0 ^ x = x
x ^ x = 0

# commutative
x ^ y =  y ^ x

# associative
x ^ y ^ z  = x ^ (y ^ z)
x^y^x = y
# the attributes of xor


x & (x-1)
# unset the rightmost 1 of x
##  x-1 will toggle all 0 and 1 until the rightmost 1
##  example 11000 minus 1 -> 10111
##          11000 ^ 10111 -> 10000
##          the rightmost 1 is removed!

x & 0xf
# get the first four bit
## 0xf is actually 1111 in binary
## example 10010100010 ^ 1111 -> 0010
```





## Other Examples



### Get Negative Number

```python
-x = ~x + 1
```
### Add Two Number

```python

```

### Power of four

```python

```
