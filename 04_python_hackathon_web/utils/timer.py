"""
    Decorator to compute the time
    and resource utilized by a program

    Experimental, donot use in production!!    
"""

from time import perf_counter
import resource



def clock_me(func):

    def time_and_space(*args, **kwargs):

        # clock the inital time
        time_start = perf_counter()

        # run the function
        func(*args, **kwargs)

        # find out the time and memory utilized
        time_elapsed = perf_counter() - time_start
        memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0

        print("Utilized: %5.5f secs and %5.5f Mb" %(time_elapsed, memory))
