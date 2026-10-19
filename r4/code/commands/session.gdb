set pagination off
set confirm off
break updateMaximum if value == 8
run < code/input/sum-max.txt
next
print value
print result
bt
frame 1
print x
print sum
frame 0
watch result
next
next
print result
delete breakpoints
continue
quit
