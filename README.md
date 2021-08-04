# MCORD_AFEHUB

Both builds contains DHCP and Thread supports. 

In build file ` mpconfigboard.h ` has been changed:

- #define MICROPY_PY_THREAD (1)
- #define MICROPY_PY_THREAD_GIL (1)

During build a micropython also `MICROPY_PY_LWIP=1` has been set up. 




[Documentaion](https://afe-documentation.readthedocs.io/en/latest/)





