# Source from Bash to use this machine's tools in the original workspace.
local_debug_tools=/data/liuwenjie/Myfile/CS100/slides/r4/build/tools
export PATH="$local_debug_tools/bin:$PATH"
export LIBRARY_PATH="$local_debug_tools/usr/lib64${LIBRARY_PATH:+:$LIBRARY_PATH}"
export LD_LIBRARY_PATH="$local_debug_tools/usr/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
unset local_debug_tools
