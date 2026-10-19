set pagination off
set confirm off
break code/exercise/polynomial.c:8 if i == 1
run
print i
print value
next
print value
finish
delete breakpoints
continue
quit
