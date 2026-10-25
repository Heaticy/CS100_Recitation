mkdir -p build/demo
cc -std=c17 -O0 -g code/bss.c -o build/demo/bss
cc -std=c17 -O0 -g code/data.c -o build/demo/data
size build/demo/bss build/demo/data
objdump -t build/demo/bss | grep ' array$'
objdump -t build/demo/data | grep ' array$'
