#adsorbed_layer model
#conversion of Core2ndMomentModel.py
#converted by Steve King, Mar 2016

r"""
This model describes the scattering from a layer of surfactant or polymer
adsorbed on large, smooth, notionally spherical particles under the conditions
that (i) the particles (cores) are contrast-matched to the dispersion medium,
(ii) $S(Q) \sim 1$ (ie, the particle volume fraction is dilute), (iii) the
particle radius is >> layer thickness (ie, the interface is locally flat),
and (iv) scattering from excess unadsorbed adsorbate in the bulk medium is
absent or has been corrected for.

Unlike many other core-shell models, this model does not assume any form
for the density distribution of the adsorbed species normal to the interface
(cf, a core-shell model normally assumes the density distribution to be a
homogeneous step-function). For comparison, if the thickness of a (traditional
core-shell like) step function distribution is $t$, the second moment about
the mean of the density distribution (ie, the distance of the centre-of-mass
of the distribution from the interface), $\sigma = \sqrt{t^2/12}$.

Definition
----------

.. math::

     I(q) = \text{scale} \cdot (\rho_\text{poly}-\rho_\text{solvent})^2
         \left[
             \frac{6\pi\phi_\text{core}}{Q^2}
             \frac{\Gamma^2}{\delta_\text{poly}^2R_\text{core}}
             \exp(-Q^2\sigma^2)
         \right] + \text{background}

where *scale* is a scale factor, $\rho_\text{poly}$ is the sld of the
polymer (or surfactant) layer, $\rho_\text{solv}$ is the sld of the
solvent/medium and cores, $\phi_\text{core}$ is the volume fraction of
the core particles, $\delta_\text{poly}$ is the bulk density of the
polymer, $\Gamma$ is the adsorbed amount, and $\sigma$ is the second
moment of the thickness distribution.

Note that all parameters except $\sigma$ are correlated so fitting more
than one of these parameters will generally fail. Also note that unlike
other shape models, no volume normalization is applied to this model (the
calculation is exact).

References
----------

S King, P Griffiths, J Hone, and T Cosgrove,
*SANS from Adsorbed Polymer Layers*, *Macromol. Symp.*, 190 (2002) 33-42.
"""

from numpy import inf, sqrt, pi, exp

name = "adsorbed_layer"
title = "Scattering from an adsorbed layer on particles"

description = """
    Evaluates the scattering from large particles
    with an adsorbed layer of surfactant or
    polymer, independent of the form of the
    density distribution.
    """
category = "shape:sphere"

# pylint: disable=bad-whitespace, line-too-long
#   ["name", "units", default, [lower, upper], "type", "description"],
parameters = [
    ["second_moment", "Ang", 23.0, [0.0, inf], "", "Second moment of polymer distribution"],
    ["adsorbed_amount", "mg/m2", 1.9, [0.0, inf], "", "Adsorbed amount of polymer"],
    ["density_shell", "g/cm3", 0.7, [0.0, inf], "", "Bulk density of polymer in the shell"],
    ["radius", "Ang", 500.0, [0.0, inf], "", "Core particle radius"],
    ["volfraction", "None", 0.14, [0.0, inf], "", "Core particle volume fraction"],
    ["sld_shell", "1e-6/Ang^2", 1.5, [-inf, inf], "sld", "Polymer shell SLD"],
    ["sld_solvent", "1e-6/Ang^2", 6.3, [-inf, inf], "sld", "Solvent SLD"],
]
# pylint: enable=bad-whitespace, line-too-long

# NB: Scale and Background are implicit parameters on every model
def Iq(q, second_moment, adsorbed_amount, density_shell, radius,
       volfraction, sld_shell, sld_solvent):
    # pylint: disable = missing-docstring
    #deltarhosqrd =  (sld_shell - sld_solvent) * (sld_shell - sld_solvent)
    #numerator =  6.0 * pi * volfraction * (adsorbed_amount * adsorbed_amount)
    #denominator =  (q * q) * (density_shell * density_shell) * radius
    #eterm =  exp(-1.0 * (q * q) * (second_moment * second_moment))
    ##scale by 10^-2 for units conversion to cm^-1
    #inten =  1.0e-02 * deltarhosqrd * ((numerator / denominator) * eterm)
    aa = (sld_shell - sld_solvent) * adsorbed_amount / q / density_shell
    bb = q * second_moment
    #scale by 10^-2 for units conversion to cm^-1
    inten = 6.0e-02 * pi * volfraction * aa * aa * exp(-bb * bb) / radius
    return inten
Iq.vectorized =  True  # Iq accepts an array of q values

# unit test values taken from SasView 3.1.2
tests =  [
    [{'scale': 1.0, 'second_moment': 23.0, 'adsorbed_amount': 1.9,
      'density_shell': 0.7, 'radius': 500.0, 'volfraction': 0.14,
      'sld_shell': 1.5, 'sld_solvent': 6.3, 'background': 0.0},
     [0.0106939, 0.1], [73.741, 4.51684e-3]],
]

# 2016-03-16 SMK converted from sasview, checked vs SANDRA
# 2016-03-18 RKH some edits & renaming
# 2016-04-14 PAK reformatting
