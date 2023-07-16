"""
For interpreting the LaTeX equations, https://quicklatex.com/ could be used for quick access.
"""


# to weight fractions (w_i)

def at_to_wt(at_fracs: list[float], molar_masses: list[float]) -> list[float]:
    """Converts atomic fractions to weight fractions.
    
        $$w_i = \frac{x_i \cdot M_i}{\sum_{z=1}^{Z} \left( x_z \cdot M_z \right)}$$
    """

    if len(at_fracs) == len(molar_masses):  # same dimensions
        if all(molar_masses):  # no zero molar masses
            
            # calculate (constant) denominator for conversion
            denominator = sum(x_z * M_z for x_z, M_z in zip(at_fracs, molar_masses))

            # convert to weight fraction
            wt_fracs = [(x_i*M_i) / denominator for x_i, M_i in zip(at_fracs, molar_masses)]

            return wt_fracs

        else:
            raise ValueError(f"One of the constituents does not have a molar mass.")

    else:
        raise ValueError(f"Lists of weight fractions and molar masses must have the same length.")

def vol_to_wt(vol_fracs: list[float], densities: list[float]) -> list[float]:
    """Converts volume fractions to weight fractions.
    
        $$w_i = \frac{\phi_i \cdot \rho_i}{\sum_{z=1}^{Z} \left( \phi_z \cdot \rho_z \right)}$$
    """

    if len(vol_fracs) == len(densities):  # same dimensions
        if all(densities):  # no zero densities
            
            # calculate (constant) denominator for conversion
            denominator = sum(phi_z * rho_z for phi_z, rho_z in zip(vol_fracs, densities))

            # convert to weight fraction
            wt_fracs = [(phi_i*rho_i) / denominator for phi_i, rho_i in zip(vol_fracs, densities)]

            return wt_fracs

        else:
            raise ValueError(f"One of the constituents does not have a density.")

    else:
        raise ValueError(f"Lists of weight fractions and molar masses must have the same length.")


# to atomic (mole) fractions (x_i)

def wt_to_at(wt_fracs: list[float], molar_masses: list[float]) -> list[float]:
    """Converts weight fractions to atomic (mole) fractions.
    
        $$x_i = \frac{w_i / M_i}{\sum_{z=1}^{Z} \left( w_z / M_z \right)}$$
    """

    if len(wt_fracs) == len(molar_masses):  # same dimensions
        if all(molar_masses):  # no zero molar masses
            
            # calculate (constant) denominator for conversion
            denominator = sum(w_z / M_z for w_z, M_z in zip(wt_fracs, molar_masses))

            # convert to atomic fraction
            at_fracs = [(w_i/M_i) / denominator for w_i, M_i in zip(wt_fracs, molar_masses)]

            return at_fracs

        else:
            raise ValueError(f"One of the constituents does not have a molar mass.")

    else:
        raise ValueError(f"Lists of weight fractions and molar masses must have the same length.")

def vol_to_at(vol_fracs: list[float], molar_volumes: list[float]) -> float:
    """Converts volume fractions to atomic (mole) fractions.

        $$x_i = \frac{\varphi_i / V_{\mathrm{m},i}}{\sum_{z=1}^{Z} \left( \varphi_z / V_{\mathrm{m},z} \right)}
              = \frac{\varphi_i \cdot \rho_i / M_i}{\sum_{z=1}^{Z} \left( \varphi_z \cdot \rho_z / M_z \right)}$$
    """

    if len(vol_fracs) == len(molar_volumes):  # same dimensions
        if all(molar_volumes):  # no zero molar volumes
            
            # calculate (constant) denominator for conversion
            denominator = sum(phi_z / V_m_z for phi_z, V_m_z in zip(vol_fracs, molar_volumes))

            # convert to atomic fraction
            at_fracs = [(phi_i/V_m_i) / denominator for phi_i, V_m_i in zip(vol_fracs, molar_volumes)]

            return at_fracs

        else:
            raise ValueError(f"One of the constituents does not have a molar volume.")

    else:
        raise ValueError(f"Lists of volume fractions and molar volumes must have the same length.")


# to volume fractions (phi_i)

def wt_to_vol(wt_fracs: list[float], densities: list[float]) -> list[float]:
    """Converts weight fractions to volume fractions.
    
        $$\varphi_i = \frac{w_i / \rho_i}{\sum_{z=1}^{Z} \left( w_z / \rho_z \right)}$$
    """

    if len(wt_fracs) == len(densities):  # same dimensions
        if all(densities):  # no zero densities
            
            # calculate (constant) denominator for conversion
            denominator = sum(w_z / rho_z for w_z, rho_z in zip(wt_fracs, densities))

            # convert to volume fraction
            vol_fracs = [(w_i/rho_i) / denominator for w_i, rho_i in zip(wt_fracs, densities)]

            return vol_fracs

        else:
            raise ValueError(f"One of the constituents does not have a density.")

    else:
        raise ValueError(f"Lists of weight fractions and densities must have the same length.")

def at_to_vol(at_fracs: list[float], molar_volumes: list[float]) -> list[float]:
    """Converts atomic fractions to volume fractions.
    
        $$\varphi_i = \frac{x_i \cdot V_{\mathrm{m},i}}{\sum_{z=1}^{Z} \left( x_z \cdot V_{\mathrm{m},z} \right)}
                    = \frac{x_i \cdot M_i / \rho_i}{\sum_{z=1}^{Z} \left( x_z \cdot M_z / \rho_z \right)}$$
    """

    if len(at_fracs) == len(molar_volumes):  # same dimensions
        if all(molar_volumes):  # no zero molar masses
            
            # calculate (constant) denominator for conversion
            denominator = sum(x_z * V_m_z for x_z, V_m_z in zip(at_fracs, molar_volumes))

            # convert to volume fraction
            wt_fracs = [(x_i*V_m_i) / denominator for x_i, V_m_i in zip(at_fracs, molar_volumes)]

            return wt_fracs

        else:
            raise ValueError(f"One of the constituents does not have a molar volume.")

    else:
        raise ValueError(f"Lists of atomic (mole) fractions and molar volumes must have the same length.")




# parts-per functions

def percent(value: float):
    """Converts value from percent."""
    return value*1e-2
perc = percent # function alias
pc   = percent # function alias

def permille(value: float):
    """Converts value from per mille."""
    return value*1e-3
pm = permille # function alias

def permyriad(value: float):
    """Converts value from per myriad."""
    return value*1e-4
bp = permyriad # function alias

def percentmille(value: float):
    """Converts value from per cent mille."""
    return value*1e-5
pcm = percentmille # function alias

def ppm(value: float):
    """Converts value from parts per million."""
    return value*1e-6

def ppb(value: float):
    """Converts value from parts per billion."""
    return value*1e-9

def ppt(value: float):
    """Converts value from parts per trillion."""
    return value*1e-12

def ppq(value: float):
    """Converts value from parts per quadrillion."""
    return value*1e-15