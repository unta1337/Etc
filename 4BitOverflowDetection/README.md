# 4BitOverflowDetection

Python & Wolfram Language code to detect overflow in 4-bit addition and subtraction.

## python/4BitOverflowDetection.py

This code was written with Visual Sudio Code Python Interactive Mode.

.csv file was reformatted after its genoration. (Convert into .xlsx and changed a color format.)

![image](https://user-images.githubusercontent.com/51486948/119360132-479df900-bce5-11eb-9650-e9a76b475fb1.png)

## mathematica/4BitOverflowDetection.nb
```
Grid[Table[
  Item[ToExprFullString[X, 
    Y], {Background -> 
     If[GetExprValue[**BOOLEAN_EXPRESSION**, X, Y], Red, White]}], {X, 0, 
   16 - 1}, {Y, 0, 16 - 1}], Frame -> All]
```
### Overflow detection
![](https://user-images.githubusercontent.com/58779799/120081820-6ee83200-c0fa-11eb-9141-00ec71c6e77c.png)

### Zero detection
![](https://user-images.githubusercontent.com/58779799/120081822-70b1f580-c0fa-11eb-9371-d3416e9e0484.png)

### Negative detection
![](https://user-images.githubusercontent.com/58779799/120081825-71e32280-c0fa-11eb-9093-76562881443a.png)

### Full detection
![](https://user-images.githubusercontent.com/58779799/120081827-73ace600-c0fa-11eb-8fe6-5f09eca81212.png)

## Contributor
 - [unta1337 (Python)](https://github.com/unta1337)
 - [refracta (Wolfram Language)](https://github.com/refracta)