if 0 <= a < 10:
    do_first()
    do_second()
elif 10 <= a < 20:
    do_the_other_thing()
elif 20 <= a < 50:
    do_first()         # Noncompliant; duplicates first condition
    do_second()
    
    
# if 0 <= a < 10:
#     do_first()
# elif 10 <= a < 20:
#     do_the_other_thing()
# elif 20 <= a < 50:
#     do_first()         # no issue, usually this is done on purpose to increase the readab    
    
if 0 <= a < 10:
    do_first()
elif 20 <= a < 50:
    do_first()         # Noncompliant, this might have been done on purpose but probably not
    
    
    
def doSomething:
  # TODO : Complete function
