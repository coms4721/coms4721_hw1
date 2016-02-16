#Problem 2

$P(X\ | \ class) = 	\prod_{j = 1}^{d} \mu_{j}^{x_j} (1 - \mu_j )^{x_j}$

$L = log(.....) \rightarrow \left(\frac{\delta L}{\mu_j} \right) = \delta $

$P(motorcycle) \ P(gas)....P(mouse) \leftarrow O$

$ \delta/N \rightarrow \left(\frac{1+O}{2+N} \right)$

$ = ( MLE \ | \ Laplace ) $

$P(Y \ | \ X) $

$prediction = argmax_{forum} \  P(Y=forum | X) $

$ \propto P(X|forum) P(forum) $

$ \Rightarrow \prod_{j=1}^d \mu_j^{x_j}(1-\mu_j)^{1-x_j}$ # forum/total 

$ P(data|\mu) \rightarrow $
$P(data|\mu forum_1)$ ,
$P(data|\mu forum_2)$

$Likelihood = \prod P(word \ appears) \ \ \ P(!word \ appears)$

$argmax_y ( \prod_{j=1}^d \mu_{y,j}^{x_j} (1-\mu_{y,j})^{1-x_j} )  \pi_y$

$Linear \ classification: y = w_o + w_1x_1 + w_2x_2 + ...$

$y = mx+b = w_o + \sum_{j=1}^d w_jx_j $

$ log[( \prod_{j=1}^d \mu_{y,j}^{x_j}  (1 - \mu_{y,j} )^{1-x_j} ) \pi_y ] $

$= log \pi_y + \sum_{j=1}^d x_j log \mu_{y,j} + (1-x_j)log(1- \mu_{i,j})$

$= log \pi_y + \sum_{j} log (1- \mu_{i,j}) + \sum_j [ log\mu_{j,y}  * log(1- \mu_{i,j} ) ] x_j $

$ = b_y + w_{y} x_j \rightarrow w_{y(forum \ or \ class),j(dimension \ or \ word \ index)} $

$ \prod_{j=1} \mu ..... (1- \mu ) \prod_y $

$ b + wx (dot product) $


