# Content outline

## Intro
- Introduction via quantum computing and/or material sciences
- Quantum Computing
- Fermi Hubbard

## Quantum gas microscopy
- History
    - Laser cooling
    - BEC
    - Fermionic gases

- Techniques
    - Laser cooling
    - Optical lattices

- Analog mode

    TH: state of the art, refer to FermiQP
    - Material sciences / applications
    - Hubbard model
    - Phase diagrams
    - Parameter tuning
        - Feshbach resonances
        - Lattice depth


- Digital mode
    
    TH: focus, papers zu collisional gates, double well experiments, Porto (USA), Immanuel&Trozski, Simon Foelling (PhD), Gitter-Atom-Bewegung

    - Motivation for quantum computers
    - Basic principles
        - Qubits
        - Single-qubit operations
        - Two-qubit operations
    - Applications


## Magneto-optical traps

TH: formulas, motivations, maybe calculations (speeds, capture velocities)

- Goal
- History
- Working principles
    - Absorption and emission
        - Atomic phyics basics
        - Zeeman shift
    - Recoil
    - Magnetic field geometry
    - Quantitative estimations (loading rate, duration, cutoff speed)
- Gray molasses cooling (citations, orders of magnitudes)


## Experimental setup of the FermiQP demonstrator

- Goals
    - Quantum gas microscope
        - Analogue mode
        - Digital mode
    - Technical features
        - Compactness
        - low cycle time
        - precision (magnetic fields etc)
        - Raman-MW-RF single qubit gates
        - collisional two-qubit gates with all-to-all connectivity
- Lithium
    - Why lithium
        - Broad Feshbach resonance at 800G
        - large lattice constants possible
    - Drawbacks of lithium
        - lightweight
        - ..?
    - Level structure
        - Cooler and repumper transition
        - smeared-out 3P_3/2 state
- Vacuum chamber
- Cycle overview [short, just ]
    - oven
    - 2D MOT
    - push beam
    - 3D MOT
    - evaporative cooling
    - Raman sideband cooling
    - lattices
    - superlattice
    - UV addressing
    - IR addressing for all-to-all connectivity
    - imaging
- 3D MOT
    - MOT laser system
    - 3D MOT beams
        - maybe RFA discussion
    - magnetic gradients
- Gray molasses cooling (maybe just mention)
- Feshbach field
    - requirements
        - field
        - curvature
        - coil switching
        - parallelogram geometry due to laser beams
    - simulation
        - Magpylib
        - 
    - maybe compensation fields (agree with Janet)


## Conclusion and outlook

- Next steps for the 3D MOT
    - optimization
    - alignment
- Next steps for the Feshbach field
    - Characterisation
    - 
- Next steps for the FermiQP demonstrator
    - Maybe loading directly into lattice from MOT
    - Fast evaporation in dipole trap
    - Implementing other cooling methods
    - Implementing lattices