#! python
# %% import
import rivtlib.rvapi as rv

# rv singledoc: True

# %% project description
rv.I("""Project description
     
     Design of embedded pole foundation for the flagpole design example in 
     Appendix A of NAAMM/FP 1001-07,
     "Guide Specifications for Design of Metal Flagpoles"
     Embedded pole foundation design is per 2024 IBC Eq 6-1 and Table 18-I-A.
     Soil properites are per Table 1806.2 in the 2024 IBC
    """)
# %% design input
rv.V("""Design input 
     
     Design input _[T]
     Mbase ==: 24.835*ftkips |ftkips, mkN, 2 | moment at base of flagpole
     P ==: 24.835*kips |kips,kN,2| horizontal load
     b ==: 24*inch |inch, cm, 2 | width of concrete drilled pier
     PFP ==: 200*pcf | pcf, kN_m3, 2| allowable lateral bearing pressure - sandy gravel  
     h ==: 1*ft | ft, m, 2| height
     
     PYTHON | pole_embed.py | rvspace
     
     # P <=: Mbase/(1*ft)
     | PYTHON | pole_embed.py | rvspace
     depth :=: Depth_nonconstrained (P, h, b, PFP, 2) | -ft, -m, 2 | required embed

     ## PYTHON | pole_embed.py | rvspace
     ## depth :=: Depth_nonconstrained (P, h, b, PFP, 2)
     """)
