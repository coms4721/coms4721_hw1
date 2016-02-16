#Problem 4

$C = \{red, orange, yellow, green, blue\}$

$n = 100\ balls$

$n_{red}, n_{orange}, n_{yellow}, n_{green}, n_{blue}$

$p(red) = n_{red}/n$

$p(red,red) = n_{red}/n * n_{red}/n$

$p(different color) = 1 - p(same color)$

$ = 1 - [p(red,red) + p(orange,orange) + p(yellow,yellow) + p(green,green) + p(blue,blue)]$

$ = 1 -  \sum_{c \in C} (n_c/n)^2 $

$ = 1 - \sum_{c} (p_c)^2 $