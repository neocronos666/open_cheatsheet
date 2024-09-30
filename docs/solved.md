# :bug: Errors found and how were corrected

## FLET

### Error
    error while loading shared libraries: libmpv.so.1: cannot open shared object file: No such file or directory
### SSolution
    sudo apt update
    sudo apt install libmpv-dev libmpv2
    sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so /usr/lib/libmpv.so.1
---
