# 3D Magneto-optical Trap

## Theory
### History
- Laser cooling (Haensch, Phillips & Metcals)
- Optical Earnshaw theorem
- Internal degrees of freedom
- First implementation, first lithium implementations (1993)

### Atom-Light Interaction
- Two-level system
- Scattering
- Photon Recoil, Spontaneous emission and Doppler limit

### MOT theory
- geometry
- magnetic gradients
- capture velocities: Tiecke (HO model, referencing Metcalf v.d. Straaten)

### Magneto-optical traps with Lithium
- peculiarities
    - unresolved manifold
- Kawanaka 1993, Schunemann 1998, Tiecke 2009
- Lithium
- some other experiments and their data

### Grey molasses cooling
- theory
    - spatially varying polarization
    - light states experience spatially varying energy shift
- laser requirements (Burchianti)

## 3D MOT for FermiQP
### 3D MOT geometry
- glass cell
- tight layout (objectives, glass cell geometry)
- shallow angles

### Optical setup
- laser requirements
    - cooler & repumper
    - powers
- laser setup
    - lasers
        - RFAs (specs and problems, ref to Janet's thesis)
        - seeds
        - locking scheme (cavity, offset locks to freely shift MOT board)
    - outline of complete setup
        - D2 and D1 light
        - 2D MOT and 3D MOT
        - generation of cooler and repumper
        - possibility to add EOM in order to address more velocity classes
    - 2D MOT setup ("first part of setup")
        - isolator (model, specs, characterisation)
        - telescope and focusing (lenses, factor of resizing, beam profile)
        - AOM (shift, aperture, driver to be replaced with centrally steered VCO)
        - free space for EOM
        - to lock
        - to push beam
        - cooler and repumper
            - AOMs (shift, aperture, driver to be replaced with centrally steered VCO)
            - overlapping (graph from beam profiler?)
            - coupling into fibers
        - relative powers

- outcoupler optics
    - overview drawing of the MOT beams (inventor)
    - planning schematics
    - change of optical power (polarization and absorption) -> focussing of beam (Gaussian beam simulation)
    - polarization requirements
    - mirror and glass cell surface characterization
    - polarization fixations
        - first pass through glass cell: fixing such that right / left after single pass through glass window, note down polarizations at other positions
        - second pass: send light in through cube and lambda/4 to get right/left polarization, pass it through a mock setup of the system and note down the polarization after the waveplates as a reference
    
### Magnetic gradients
- short characterization of the simulation results

### Parameter estimations
- size
- capture velocity estimation
- density / atom number?
