# Fibonacci

This is the fastest algorithm I could come up with for the Fibonacci sequence in Python. After coding a solution with $ O(\sqrt{n}) $ time complexity, I managed to decrease it to just $ O(\log{n}) $ using identities of the Lucas sequence. However, for very large $ n $, this algorithm is closer to having $ O(\log^2{n}) $ time complexity.

## Lucas Sequence Identities

These identities serve as the basis for the algorithm.

- $ F_{2n} = F_nL_n $
- $ L_{2n} = L_n^2-2(-1)^n $
- $ 2F_{n+1} = F_n+L_n $
- $ 2L_{n+1} = 5F_n+L_n $

## Explanation

Any Fibonacci number $ F_n $ can be calculated if the previous Fibonacci and Lucas numbers $ F_{n-1} $ and $ L_{n-1} $ are known or if the middle Fibonacci and Lucas numbers $ F_{\frac{n}{2}}$ and $ L_{\frac{n}{2}} $ exist. 

1. If $ n $ is zero, return the base cases $ F_0 $ and $ L_0 $.
2. If $ n $ is odd, make it even by calculating $ F_{n-1} $ and $ L_{n-1} $.
3. If $ n $ is even, half it by calculating $ F_{\frac{n}{2}}$ and $ L_{\frac{n}{2}} $.

Halving $ n $ every step is what gives the algorithm its $ O(\log{n}) $ time complexity. Even when $ n $ is in the form $ 2^k-1 $, the algorithm ensures that the next $ n $ will be even if it is currently odd, making it only twice as slow as the best case scenario when $ n $ is in the form $ 2^k $.

These steps correlate with the binary representation of $ n $. For example, $ n = 100 $ can also be written as $ n = 1100100_2 $. If the right bit is $ 0 $, then $ n $ is shifted to the right. Otherwise, it is set to $ 0 $ before shifting to the right. This results in the following steps:
1. `0` $ 100 $
2. `0` $ 50 $
3. `1` $ 25, 24 $
4. `0` $ 12 $
5. `0` $ 6 $
6. `1` $ 3, 2 $
7. `1` $ 1, 0 $
