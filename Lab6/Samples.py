def defaultSamples(x, errors):
    assert(len(x) == len(errors))
    return 2.0 + 2.0 * x + errors


def disturbedSamples(x, errors):
    assert(len(x) == len(errors))
    y = 2.0 + 2.0 * x + errors
    y[0] += 10.0
    y[len(y) - 1] -= 10.0
    return y
