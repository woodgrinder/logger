* sample Code to illustrate logging.


Note that log once the first basicConfig is done, no other basicConfig calls will work.  You have to use getLogger to set up a logger object, then modify that object with logger methods.
