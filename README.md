# PascalAndMore
A pascal triangle generator. Also, make your own pascal triangle with alternating operations.

TO RUN: type 
```python pyramid.py --n <int> --ops <comma separated list>```
n >= 1; ops: +, -, *, %, div

```
- : inner - outer
/ : inner / outer
% : outer % inner
```
Example: python pyramid.py --n 8 --ops +
(Generates pascal's triangle)

Example: python pyramid.py --n 8 --ops +,*
(Generates a triangle with alternating + and * operations)

Explination:
``` python pyramid.py --n 7 --ops="+,+,*" ```

Output

                                  1       
                                  +
                               1      1      
                                  +
                           1      2      1      
                              *       *
                        1      2      2      1     
                           +      +      +
                    1      3      4      3      1     
                        +      +      +      +
                 1      4      7      7      4      1
                    *      *       *     *      *
             1      4     28      49     28     4      1   
