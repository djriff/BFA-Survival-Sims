# BfA Survival Hunter Sims

This repo includes scripts and sims for survival hunters.

## Documentation
All documentation can be found in the [Wiki](https://github.com/djriff/bfa-survival-sims/wiki).

## Discussion
- [Discord](https://discord.gg/ZpRNX6)

## How to Run

1. Each directory has a list of reports in `reports.py` that you want to sim.
2. Create `reports/` and `profiles/` directories within the directory you want to sim.
3. After creating reports, run `python profiles.py [DA, LotV]` in the given directory you want to generate profiles for.
4. After profiles are generated create `secrets.py` inside the root directory. Set `apiKey = XXX`
5. By default if a file already exists in `results/` sim.py will skip it
6. To run the sims use `python sim.py dir/ [--iterations X]` where `dir/` is the sim directory you want to sim

**IF YOU WANT TO STOP THE SCRIPT USE CTRL+Z**

## SimC Script for Azerite Traits
```
.\simc.exe spell_query=azerite.class=hunter | Out-File 'A:\simc-bfa\hunter-traits.txt'
```

## Base Actor Information
All sims are run with the following as a base (unless specified otherwise)

### Talent Combos
Every sim is run with the top Five builds
- 1: ViV_HB_BS_FS_BoP
- 2: ViV_HB_BS_FS_Chak
- 3: ViV_GT_BS_FS_Chak
- 4: ViV_HB_BS_FS_WI
- 5: ViV_HB_BS_TotS_BoP

### Azerite Traits
- TBD

### Stats - Mythic (Percent Stat - Gear Amount)
- 19.56% Crit - 1048
- 14.04% Haste - 955
- 4.27% Versatility - 363
- 19.00% Mastery - 564
- 7588 Agility - 4750

### Enchants
- Weapon: TBD
- Ring: TBD

### Consumables
- Food: [Bountiful Captains Feast](https://bfa.wowhead.com/item=156526/bountiful-captains-feast)

## Results
- [talents](https://github.com/djriff/bfa-survival-sims/tree/master/talents)
- [bulk weights](https://github.com/djriff/bfa-survival-sims/tree/master/stats)
- [azerite traits](https://github.com/djriff/bfa-survival-sims/tree/master/azerite-traits)
- [racials](https://github.com/djriff/bfa-survival-sims/tree/master/racials)
- [consumables](https://github.com/djriff/bfa-survival-sims/tree/master/consumables)
- [enchants](https://github.com/djriff/bfa-survival-sims/tree/master/enchants)
- [APL Tests](https://github.com/djriff/bfa-survival-sims/tree/master/apl)
- [antorus composite scaling](https://docs.google.com/spreadsheets/d/1xfME0P6LKmI541Ma6NE7b5XahWu-rxdFUSHy0Y-MoCM/edit?usp=sharing)

##Credit
- Publik (https://github.com/seanpeters86/bfa-shadow-priest) for getting the ball rolling and writing the majority of the scrips.
