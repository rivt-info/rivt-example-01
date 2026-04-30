"""

This file has functions to calculate required ground embedment for a pole
resisting a lateral force at a height above the ground. Thr calculation is
based on 2024 IBC Section 1807.3
The are functions for both:
nonconstrained at grade (Eq 18-1) and
constrained at grade (Eq. 18-2)

"""


def test1(x):
    return x


def Depth_nonconstrained(P, h, dia, PFP, tol):
    """Calculate required pole embedment using Eq. 18-1

    Parameters
    ----------
    P : lateral force on pole (lbf)
    h : height above grade of lateral force on pole (ft)
    dia : diameter of post below grade (ft)
    PFP : allowable soil passive equivalent fluid pressure (pcf)
            (see 2024 IBC Table 1806.2 for instance)
    tol : use 2 if 1/2" motion at grade is permissible per 1806.3.4,
            otherwise use 1

    Returns
    -------
    d : calculated embedment depth (ft)

    """
    d = 10
    if tol != 1 and tol != 2:
        print("TOL is incorrect!")
        d = 0
        return d
    b = tol * dia  # effective width of pole in ground
    S1 = PFP * d / 3
    A = 2.34 * P / (S1 * b)
    d_new = 0.5 * A * (1 + (1 + (4.36 * h / A)) ** 0.5)
    while abs(d - d_new) > 0.0010:
        d = d_new
        S1 = PFP * d / 3
        A = 2.34 * P / (S1 * b)
        d_new = 0.5 * A * (1 + (1 + (4.36 * h / A)) ** 0.5)

    print(d)
    return d


def Depth_constrained(P, h, dia, PFP):
    """Calculate required pole embedment using Eq. 18-2

    Parameters
    ----------
    P : lateral force on pole (lbf)
    h : height above grade of lateral force on pole (ft)
    dia : diameter of post below grade (ft)
    PFP : allowable soil passive equivalent fluid pressure (pcf)
            (see 2024 IBC Table 1806.2 for instance)

    Returns
    -------
    d : calculated embedment depth (ft)

    """
    d = 10
    b = dia  # effective width of pole in ground
    S3 = PFP * d
    d_new = ((4.25 * P * h) / (S3 * b)) ** 0.5
    while abs(d - d_new) > 0.0010:
        d = d_new
        S3 = PFP * d
        d_new = ((4.25 * P * h) / (S3 * b)) ** 0.5

    print(d)
    return d


depth = Depth_nonconstrained(696, 4, 1, 1.33 * 400, 2)
# print("nonconstrained depth =","%.2f" %depth , "ft")

depth = Depth_constrained(696, 4, 1, 1.33 * 400)
# print("constrained depth =","%.2f" %depth , "ft")
