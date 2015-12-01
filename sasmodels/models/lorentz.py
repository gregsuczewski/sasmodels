r"""
Lorentz (Ornstein-Zernicke Model)

Definition
----------

The Ornstein-Zernicke model is defined by

.. math:: I(q)=\frac{\text{scale}}{1+(qL)^2}+\text{background}

The parameter $L$ is the screening length *cor_length*.

For 2D data the scattering intensity is calculated in the same way as 1D,
where the $q$ vector is defined as

.. math:: q=\sqrt{q_x^2 + q_y^2}

.. figure:: img/lorentz_1d.jpg

    1D plot using the default values (w/200 data point).

References
----------

L.S. Qrnstein and F. Zernike, *Proc. Acad. Sci. Amsterdam* 17, 793 (1914), and
*Z. Phys.* 19, 134 (1918), and 27, 761 {1926); referred to as QZ.
"""

from numpy import inf

name = "lorentz"
title = "Ornstein-Zernicke correlation length model"
description = """
Model that evaluates a Lorentz (Ornstein-Zernicke) model.
        
I(q) = scale/( 1 + (q*L)^2 ) + bkd
        
The model has three parameters: 
    length     =  screening Length
    scale  =  scale factor
    background    =  incoherent background
"""
category = "shape-independent"

#             ["name", "units", default, [lower, upper], "type","description"],
parameters = [["cor_length", "Ang", 50.0, [0, inf], "", "Screening length"],]

Iq = """
    double denominator = 1 + (q*cor_length)*(q*cor_length);
    return 1/denominator;
"""

Iqxy = """
    return Iq(sqrt(qx*qx + qy*qy), cor_length);
    """

# parameters for demo
demo = dict(scale=1.0,background=0.0,cor_length=50.0)

# For testing against the old sasview models, include the converted parameter
# names and the target sasview model name.
oldname = 'LorentzModel'
oldpars = dict(cor_length='length')

# parameters for unit tests
tests = [
         [{'cor_length' : 250},0.01,0.137931]
         ]