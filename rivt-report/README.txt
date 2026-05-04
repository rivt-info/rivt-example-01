
[ 1i ] Summary
--------------------------------------------------------------------------------
 
This rivt example calculates the maximum stress and deflection in a simply
This rivt example calculates the maximum stress and deflection in a simply
supported, uniformly loaded beam. It also serves as an annotated example of
supported, uniformly loaded beam. It also serves as an annotated example of
a single doc with multiple sections (a single doc does not use the
a single doc with multiple sections (a single doc does not use the
report generating script).
report generating script).
 
The example illustrates the use of some of the most common API functions,
The example illustrates the use of some of the most common API functions,
commands and tags. Further details are provided in the 
commands and tags. Further details are provided in the 
 rivt user manual, https://www.rivt.info .
 rivt user manual, https://www.rivt.info .
 
The file may be formatted as a text, PDF or HTML doc by changing the type
The file may be formatted as a text, PDF or HTML doc by changing the type
parameter in the PUBLISH command of the Doc API (rv.D) at the end
parameter in the PUBLISH command of the Doc API (rv.D) at the end
of the file. Published files are found in the respective sub-folders of the
of the file. Published files are found in the respective sub-folders of the
_published folder.
_published folder.
 
 

[ 2i ] Load Combinations
--------------------------------------------------------------------------------
 
This is an inline table using the restructured text syntax. 
This is an inline table using the restructured text syntax. 
 
 

Table 1: ASCE 7-05 Load Effects

Table 1: ASCE 7-05 Load Effects
============= ================================================
============= ================================================
Equation No.    Load Combination
Equation No.    Load Combination
============= ================================================
============= ================================================
16-1           1.4(D+F)
16-1           1.4(D+F)
16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
============= ================================================
============= ================================================
 
When an inline table is contained in a TABLE block it produces the same
When an inline table is contained in a TABLE block it produces the same
output as above and also writes the table to a CSV file.
output as above and also writes the table to a CSV file.
 
Table 2: ASCE 7-05 Load Effects (saved as csv in _storeed folder)
============= ================================================ 
Equation No.    Load Combination 
============= ================================================ 
16-1           1.4(D+F) 
16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R) 
16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W) 
============= ================================================ 

Table 2: ASCE 7-05 Load Effects (saved as csv in _storeed folder)
============= ================================================ 
Equation No.    Load Combination 
============= ================================================ 
16-1           1.4(D+F) 
16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R) 
16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W) 
============= ================================================ 

 
 

Fig. 1 - Beam Geometry  [file: beam1.png ] 


 Image: Fig. 1 - Beam Geometry 

 
 
Maximum Bending Stress 
Maximum Bending Stress 
 
┌  Eq-1
│
│          M₁
│     σ₁ = ──
│          S₁
└


┌  Eq-1
│
│          M₁
│     σ₁ = ──
│          S₁
└


 
 

[ 3v ] Loads and Geometry
--------------------------------------------------------------------------------
 
Successive lines of value definiiions are formatted as a table. Variable
Successive lines of value definiiions are formatted as a table. Variable
values are defined with the define operator. The line tag [T] labels and
values are defined with the define operator. The line tag [T] labels and
numbers the table.
numbers the table.
 

Table 3: Define Unit Loads

Table 3: Define Unit Loads
==========  =========  ==========  ===================
variable        value     [value]  description
==========  =========  ==========  ===================
D_1          3.80 psf    0.18 kPA  joists DL
D_2          2.10 psf    0.10 kPA  plywood DL
D_3         10.00 psf    0.48 kPA  partitions DL
D_4          3.00 klf  43.78 kN_m  fixed machinery  DL
L_1         40.00 psf    1.92 kPA  ASCE7-O5 LL
==========  =========  ==========  =================== 
 
The VALTABLE command reads variable values from the file in the _src
The VALTABLE command reads variable values from the file in the _src
folder. The text is used as the table title. The range specifies the
folder. The text is used as the table title. The range specifies the
starting and ending line to be read from the file (0:0 means all lines).
starting and ending line to be read from the file (0:0 means all lines).
The num;non parameter specifies whether theimported table is numbered.
The num;non parameter specifies whether theimported table is numbered.
 

Table 4: Beam Geometry [file: beam1.csv]

==========  ========  =========  =============
variable       value    [value]  description
==========  ========  =========  =============
spc_1        2.00 ft     0.61 m  beam spacing
spn_1       16.00 ft     4.88 m  beam span
==========  ========  =========  =============


**Table 4**: Beam Geometry [file: beam1.csv]

==========  ========  =========  =============
variable       value    [value]  description
==========  ========  =========  =============
spc_1        2.00 ft     0.61 m  beam spacing
spn_1       16.00 ft     4.88 m  beam span
==========  ========  =========  =============

 
Uniform Distributed Loads

Uniform Distributed Loads

┌  Eq-2
│
│     dl_1 = 1.2*(D_4 + spc_1*(D_1 + D_2 + D_3))
└

=========  ========  ========  ========  =======
   D_3       D_2       D_4       D_1      spc_1
=========  ========  ========  ========  =======
10.00 psf  2.10 psf  3.00 klf  3.80 psf  2.00 ft
=========  ========  ========  ========  =======

========  ==========  =========================
 dl_1      [dl_1 ]            reference
========  ==========  =========================
3.64 klf  53.09 kN_m  dead load: ASCE7-05 2.3.2
========  ==========  =========================
┌  Eq-2
│
│     dl_1 = 1.2*(D_4 + spc_1*(D_1 + D_2 + D_3))
└

=========  ========  ========  ========  =======
   D_3       D_2       D_4       D_1      spc_1
=========  ========  ========  ========  =======
10.00 psf  2.10 psf  3.00 klf  3.80 psf  2.00 ft
=========  ========  ========  ========  =======

========  ==========  =========================
 dl_1      [dl_1 ]            reference
========  ==========  =========================
3.64 klf  53.09 kN_m  dead load: ASCE7-05 2.3.2
========  ==========  =========================
 
┌  Eq-3
│
│     ll_1 = 1.6*L_1*spc_1
└

=========  =======
   L_1      spc_1
=========  =======
40.00 psf  2.00 ft
=========  =======

========  =========  =========================
 ll_1      [ll_1 ]           reference
========  =========  =========================
0.13 klf  1.87 kN_m  live load: ASCE7-05 2.3.2
========  =========  =========================
┌  Eq-3
│
│     ll_1 = 1.6*L_1*spc_1
└

=========  =======
   L_1      spc_1
=========  =======
40.00 psf  2.00 ft
=========  =======

========  =========  =========================
 ll_1      [ll_1 ]           reference
========  =========  =========================
0.13 klf  1.87 kN_m  live load: ASCE7-05 2.3.2
========  =========  =========================
 
┌  Eq-4
│
│     omega_1 = dl_1 + ll_1
└

========  =============
  dl_1        ll_1
========  =============
3.64 klf  128.00 ft·psf
========  =============

==========  ============  ==========================
 omega_1     [omega_1 ]           reference
==========  ============  ==========================
 3.77 klf    54.96 kN_m   total load: ASCE7-05 2.3.2
==========  ============  ==========================
┌  Eq-4
│
│     omega_1 = dl_1 + ll_1
└

========  =============
  dl_1        ll_1
========  =============
3.64 klf  128.00 ft·psf
========  =============

==========  ============  ==========================
 omega_1     [omega_1 ]           reference
==========  ============  ==========================
 3.77 klf    54.96 kN_m   total load: ASCE7-05 2.3.2
==========  ============  ==========================
 
 

[ 4v ] Beam Response
--------------------------------------------------------------------------------
 
 

Function Table 5: Beam functions    [file: _src/sectprop.py ]

==========================  =====================================================
Function                    Docstring
==========================  =====================================================
rectsect(b, d)              section modulus of rectangle
rectinertia(b, d)           moment of inertia of rectangle
midspan_delta(ln, w, e, i)  mid-span deflection of simply supported beam with UDL
==========================  =====================================================


**Function Table 5**: Beam functions   **[file:** _src/sectprop.py **]**

==========================  =====================================================
Function                    Docstring
==========================  =====================================================
rectsect(b, d)              section modulus of rectangle
rectinertia(b, d)           moment of inertia of rectangle
midspan_delta(ln, w, e, i)  mid-span deflection of simply supported beam with UDL
==========================  =====================================================

 
┌  Eq-5
│
│     section_1 = rectsect(10*inch, 18*inch)
└


============  ==============
 section_1     [section_1 ]
============  ==============
 540.00 in3    8849.01 cm3
============  ==============

┌  Eq-5
│
│     section_1 = rectsect(10*inch, 18*inch)
└


============  ==============
 section_1     [section_1 ]
============  ==============
 540.00 in3    8849.01 cm3
============  ==============

 
┌  Eq-6
│
│     inertia_1 = rectinertia(10*inch, 18*inch)
└


============  ==============
 inertia_1     [inertia_1 ]
============  ==============
 4860.0 in4    202288.5 cm4
============  ==============

┌  Eq-6
│
│     inertia_1 = rectinertia(10*inch, 18*inch)
└


============  ==============
 inertia_1     [inertia_1 ]
============  ==============
 4860.0 in4    202288.5 cm4
============  ==============

 
Bending Stress

Bending Stress

 
┌  Eq-7
│
│                        2
│           omega_1*spn_1 
│     m_1 = --------------
│                 8       
└

=========  ========
 omega_1    spn_1
=========  ========
3.77 klf   16.00 ft
=========  ========

============  ==========  ===================
    m_1         [m_1 ]         reference
============  ==========  ===================
120.52 ftkip  163.40 mkN  mid-span UDL moment
============  ==========  ===================
┌  Eq-7
│
│                        2
│           omega_1*spn_1 
│     m_1 = --------------
│                 8       
└

=========  ========
 omega_1    spn_1
=========  ========
3.77 klf   16.00 ft
=========  ========

============  ==========  ===================
    m_1         [m_1 ]         reference
============  ==========  ===================
120.52 ftkip  163.40 mkN  mid-span UDL moment
============  ==========  ===================
 
┌  Eq-8
│
│               m_1   
│     fb_1 = ---------
│            section_1
└

===========  =============
 section_1        m_1
===========  =============
540.0 inch3  120.5 ft2·klf
===========  =============

=============  =========  ==============
    fb_1        [fb_1 ]     reference
=============  =========  ==============
2678.2 lb_in2  18.5 MPA   bending stress
=============  =========  ==============
┌  Eq-8
│
│               m_1   
│     fb_1 = ---------
│            section_1
└

===========  =============
 section_1        m_1
===========  =============
540.0 inch3  120.5 ft2·klf
===========  =============

=============  =========  ==============
    fb_1        [fb_1 ]     reference
=============  =========  ==============
2678.2 lb_in2  18.5 MPA   bending stress
=============  =========  ==============
 
┌  Eq-9
│
│     fb_1 < 20000*lb_in2
└

========  ===============  ========  =======  ============
  fb_1     20000*lb_in2     ratio     check    reference
========  ===============  ========  =======  ============
2.68 ksi     20.00 ksi     0.133908    OK     stress ratio
========  ===============  ========  =======  ============

┌  Eq-9
│
│     fb_1 < 20000*lb_in2
└

========  ===============  ========  =======  ============
  fb_1     20000*lb_in2     ratio     check    reference
========  ===============  ========  =======  ============
2.68 ksi     20.00 ksi     0.133908    OK     stress ratio
========  ===============  ========  =======  ============

 
Deflection

Deflection

 
┌  Eq-10
│
│     delta_1 = midspan_delta(spn_1, omega_1, 29000*ksi, inertia_1)
└


==========  ============
 delta_1     [delta_1 ]
==========  ============
0.04 inch     1.00 mm
==========  ============

┌  Eq-10
│
│     delta_1 = midspan_delta(spn_1, omega_1, 29000*ksi, inertia_1)
└


==========  ============
 delta_1     [delta_1 ]
==========  ============
0.04 inch     1.00 mm
==========  ============

 
 
