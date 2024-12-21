from antenna import Antenna
from mesh import ElectoMagneticMesh, Source

import numpy as np

def source_function(t):
    return np.sin(2 * np.pi * t)

antenna = Antenna(0, 0, 0.3, 0.25)
source = Source(0, 0.15, source_function)

mesh = ElectoMagneticMesh(200, 0.0025, 0.0025)

mesh.add_antenna(antenna)
mesh.add_source(source)

mesh.visualize(1000)
