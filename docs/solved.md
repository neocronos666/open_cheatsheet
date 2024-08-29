# Informacion de probelmas resueltos con su solucion

## FLET
### Err
    error while loading shared libraries: libmpv.so.1: cannot open shared object file: No such file or directory
### SOL
    sudo apt update
    sudo apt install libmpv-dev libmpv2
    sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so /usr/lib/libmpv.so.1
