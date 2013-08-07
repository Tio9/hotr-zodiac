hotr-zodiac
===========

pypy scripts for optimizing your Heroes of the Realm zodiac order


Requires PyPy version 2.1

zodiac_opy.py 

Edit this file to add your list of 10 zodaics in 3-letter form at the very bottom, inside the main([])
then run it in pypy, w/ this command line: pypy zodiac_opt.py

If you enter fewer than 10 zodaics, it will do a single run for every combination of possible fill-ins to get to 10.
Caution: the fewer you enter, the more runs will take place (10 ^ # of missing).
