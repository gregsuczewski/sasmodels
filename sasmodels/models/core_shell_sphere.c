double form_volume(double radius, double thickness);
double Iq(double q, double radius, double thickness, double core_sld, double shell_sld, double solvent_sld);

double Iq(double q, double radius, double thickness, double core_sld, double shell_sld, double solvent_sld) {


    double intensity = core_shell_kernel(q,
                              radius,
                              thickness,
                              core_sld,
                              shell_sld,
                              solvent_sld);
    return intensity;
}

static void Fq(double q, double *F1, double *F2, double radius, double thickness, double core_sld, double shell_sld, double solvent_sld) {


    double intensity = core_shell_kernel(q,
                              radius,
                              thickness,
                              core_sld,
                              shell_sld,
                              solvent_sld);
    *F2 = intensity;
    *F1 = intensity**(1./2.);
}

double form_volume(double radius, double thickness)
{
    return M_4PI_3 * cube(radius + thickness);
}
