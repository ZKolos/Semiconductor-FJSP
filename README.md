# Semiconductor-FJSP

University project (Budapest University of Technology and Economics, 2026) on scheduling a semiconductor wafer fab,
modelled as a flexible job-shop scheduling problem (FJSP).

Wafers pass through hundreds of process steps and return to the same tool groups
many times, so lots at different stages compete for the same expensive tools.
The project builds a scheduling model and algorithm that assigns and sequences
these operations on a finite set of tools while respecting:

- **Re-entrant flow:** lots revisit the same tool groups at different stages
- **Queue-time (Q-time) limits:** after certain steps, the next step must start within a maximum time window
- **Sequence-dependent setups:** changeover time depends on the previous recipe
- **Metrology sampling and rework:** sampled lots are measured, and out-of-spec results can send them back for rework

Team: Kolos Benedek Zubonyai, Bálint Ábel Tőkey