from math import fabs, floor, atan2

'''
double
round(double x)
{
    double absx, y;
    absx = fabs(x);
    y = floor(absx);
    if (absx - y >= 0.5)
        y += 1.0;
    return copysign(y, x);
}

double
copysign(double x, double y)
{
    /* use atan2 to distinguish -0. from 0. */
    if (y > 0. || (y == 0. && atan2(y, -1.) > 0.)) {
        return fabs(x);
    } else {
        return -fabs(x);
    }
}
'''


def copysign(x: float, y: float) -> float:
    if (y > 0. or (y == 0. and atan2(y, -1) > 0.)):
        return fabs(x)
    else:
        return -fabs(x)


def custom_round(x: float) -> float:
    absx = fabs(x)
    y = floor(absx)
    if (absx - y >= 0.5):
        y += 1.0
    return copysign(y, x)
