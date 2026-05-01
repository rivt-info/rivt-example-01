
[ 1i ] Summary
--------------------------------------------------------------------------------
 
This rivt example calculates the maximum stress and deflection in a simply
supported, uniformly loaded beam. It also serves as an annotated example of
a single doc with multiple sections (a single doc does not use the
report generating script).
 
The example illustrates the use of some of the most common API functions,
commands and tags. Further details are provided in the [U] rivt user manual,
https://www.rivt.info|.
 
The file may be formatted as a text, PDF or HTML doc by changing the type
parameter in the PUBLISH command of the Doc API (rv.D) at the end
of the file. Published files are found in the respective sub-folders of the
_published folder.
 
 

[ 2i ] Load Combinations
--------------------------------------------------------------------------------
 
This is an inline table using the restructured text syntax. 
 
 

**Table 1**: ASCE 7-05 Load Effects 

============= ================================================
Equation No.    Load Combination
============= ================================================
16-1           1.4(D+F)
16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
============= ================================================
 
When an inline table is in a [[TABLE]] block it produces the same output
as above, and also writes the table to a CSV file in the _stored folder.
 
**Table 2**: ASCE 7-05 Load Effects (saved as csv)

============= ================================================ 
Equation No.    Load Combination 
============= ================================================ 
16-1           1.4(D+F) 
16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R) 
16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W) 
============= ================================================ 

 
 


.. image:: c:/git/rivt-example-01-git/rivt-report/_src/beam1.png
   :width: 50%
   :align: center


.. raw:: html 

   <p align="center">Fig. 1 - Beam Geometry 

 
 
Maximum Bending Stress 
 

.. code:: 

          M₁
     σ₁ = ──
          S₁


 
 
 

[ 3v ] Loads and Geometry
--------------------------------------------------------------------------------
 
Successive lines of value definiiions are formatted as a table. Variable
values are defined with the define operator. The line tag [T] labels and
numbers the table.
 

**Table 3**: Define Unit Loads 

==========  =========  ==========  ===================
variable        value     [value]  description
==========  =========  ==========  ===================
D_1          3.80 psf    0.18 kPA  joists DL
D_2          2.10 psf    0.10 kPA  plywood DL
D_3         10.00 psf    0.48 kPA  partitions DL
D_4          1.00 klf  14.59 kN_m  fixed machinery  DL
L_1         40.00 psf    1.92 kPA  ASCE7-O5 LL
==========  =========  ==========  =================== 
 
The VALTABLE command reads variable values from the file in the _src
folder. The text is used as the table title. The range specifies the
starting and ending line to be read from the file (0:0 means all lines).
The *num;non* parameter specifies whether theimported table is numbered.
 

**Table 4**: Beam Geometry [file: beam1.csv]

==========  ========  =========  =============
variable       value    [value]  description
==========  ========  =========  =============
W_1          2.00 ft     0.61 m  beam spacing
S_1         14.00 ft     4.27 m  beam span
==========  ========  =========  =============

 
Uniform Distributed Loads 

.. code-block:: text 

   Eq.9
           dl_1 = 1.2*(D_4 + W_1*(D_1 + D_2 + D_3))


========  ==========  =========================
 dl_1      [dl_1 ]            reference
========  ==========  =========================
1.24 klf  18.07 kN_m  dead load: ASCE7-05 2.3.2
========  ==========  =========================

========  =========  ========  =======  =====
  D_1        D_3       D_2       W_1     D_4
========  =========  ========  =======  =====
3.80 psf  10.00 psf  2.10 psf  2.00 ft   klf
========  =========  ========  =======  =====
 

.. code-block:: text 

   Eq.10
           ll_1 = 1.6*L_1*W_1


========  =========  =========================
 ll_1      [ll_1 ]           reference
========  =========  =========================
0.13 klf  1.87 kN_m  live load: ASCE7-05 2.3.2
========  =========  =========================

=======  =========
  W_1       L_1
=======  =========
2.00 ft  40.00 psf
=======  =========
 

.. code-block:: text 

   Eq.11
           omega_1 = dl_1 + ll_1


==========  ============  ==========================
 omega_1     [omega_1 ]           reference
==========  ============  ==========================
 1.37 klf    19.94 kN_m   total load: ASCE7-05 2.3.2
==========  ============  ==========================

=============  ========
    ll_1         dl_1
=============  ========
128.00 ft·psf  1.24 klf
=============  ========
 
 

[ 4v ] Beam Stress
--------------------------------------------------------------------------------
 
Section Properties
 
**[ Python file read:** _src/sectprop.py **]**



 
    section_1 = rectsect(10*inch, 18*inch)

============  ==============
 section_1     [section_1 ]
============  ==============
 540.00 in3    8849.01 cm3
============  ==============

 
    inertia_1 = rectinertia(10*inch, 18*inch)

============  ==============
 inertia_1     [inertia_1 ]
============  ==============
 4860.0 in4    202288.5 cm4
============  ==============

 
Bending Stress
 

.. code-block:: text 

   Eq.15
                    2        
                 S_1 *omega_1
           m_1 = ------------
                      8      


===========  =========  ===================
   m_1        [m_1 ]         reference
===========  =========  ===================
33.47 ftkip  45.38 mkN  mid-span UDL moment
===========  =========  ===================

=========  ========
 omega_1     S_1
=========  ========
1.37 klf   14.00 ft
=========  ========
 

.. code-block:: text 

   Eq.16
                     m_1   
           fb_1 = ---------
                  section_1


============  =========  ==============
   fb_1        [fb_1 ]     reference
============  =========  ==============
743.8 lb_in2   5.1 MPA   bending stress
============  =========  ==============

===========  ============
 section_1       m_1
===========  ============
540.0 inch3  33.5 ft2·klf
===========  ============
 

fb_1 < 20000*lb_in2 | ksi, 2, >>> OK, >>> NOT OK | stress ratio 
 

[ 5v ] Beam deflection
--------------------------------------------------------------------------------
 
text 123
 
 

end of doc
