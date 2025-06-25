import numpy as np

def transport(loc, vel, dt):
    """transport equations
    Args:
         loc: initial location (can be int/float or array)
         vel: velocity (can be int/float or array)
         dt: time step

    Returns:
        location after one time step
     """

    # if loc, vel are simple numbers
    if isinstance(loc, (int, float)) and isinstance(vel, (int, float)):
        loc = loc + vel * dt

    # Added block for -> test_transport_4
    # if loc or vel is list, we want to convert to numpy arrays
    if type(loc) is list:
        loc = np.array(loc)
    if type(vel) is list:
        vel = np.array(vel)

    if isinstance(loc, np.ndarray) and isinstance(vel, np.ndarray):
        # vel = vel.astype(np.float32, copy=False)
        
        # fixing for xfail "doesn't work for arrays with dtype=int"
        vel = vel.astype(dtype=np.float32, copy=False)
        loc = loc.astype(dtype=np.float32, copy=False)

        vel = vel.astype(np.float32, copy=False)
        loc[:] = loc[:] + vel[:] *dt
    return loc