r"""
This model provides the form factor, $P(q)$, for a monodisperse hollow right
angle circular cylinder (tube) where the form factor is normalized by the
volume of the tube

.. math::

    P(q) = \text{scale} \left<F^2\right>/V_\text{shell} + \text{background}

where the averaging $\left<\ldots\right>$ is applied only for the 1D calculation.

The inside and outside of the hollow cylinder are assumed have the same SLD.

Definition
----------

The 1D scattering intensity is calculated in the following way (Guinier, 1955)

.. math::

    %\begin{align*} % isn't working with pdflatex
    \begin{array}{rl}
    P(q)           &= (\text{scale})V_\text{shell}\Delta\rho^2
            \int_0^{1}\Psi^2
            \left[q_z, R_\text{shell}(1-x^2)^{1/2},
                       R_\text{core}(1-x^2)^{1/2}\right]
            \left[\frac{\sin(qHx)}{qHx}\right]^2 dx \\
    \Psi[q,y,z]    &= \frac{1}{1-\gamma^2}
            \left[ \Lambda(qy) - \gamma^2\Lambda(qz) \right] \\
    \Lambda(a)     &= 2 J_1(a) / a \\
    \gamma         &= R_\text{core} / R_\text{shell} \\
    V_\text{shell} &= \pi \left(R_\text{shell}^2 - R_\text{core}^2 \right)L \\
    J_1(x)         &= (\sin(x)-x\cdot \cos(x)) / x^2 \\
    \end{array}

where *scale* is a scale factor and $J_1$ is the 1st order
Bessel function.

To provide easy access to the orientation of the core-shell cylinder, we define
the axis of the cylinder using two angles $\theta$ and $\phi$. As for the case
of the cylinder, those angles are defined in Figure 2 of the CylinderModel.

**NB**: The 2nd virial coefficient of the cylinder is calculated
based on the radius and 2 length values, and used as the effective radius
for $S(q)$ when $P(q) \cdot S(q)$ is applied.

In the parameters, the contrast represents SLD :sub:`shell` - SLD :sub:`solvent`
and the *radius* is $R_\text{shell}$ while *core_radius* is $R_\text{core}$.

.. figure:: img/hollow_cylinder_1d.jpg

    1D plot using the default values (w/1000 data point).

.. figure:: img/orientation.jpg

    Definition of the angles for the oriented hollow_cylinder model.

.. figure:: img/orientation2.jpg

    Examples of the angles for oriented pp against the detector plane.

References
----------

L A Feigin and D I Svergun, *Structure Analysis by Small-Angle X-Ray and
Neutron Scattering*, Plenum Press, New York, (1987)
"""

from numpy import inf

name = "hollow_cylinder"
title = ""
description = """
P(q) = scale*<f*f>/Vol + background, where f is the scattering amplitude.
core_radius = the radius of core
radius = the radius of shell
length = the total length of the cylinder
sld = SLD of the shell
solvent_sld = SLD of the solvent
background = incoherent background
"""
category = "shape:cylinder"

#             ["name", "units", default, [lower, upper], "type","description"],
parameters = [
              ["radius", "Ang", 30.0, [0, inf], "volume", "Cylinder radius"],
              ["core_radius", "Ang", 20.0, [0, inf], "volume", "Hollow core radius"],
              ["length", "Ang", 400.0, [0, inf], "volume", "Cylinder length"],
              ["sld", "1/Ang^2", 6.3, [-inf, inf], "", "Cylinder sld"],
              ["solvent_sld", "1/Ang^2", 1, [-inf, inf], "", "Solvent sld"],
              ["theta", "degrees", 90, [-360, 360], "orientation", "Theta angle"],
              ["phi", "degrees", 0, [-360, 360], "orientation", "Phi angle"],
              ]

source = ["lib/J1.c", "lib/gauss76.c", "hollow_cylinder.c"]

# parameters for demo
demo = dict(scale=1.0,background=0.0,length=400.0,radius=30.0,core_radius=20.0,
            sld=6.3,solvent_sld=1,theta=90,phi=0,
            radius_pd=.2, radius_pd_n=9,
            length_pd=.2, length_pd_n=10,
            theta_pd=10, theta_pd_n=5,
            )

# For testing against the old sasview models, include the converted parameter
# names and the target sasview model name.
oldname = 'HollowCylinderModel'
oldpars = dict(scale='scale',background='background',radius='radius',
               core_radius='core_radius',sld='sldCyl',length='length',
               solvent_sld='sldSolv',phi='axis_phi',theta='axis_theta')

# Parameters for unit tests
tests = [
         [{"radius" : 30.0},0.00005,1764.926]
         ]
