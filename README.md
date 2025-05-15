This a brief description of the files above.

# Exact solutions to relativistic stars in gravity and beyond

## Exact static spherical symmetric solutions in general relativity
The Mathematica notebook _Tolman static spheres.nb_ rederives the solutions in [Tolman's 1939 seminal paper](https://journals.aps.org/pr/abstract/10.1103/PhysRev.55.364) using the $(- + + +)$ metric signature.

## Exact solutions to relativistic stars in $f(R)$ gravity
The following were used to calculate and plot the solutions in the article [Some exact relativistic star solutions in f(R) gravity](https://iopscience.iop.org/article/10.1088/1361-6382/adc8f2).

+ The file ***Complete stellar reconstruction case I.nb*** calculates the exact solutions for a quadratic model of gravity assuming an interior Schwarzschild-Tolman IV metric.
+ The file ***Complete stellar reconstruction case II.nb*** calculates the exact solutions for a quadratic model of gravity assuming a generic static, spherically symmetric interior metric.
+ The file ***Parameter space analysis solution I.nb*** performs the parameter space analysis, checking the condition $`0<c_{m,r}^{2}<1`$, for the first case (interior Schwarzschild-Tolman IV). The parameter space analysis for the second case follows the same steps -- this file is not listed since it exceeds the allowed file size.
+ The file ***Stellar solution I.nb*** contains only the full expressions of the matter and curvature fluids for the first case.
+ The file ***parameterspace.py*** outputs 3D parameter space plots. The exported _.tx_ files from the mathematica notbook performing the parameter space analysis are used.
+ The _.txt_ files _starobinsky4sphere1000pts.txt_ and _starobinskycausalsphere1000pts.txt_ are the random generated parameter values and the parameter values that satisfy causality respectively. These files correspond to the parameter space analysis performed for the second case (a generic metric) and is included here as an example to the python file's output. 
