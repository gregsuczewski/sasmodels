#barbell model
# Note: model title and parameter table are inserted automatically
r"""
Calculates the scattering from a barbell-shaped cylinder.  Like
:ref:`capped-cylinder`, this is a sphereocylinder with spherical end
caps that have a radius larger than that of the cylinder, but with the center
of the end cap radius lying outside of the cylinder. See the diagram for
the details of the geometry and restrictions on parameter values.

Definition
----------

.. figure:: img/barbell_geometry.jpg

    Barbell geometry, where $r$ is *radius*, $R$ is *bell_radius* and
    $L$ is *length*. Since the end cap radius $R \geq r$ and by definition
    for this geometry $h < 0$, $h$ is then defined by $r$ and $R$ as
    $h = - \sqrt{R^2 - r^2}$

The scattered intensity $I(q)$ is calculated as

.. math::

    I(q) = \frac{\Delta \rho^2}{V} \left<A^2(q)\right>

where the amplitude $A(q)$ is given as

.. math::

    A(q) =&\ \pi r^2L
        \frac{\sin\left(\tfrac12 qL\cos\theta\right)}
             {\tfrac12 qL\cos\theta}
        \frac{2 J_1(qr\sin\theta)}{qr\sin\theta} \\
        &\ + 4 \pi R^3 \int_{-h/R}^1 dt
        \cos\left[ q\cos\theta
            \left(Rt + h + {\tfrac12} L\right)\right]
        \times (1-t^2)
        \frac{J_1\left[qR\sin\theta \left(1-t^2\right)^{1/2}\right]}
             {qR\sin\theta \left(1-t^2\right)^{1/2}}

The $\left<\ldots\right>$ brackets denote an average of the structure over
all orientations. $\left<A^2(q)\right>$ is then the form factor, $P(q)$.
The scale factor is equivalent to the volume fraction of cylinders, each of
volume, $V$. Contrast $\Delta\rho$ is the difference of scattering length
densities of the cylinder and the surrounding solvent.

The volume of the barbell is

.. math::

    V = \pi r_c^2 L + 2\pi\left(\tfrac23R^3 + R^2h-\tfrac13h^3\right)


and its radius of gyration is

.. math::

    R_g^2 =&\ \left[ \tfrac{12}{5}R^5
        + R^4\left(6h+\tfrac32 L\right)
        + R^2\left(4h^2 + L^2 + 4Lh\right)
        + R^2\left(3Lh^2 + \tfrac32 L^2h\right) \right. \\
        &\ \left. + \tfrac25 h^5 - \tfrac12 Lh^4 - \tfrac12 L^2h^3
        + \tfrac14 L^3r^2 + \tfrac32 Lr^4 \right]
        \left( 4R^3 6R^2h - 2h^3 + 3r^2L \right)^{-1}

.. note::
    The requirement that $R \geq r$ is not enforced in the model! It is
    up to you to restrict this during analysis.

.. figure:: img/barbell_1d.jpg

    1D plot using the default values (w/256 data point).

For 2D data, the scattering intensity is calculated similar to the 2D
cylinder model.

.. figure:: img/barbell_2d.jpg

    2D plot (w/(256X265) data points) for $\theta = 45^\circ$ and
    $\phi = 0^\circ$ with default values for the remaining parameters.

.. figure:: img/orientation.jpg

    Definition of the angles for oriented 2D barbells.

.. figure:: img/orientation2.jpg

    Examples of the angles for oriented pp against the detector plane.

References
----------

H Kaya, *J. Appl. Cryst.*, 37 (2004) 37 223-230

H Kaya and N R deSouza, *J. Appl. Cryst.*, 37 (2004) 508-509 (addenda and errata)
"""
from numpy import inf

name = "barbell"
title = "Cylinder with spherical end caps"
description = """
        Calculates the scattering from a barbell-shaped cylinder. That is a sphereocylinder with spherical end caps that have a radius larger than that of the cylinder and the center of the end cap
        radius lies outside of the cylinder.
        Note: As the length of cylinder(bar) -->0,it becomes a dumbbell. And when rad_bar = rad_bell, it is a spherocylinder.
        It must be that rad_bar <(=) rad_bell.
"""
category = "shape:cylinder"

#             ["name", "units", default, [lower, upper], "type","description"],
parameters = [["sld", "4e-6/Ang^2", 4, [-inf, inf], "", "Barbell scattering length density"],
              ["solvent_sld", "1e-6/Ang^2", 1, [-inf, inf], "", "Solvent scattering length density"],
              ["bell_radius", "Ang", 40, [0, inf], "volume", "Spherical bell radius"],
              ["radius", "Ang", 20, [0, inf], "volume", "Cylindrical bar radius"],
              ["length", "Ang", 400, [0, inf], "volume", "Cylinder bar length"],
              ["theta", "degrees", 60, [-inf, inf], "orientation", "In plane angle"],
              ["phi", "degrees", 60, [-inf, inf], "orientation", "Out of plane angle"],
             ]

source = ["lib/J1.c", "lib/gauss76.c", "barbell.c"]

# parameters for demo
demo = dict(scale=1, background=0,
            sld=6, solvent_sld=1,
            bell_radius=40, radius=20, length=400,
            theta=60, phi=60,
            radius_pd=.2, radius_pd_n=5,
            length_pd=.2, length_pd_n=5,
            theta_pd=15, theta_pd_n=0,
            phi_pd=15, phi_pd_n=0,
           )

# For testing against the old sasview models, include the converted parameter
# names and the target sasview model name.
oldname = 'BarBellModel'
oldpars = dict(sld='sld_barbell',
               solvent_sld='sld_solv', bell_radius='rad_bell',
               radius='rad_bar', length='len_bar')
