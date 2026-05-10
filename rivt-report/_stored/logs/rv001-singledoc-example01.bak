#! python
# %% import
import rivtlib.rvapi as rv

# rv setpublic: false; true flips default header "private" to "public"
# rv setwidth: 80; width of text output, default is 80 characters

# %% rv.I("""Summary
rv.I("""Summary  

    This rivt example calculates the maximum stress and deflection in a simply
    supported, uniformly loaded beam. It also serves as an annotated example of
    a doc with multiple sections that is not part of a report.

    The example illustrates the use of some of the most common API functions,
    commands and tags. Further details are provided in the 
    _[U] rivt user manual, https://www.rivt.info].

    The file may be formatted as a text, PDF or HTML doc by changing the type
    parameter in the PUBLISH command of the *Doc API (rv.D)* at the end of the
    file. Published files are found in the sub-folders of the *_published*
    folder.

    """)

# %% rv.I("""Load Combinations
rv.I("""Load Combinations 

    ## Indented comments with double hashes will not appear in the doc
    ## An inline table contained in a TABLE block is written to a CSV file. 

    _[[TABLE]]  ASCE 7-05 Load Effects (saved as csv in _stored folder)
    ============= ================================================
    Equation No.    Load Combination
    ============= ================================================
    16-1           1.4(D+F)
    16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
    16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
    ============= ================================================
    _[[END]]

    """)

# %% rv.V("""Loads and Geometry
rv.V("""Loads and Geometry 
    
    Successive lines of value definitions are formatted as a table. Variable
    values are defined with the define operator. The line tag [T] labels and
    numbers the table.
    
    Define Unit Loads _[T]
    D_1 ==: 3.8*psf | psf, kPA, 2 | joists DL         
    D_2 ==: 2.1*psf | psf, kPA, 2 | plywood DL          
    D_3 ==: 10.0*psf | psf, kPA, 2 | partitions DL       
    D_4 ==: 2*1.5*klf |klf, kN_m, 2 | fixed machinery DL
    L_1 ==: 40*psf | psf, kPA, 2 | ASCE7-O5 LL
    b_1 ==: 10*inch | inch, mm, 2 | beam width
    h_1 ==: 18*inch | inch, mm, 2 | beam depth
    E_1 ==: 29000*ksi | ksi, MPA, 2 | modulus of elasticity 
    
    The VALTABLE command reads variable values from a file in the src
    folder. The description is used as the table title. The range specifies the
    starting and ending line to be read from the file (0:0 means all lines).

    | VALTABLE | src/beam1.csv | Beam Geometry, 0:0

    ## The IMAGE command inserts an image file with caption, % scale, num;non option 
    | IMAGE | src/beam1.png | Beam Diagram, 60, num

    Uniform Distributed Loads _[C]
    dl_1 <=: 1.2 * (spc_1 * (D_1 + D_2 + D_3) + D_4) | klf, kN_m, 2 | dead load [ASCE7-05 2.3.2]

    ll_1 <=: 1.6 * spc_1 * L_1 | klf, kN_m, 2 | live load [ASCE7-05 2.3.2]
    
    omega_1 <=: dl_1 + ll_1 | klf, kN_m, 2 | total load [ASCE7-05 2.3.2]
    
    """)

# %% rv.V("""Beam Stress
rv.V("""Beam Response

    The following lines import the beam geometry from an external file, 
    calculate section properties from imported functions and calculate 
    the maximum moment, bending stress and mid-span deflection. 

    | PYTHON | src/sectprop.py | Beam functions

    section_1 :=: rectsect(b_1, h_1) | in3, cm3, 2 | rectangle - S

    inertia_1 :=: rectinertia(b_1, h_1) | in4, cm4, 1 | rectangle - I

    
    ##  The line tag [M] formats the equation using utf-8 text.
    σ1 = M1 / S1 _[M]  Maximum Bending Stress 
        
    m_1 <=: omega_1 * spn_1**2 / 8 | ftkips, mkN, 2 | mid-span UDL moment 
    
    fb_1 <=: m_1 / section_1 | psqin, MPA, 1 | bending Stress 

    fb_1 < 20000*psqin | ksi, 2, **OK**, **>> NOT OK** | stress ratio 

    delta_1 :=: midspan_delta(spn_1, omega_1, E_1, inertia_1) | inch, mm, 2 | mid-span deflection

    | IMAGE2 | src/ss-beam2.png, src/ss-beam1.png | Moment Diagram, Deflection Diagram,46,54,num,num

    """)


# %% rv.D("""Publish Doc
rv.D("""Publish Doc 
    
    _[[METADATA]] 
    [doc]
    authors = R Holland
    version = 1.0.0a10
    repo = https://github.com/rivt-info/rivt-single-doc
    license = https://opensource.org/license/mit/
    copyright = -
    fork1_authors = -
    fork1_version = -
    fork1_repo = -
    fork1_license = https://opensource.org/license/mit/
    
    [layout]
    addtype = true
    coverlogo = logo1.png
    runninglogo = logo2.png
    runningtext = rivt
    subtitle =  -
    copyright = -
    client = user example
    projectnum = 0001
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    pdf_link_underline = true
    _[[END]]
    
    The rivt file may be published as a text, PDF or HTML doc by changing the
    type parameter to text, pdf or html. A README.txt file is always written to
    the rivt and _rivt-public folders. Published files are found in sub-folders
    of the _published folder.

    | PUBLISH | Example 1 - rivt Doc | pdf
    """)
