set print repeats 0
break code/sanitizer/array_loop.c:6 if i == 6
run
print i
print data
print sizeof data
