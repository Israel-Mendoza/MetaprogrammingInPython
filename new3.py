"""
Why would we want to override the __new__ method?
Why not use __new__ to initialize the instance all the time then?
"""

# Sometimes, we may actually want to tweak some of the instantiation process.
# We could definitely use the __new__ method to initialize the instance
# without having to use the __init__ method, but then we would have to take
# care of the instance creation all the time.
