# Tutorial #8

### 1

ponto (4,7) e curva y<sup>2</sup> = x<sup>3</sup> − 5x + 5 

**Em $\mathbb{Z}_{23}$:**

Substituir x = 4 em **x<sup>3</sup> - 5x + 5 mod 23**:

4<sup>3</sup> - 5 * 4 + 5 mod 23 = 3

Calcular **y<sup>2</sup> mod 23** para y = 7:

7<sup>2</sup> mod 23 = 3

Como y<sup>2</sup> $\equiv$ x<sup>3</sup> - 5x + 5 mod 23, o ponto (4,7) pertence à curva y<sup>2</sup> = x<sup>3</sup> − 5x + 5 $\mathbb{Z}_{23}$.

---

**Em $\mathbb{R}$:**

Substituir x = 4 em **x<sup>3</sup> - 5x + 5**:

4<sup>3</sup> - 5 * 4 + 5 = 49

Verificar se y = 7 satisfaz y<sup>2</sup>:

7<sup>2</sup> = 49

Como y<sup>2</sup> = x<sup>3</sup> - 5x + 5, o ponto (4,7) pertence à curva y<sup>2</sup> = x<sup>3</sup> − 5x + 5 $\mathbb{R}$.

Logo, o ponto (4,7) pertence à curva y<sup>2</sup> = x<sup>3</sup> − 5x + 5 em $\mathbb{Z}_{23}$ e em $\mathbb{R}$.

### 2

P = (-2, 2) e Q = (3, 3) e a curva y<sup>2</sup> = x<sup>3</sup> − 6x

**Calcular P + Q**

declive m = $\frac{3 - 2}{3 - (-2)}$ = $\frac{1}{5}$

x_r = $\left(\frac{1}{5}\right)^2$ - (-2) - 3 = $\frac{1}{25}$ + 2 - 3 = -$\frac{24}{25}$

y_r = $\frac{1}{5}\left(-2 - \left(-\frac{24}{25}\right)\right)$ - 2 = -$\frac{276}{125}$

Portanto, R = P + Q = $\left(-\frac{24}{25}, -\frac{276}{125}\right)$.

---

**Calcular 2P**

declive m = $\frac{3(-2)^2 - 6}{2 *2} = \frac{12}{4}$ = 3

x_r = 3<sup>2</sup> + 2 + 2 = 13

y_r = 3 * (- 2 - 13) - 2 = -47

Portanto, R = 2P = (13, -47).

### 3

O código está implementado no ficheiro **ex3_tutorial.py** e a imagem abaixo mostra a execução do código.

![ex3](image1.png)

### 4

O código está implementado no ficheiro **ex4_tutorial.py** e a imagem abaixo mostra a execução do código.

![ex4](image2.png)

### 5

O código para as 3 alíneas está implementado no ficheiro **ex5_tutorial.py**. Cada alínea está identificada com um comentário no código. A imagem abaixo mostra a execução do código.

![ex5](image3.png)



