Here's a funny ASCII diagram.
```
                              ┌────────────────────────────────────────────────────────┐
                              │                     Archive Directory                  │
                              ├─────┬───────┬──────────────┬─────┬─────────────────────┤
                              │┼┼┼┼┼│Archive│┼┼┼┼┼┼┼┼┼┼┼┼┼┼│Vault│┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼│
┌───────────────────┐         ├─────┴────┬──┴─────┬────────┴─────┴─────────────────────┤
│Source Directory A │  Links  │Archive A │┼┼┼┼┼┼┼┼│    (Latest)                        │
├───────────────────┤         ├──────────┴────────┤ ┌─►archive-c-20230306-201312.tar.gz│
│Save.dat◄──────────┼─────────┤Save.dat           │ │  │                               │
│                   │         │                   │ │  ├──Johnny-Hillstart.json        │
│Config.conf◄───────┼─────────┤Config.conf        │ │  │                               │
└───────────────────┘         ├─────────┬─────────┤ │  └──Guy-Manlove.json             │
                              │Archive B│┼┼┼┼┼┼┼┼┼│ │                                  │
┌───────────────────┐         ├─────────┴─────────┤ │  archive-c-20230305-050420.tar.gz│
│Source Directory B │    ┌────┤Saves/             │ │  │                               │
│                   │    │    │  │                │ │  ├──Johnny-Hillstart.json        │
│Saves/◄────────────┼────┘    │  ├──save01.bin    │ │  │                               │
│                   │         │  │                │ │  └──Guy-Manlove.json             │
│Settings.ini◄──────┼────┐    │  └──save02.bin    │ │                                  │
│                   │    │    │                   │ │                                  │
└───────────────────┘    └────┤Settings.ini       │ │                                  │
                              ├───────────────────┤ │                                  │
                              │Archive C          │ │                                  │
┌───────────────────┐         ├───────────────────┤ │                                  │
│Source Directory C │ ┌───────┤Johnny-Hillst..json├─┤                                  │
│                   │ │       │                   │ │                                  │
│Johnny-Hills..json◄├─┘ ┌─────┤Guy-Manlove.json   ├─┘                                  │
│                   │   │     │                   │                                    │
│Guy-Manlove.json◄──┼───┘ ┌───┤Willie-Jabbs.json  │                                    │
│                   │     │   │                   │                                    │
│Willie-Jabbs.json◄─┼─────┘   │                   │                                    │
│                   │         │                   │                                    │
│                   │         │                   │                                    │
└───────────────────┘         │                   │                                    │
                              └───────────────────┴────────────────────────────────────┘
```
