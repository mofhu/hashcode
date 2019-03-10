# optimize outline

1. add shuffle function in small-scale search
    * baseline: 2, 14745, 875, 261334, 117179 = 394135
    * new baseline: 2, 8163, 1356, 397736, 325052 = 732309
2. optimize search size using a threshold
    * find cluster base by statistics
    * threshold cutoff for code
    * new baseline: 2, 96465, 1384, 408188, 364330 = 870369

Target 20190310
    * for case B, max ~ 240000
    * for case C, max ~ 1500
    * for case D, max ~ 480000
    * for case E, max ~ 560000

3. search in memory
    * optimize case B
    * should be able to index files by tag and search
    * reuse tag dict: 800000 tags, should hold in memory
4. optimize cluster (pending)

