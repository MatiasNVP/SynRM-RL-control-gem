# SynRM FOC and Reinforcement Learning Control using Gym Electric Motor

This repository presents a simulation-based control project for a Synchronous Reluctance Machine using Gym Electric Motor.

The first stage implements a Field-Oriented Control baseline with:

- Speed PI controller
- dq current PI controllers
- Simplified MTPA strategy
- dq-to-abc voltage transformation
- Performance metrics for speed and current tracking

The next stage explores Deep Reinforcement Learning controllers for current control and residual control over the FOC baseline.

## Current status

- [x] FOC baseline implemented
- [x] SynRM simulation using Gym Electric Motor
- [x] Basic performance metrics
- [ ] TD3 current-control agent
- [ ] Residual RL over FOC
- [ ] FOC vs DRL benchmark comparison

## Baseline architecture

omega_ref → Speed PI → MTPA → Current PI controllers → dq-to-abc → GEM SynRM environment

## Technologies

- Python
- Gym Electric Motor
- NumPy
- Matplotlib
- Stable-Baselines3
- Jupyter Notebook

## Results

Preliminary FOC results are shown below.

![FOC speed response](results/figures/foc_speed_response.png)

![FOC current tracking](results/figures/foc_current_tracking.png)

