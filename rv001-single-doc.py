#! python
# %% import
import rivtlib.rvapi as rv

# rv singledoc: True
# rv public: False

# %% rv.I("""Load Combinations
rv.I("""Load Combinations 
    ASCE 7-05 Load Effects _[T]
    ============= ================================================
    Equation No.    Load Combination
    ============= ================================================
    16-1           1.4(D+F)
    16-2           1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
    16-3           1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
    ============= ================================================

    | IMAGE | beam1.png | Beam Geometry, 50, num

    Bending Stress _[E]
    
    σ1 = M1 / S1 _[M]
    """)

# %% rv.V("""Loads and Geometry
rv.V("""Loads and Geometry 
    Unit Loads _[T]
    D_1 ==: 3.8*psf | psf, kPA, 2 | joists DL         
    D_2 ==: 2.1*psf | psf, kPA, 2 | plywood DL          
    D_3 ==: 10.0*psf | psf, kPA, 2 | partitions DL       
    D_4 ==: 2*0.5*klf |klf, kN_m, 2 | fixed machinery  DL
    L_1 ==: 40*psf | psf, kPA, 2 | ASCE7-O5 LL 
    
    | VALTABLE | beam1.csv | Beam Geometry, 0:0, num

    Uniform Distributed Loads
    dl_1 <=: 1.2 * (W_1 * (D_1 + D_2 + D_3) + D_4) | klf, kN_m, 2 | dead load : ASCE7-05 2.3.2  _[E]

    ll_1 <=: 1.6 * W_1 * L_1 | klf, kN_m, 2 | live load : ASCE7-05 2.3.2 _[E]
    
    omega_1 <=: dl_1 + ll_1 | klf, kN_m, 2 | total load : ASCE7-05 2.3.2 _[E]
    """)

# %% rv.V("""Beam Stress
rv.V("""Beam Stress
    **Section Properties**

    ## comments have double hashes and will not appear in the docs

    | PYTHON | sectprop.py | nodocstring

    section_1 :=: rectsect(10*inch, 18*inch) | in3, cm3, 2 | function: rect. S _[E]

    inertia_1 :=: rectinertia(10*inch, 18*inch) | in4, cm4, 1 | function: rect. I _[E]

    **Bending Stress**

    m_1 <=: omega_1 * S_1**2 / 8 | ftkips, mkN, 2 | mid-span UDL moment _[E]

    fb_1 <=: m_1 / section_1 | lb_in2, MPA, 1 | bending stress _[E]

    fb_1 < 20000*lb_in2 | ksi, 2, >>> OK, >>> NOT OK | stress ratio _[E]
    """)

# %% rv.D("""Publish Doc
rv.D("""Publish Doc 
    
    _[[METADATA]] 
    [doc]
    authors = rholland
    version = 0.8.1
    repo = https://github.com/rivt-info/rivt-single-doc
    license = https://opensource.org/license/mit/
    fork1_authors = _authors_
    fork1_version = _version_
    fork1_repo = _repo_
    fork1_license = https://opensource.org/license/mit/
    
    ;i[layout]
    logoname = logo.png
    pdf_footer = docname, author1;author2, date, time, version
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in
    pdf_header = totalpages
    pdf_cover = cover.rst
    text_width=80    
    latex_stylesheet = texpdf.sty
    latex_cover = cover.tex
    latex_path = ./latex
    _[[END]]
    
    | PUBLISH | Single Doc Example 1 | pdf
    """)
