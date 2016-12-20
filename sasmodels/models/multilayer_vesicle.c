static
double multilayer_vesicle_kernel(double q,
          double volfraction,
          double radius,
          double thick_shell,
          double thick_solvent,
          double sld_solvent,
          double sld,
          int n_pairs)
{
    //calculate with a loop, two shells at a time
    int ii = 0;
    double fval = 0.0;
    double voli = 0.0;
    const double sldi = sld_solvent-sld;

    do {
        double ri = radius + (double)ii*(thick_shell + thick_solvent);

        // layer 1
        voli = M_4PI_3*ri*ri*ri;
        fval += voli*sldi*sph_j1c(ri*q);

        ri += thick_shell;

        // layer 2
        voli = M_4PI_3*ri*ri*ri;
        fval -= voli*sldi*sph_j1c(ri*q);

        //do 2 layers at a time
        ii += 1;

    } while(ii <= n_pairs-1);  //change to make 0 < n_pairs < 2 correspond to
                               //unilamellar vesicles (C. Glinka, 11/24/03)

    fval *= volfraction*1.0e-4*fval/voli;

    return(fval);
}

static
double Iq(double q,
          double volfraction,
          double radius,
          double thick_shell,
          double thick_solvent,
          double sld_solvent,
          double sld,
          double fp_n_pairs)
{
    int n_pairs = (int)(fp_n_pairs + 0.5);
    return multilayer_vesicle_kernel(q,
           volfraction,
           radius,
           thick_shell,
           thick_solvent,
           sld_solvent,
           sld,
           n_pairs);
}

