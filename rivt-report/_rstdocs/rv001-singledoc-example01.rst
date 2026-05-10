.. |s| unicode:: 0xA0 



.. |blklogo| image:: ../src/logo2.png
   :height: 100px
   :alt: logo



.. header::
    .. list-table::
        :class: header-box
        :align: left
        :widths: 90 10
        
        * - **Example 1 - rivt Doc** - v1.0.0a10 |s| |s| |s| Sect: **###Section###**
          - p. **###Page###**   

          

.. footer:: 
    .. list-table::
        :class: footer-box
        :align: left
        :widths: 84 22 16
        
        * - 2026-05-10 |s| |s| |s| **|** |s| |s| |s| R Holland        
          - **rivt**        
          - |blklogo|

                  


**1i.** **Summary**
--------------------------------------------------------------------------------
 
This rivt example calculates the maximum stress and deflection in a simply
supported, uniformly loaded beam. It also serves as an annotated example of
a doc with multiple sections that is not part of a report.
 
The example illustrates the use of some of the most common API functions,
commands and tags. Further details are provided in the 
`rivt user manual <https://www.rivt.info>`_.
 
The file may be formatted as a text, PDF or HTML doc by changing the type
parameter in the PUBLISH command of the Doc API (rv.D) at the end of the
file. Published files are found in the sub-folders of the _published
folder.
 
 



------------

**2i.** **Load Combinations**
--------------------------------------------------------------------------------
 
 

|

**Table 1**: ASCE 7-05 Load Effects (saved as csv in _stored folder) 

============= ================================================ 
Equation No.    Load Combination 
============= ================================================ 
16-1           1.4(D+F) 
16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R) 
16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W) 
============= ================================================ 

 
 



------------

**3v.** **Loads and Geometry**
--------------------------------------------------------------------------------
 
Successive lines of value definitions are formatted as a table. Variable
values are defined with the define operator. The line tag [T] labels and
numbers the table.
 

**Table 2**: Define Unit Loads

==========  ============  =============  =====================
variable    value         [value]        description
==========  ============  =============  =====================
D_1         3.80 psf      0.18 kPA       joists DL
D_2         2.10 psf      0.10 kPA       plywood DL
D_3         10.00 psf     0.48 kPA       partitions DL
D_4         3.00 klf      43.78 kN_m     fixed machinery  DL
L_1         40.00 psf     1.92 kPA       ASCE7-O5 LL
b_1         10.00 inch    254.00 mm      beam width
h_1         18.00 inch    457.20 mm      beam depth
E_1         29000.00 ksi  199947.96 MPA  modulus of elasticity
==========  ============  =============  =====================
 
The VALTABLE command reads variable values from a file in the src
folder. The description is used as the table title. The range specifies the
starting and ending line to be read from the file (0:0 means all lines).
 
|

**Table 3**: Beam Geometry from file: **src/beam1.csv**

==========  ========  =========  =============
variable    value     [value]    description
==========  ========  =========  =============
spc_1       2.00 ft   0.61 m     beam spacing
spn_1       16.00 ft  4.88 m     beam span
==========  ========  =========  =============


 

.. figure:: c:/git/rivt-example-01-git/rivt-report/src/beam1.png
    :width: 60%
    :align: center

    **Fig. 1** - Beam Diagram 
    

 
**Uniform Distributed Loads**



|
|

**Eq. 1:**  dead load, ASCE7-05 2.3.2

.. code-block:: text 

           dl₁ = 1.2⋅(D₄ + spc₁⋅(D₁ + D₂ + D₃))

           dl₁ = 3.64 klf     [dl₁] = 53.09 kN_m    |   dead load, ASCE7-05 2.3.2

============  ==========  ===================  =============  =========
spc₁          D₂          D₄                   D₃             D₁
============  ==========  ===================  =============  =========
2.00 ft       2.10 psf    3.00 klf             10.00 psf      3.80 psf
beam spacing  plywood DL  fixed machinery  DL  partitions DL  joists DL
============  ==========  ===================  =============  =========
 


|
|

**Eq. 2:**  live load: ASCE7-05 2.3.2

.. code-block:: text 

           ll₁ = 1.6⋅L₁⋅spc₁

           ll₁ = 0.13 klf     [ll₁] = 1.87 kN_m    |   live load: ASCE7-05 2.3.2

============  ===========
spc₁          L₁
============  ===========
2.00 ft       40.00 psf
beam spacing  ASCE7-O5 LL
============  ===========
 


|
|

**Eq. 3:**  total load: ASCE7-05 2.3.2

.. code-block:: text 

           ω₁ = dl₁ + ll₁

           ω₁ = 3.77 klf     [ω₁] = 54.96 kN_m    |   total load: ASCE7-05 2.3.2

=========================  =========================
dl₁                        ll₁
=========================  =========================
3.64 klf                   128.00 ft·psf
dead load, ASCE7-05 2.3.2  live load: ASCE7-05 2.3.2
=========================  =========================
 
 



------------

**4v.** **Beam Response**
--------------------------------------------------------------------------------
 
The following lines import the beam geometry from an external file, 
calculate section properties from imported functions and calculate 
the maximum moment, bending stress and mid-span deflection. 
 

**Table 4**: Beam functions from file: **src/sectprop.py**


==========================  =====================================================
Function                    Docstring
==========================  =====================================================
rectsect(b, d)              section modulus of rectangle
rectinertia(b, d)           moment of inertia of rectangle
midspan_delta(ln, w, e, i)  mid-span deflection of simply supported beam with UDL
==========================  =====================================================

 
|

**Eq. 4:**  rectangle - S

.. code-block:: text 

           section₁ = rectsect(b₁, h₁)


==========  ==========
   h_1         b_1
==========  ==========
18.00 inch  10.00 inch
==========  ==========

.. class:: table-no-split

===========================  ==========================  =============
**section_1  = 540.00 in3**  [section_1 ] = 8849.01 cm3  rectangle - S
===========================  ==========================  =============

 
|

**Eq. 5:**  rectangle - I

.. code-block:: text 

           inertia₁ = rectinertia(b₁, h₁)


=========  =========
   h_1        b_1
=========  =========
18.0 inch  10.0 inch
=========  =========

.. class:: table-no-split

===========================  ===========================  =============
**inertia_1  = 4860.0 in4**  [inertia_1 ] = 202288.5 cm4  rectangle - I
===========================  ===========================  =============

 
 

|


**Eq.6**

.. code-block:: text 

                M₁
           σ₁ = ──
                S₁




 


|
|

**Eq. 7:**  mid-span UDL moment

.. code-block:: text 

                       2
                ω₁⋅spn₁ 
           m₁ = ────────
                   8    

           m₁ = 120.52 ftkip     [m₁] = 163.40 mkN    |   mid-span UDL moment

==========================  =========
ω₁                          spn₁
==========================  =========
3.77 klf                    16.00 ft
total load: ASCE7-05 2.3.2  beam span
==========================  =========
 


|
|

**Eq. 8:**  bending Stress

.. code-block:: text 

                    m₁   
           fb₁ = ────────
                 section₁

           fb₁ = 2678.2 lb_in2     [fb₁] = 18.5 MPA    |   bending Stress

===================  =============
m₁                   section₁
===================  =============
120.5 ft2·klf        540.0 inch3
mid-span UDL moment  rectangle - S
===================  =============
 
|

**Eq.9:** stress ratio

.. code-block:: text 

               fb₁ < 20000⋅psqin


========  ==============  ========  =======  ============
  fb_1     20000*psqin     ratio     check    reference
========  ==============  ========  =======  ============
2.68 ksi    20.00 ksi     0.133908  **OK**   stress ratio
========  ==============  ========  =======  ============

 
|

**Eq. 10:**  mid-span deflection

.. code-block:: text 

           δ₁ = midspan_δ(spn₁, ω₁, E₁, inertia₁)


=========  ============  =============  ========
 omega_1       E_1         inertia_1     spn_1
=========  ============  =============  ========
3.77 klf   29000.00 ksi  4860.00 inch4  16.00 ft
=========  ============  =============  ========

.. class:: table-no-split

========================  ====================  ===================
**delta_1  = 0.04 inch**  [delta_1 ] = 1.00 mm  mid-span deflection
========================  ====================  ===================

 

.. list-table::
    :widths: 46 54
    :header-rows: 0

    * - .. figure:: c:/git/rivt-example-01-git/rivt-report/src/ss-beam2.png
            :width: 100%

            **Fig. 2 -** Moment Diagram 
     
      - .. figure:: c:/git/rivt-example-01-git/rivt-report/src/ss-beam1.png
            :width: 100%
            
            **Fig. 3 -** Deflection Diagram 
                     

 
 
