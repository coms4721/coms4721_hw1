#Problem 4

##a
$C = \{red, orange, yellow, green, blue\}$

$n = 100\ balls$

$n_{red}, n_{orange}, n_{yellow}, n_{green}, n_{blue}$

$p(red) = n_{red}/n$

$p(red,red) = n_{red}/n * n_{red}/n$

$p(different color) = 1 - p(same color)$

$ = 1 - [p(red,red) + p(orange,orange) + p(yellow,yellow) + p(green,green) + p(blue,blue)]$

$ = 1 -  \sum_{c \in C} (n_c/n)^2 $

$ = 1 - \sum_{c} (p_c)^2 $

##b

$entropy H = - \{p \ log \ p + (1-p)log(1-p)\} $

$max \ H \ wrt \ p \rightarrow p = 0.5 $

$ H = - \sum_k P_k logpk $

Paint each color 20 times. 

$ \sigma (\omega_0 + \omega_1 x_1 + \omega_2 x_2 + ... )  \rightarrow [0,1] $

$ P ( \ Y_{class} = 1 \ | \ X_{data} ) $

$posterior$

$P(Y=1|X) = \dfrac{P(X,Y=1)}{P(X)} $

$ = \dfrac{P(X|Y=1)P(Y)}{P(X)} $

$ \propto P(X|Y=1)P(Y) $

  $ \ \ \ likelihood    - prior$
  
$ P(Yes_{Y=1}) = 0.001 $

$\pi_1 = '' $

$ P(Yes_{Y=0}) = 0.999 $

$\pi_0 = '' $

$ \pi_1 = 200/300 = 2/3 $
$ \pi_2 = 100/300 = 1/3 $

$ not \rightarrow P(X|C_1) \ vs. P(X|C_2) $

$ V \rightarrow P(C_1|X) \ vs. P(C_2|X) $

$ P(X|C_1) \pi_1 = P(X|C_2) \pi_2 \ C $

$ \ \ \ \ \ \ \ \ * 2/3 \ \ \ \ \ \ \ \ \ \ \ \ * 1/3 $

$ P(X|C_1) \pi_1 = P(X|C_2) \pi_2 C $

$ find \ x $

$ \pi_0 = 2/3 \ \pi_1 = 1/3 $

$ P(X|Y=0) = N(0,1) = \dfrac{1}{	\sqrt{2 \pi}} e^{-1/2*x^2} $ 

$ P(X|Y=1) = N(1,1/4) = \dfrac{1}{	\sqrt{2 \pi*{1/4}}} e^{-1/2*{(x-1)^2}/(v4)} $ 

$ P(X|Y = 0) \pi_0 = P(X|Y=1) \pi_1 C$



$f* (x) = \bigg\{ \begin{array}\ 0 \ \ \ \ x <b_1 \\ 1 \ \ \ \ b_1<x<b_2\\ 0 \ \ \ \ x > b_2\end{array} $