# Changelog

In this document you will find the changelog for this mod documenting every change made in every version. This changelog was started with version 1.08.58, but will be retroactively updated for older versions of the mod, starting with version 1.06.04 since 1.06.03 is the first version to be committed to GitHub and thus differences can only be documented from 1.06.04.

In the case of a weapon name changing, that change will not be listed in the modifications section. Instead, it will be listed in the weapons section with a note saying the modification name was changed accordingly, unless there is a reason for the modification's name to be different, in which case a seperate entry will exist in the modifications section.

All dates are listed in DD-MM-YYYY format.

## 1.08.58 - 25-06-2024

### Vehicles:

- #### Additions:

    - Added **SEPECAT** as manufacturer and **SEPECAT Jaguar A** as the manufacturer and manufacturer's name for the vehicle for the **Jaguar A** nuclear bombers, as well as to the standard **Jaguar A**, the **Jagaur E**, **Jaguar G.R. Mk. 1**, **Jaguar G.R. Mk. 1B**, and only as the manufacturer's name for the vehicle for the **Jaguar IS (DARIN II)**.
    - Added **SEPECAT / Hindustan Aeronautics Limited** as the manufacturer for the **Jaguar IS (DARIN II)**.
    - Added **Avions Marcel Dassault-Breguet Aviation / Dornier Flugzeugwerke** as the manufacturer for the **Alpha Jet A** and **Alpha Jet E**.
    - **Panzeräger I** added as alternate name in the long name for the Panzerjäger **Panzeräger I**.
    - Added **Douglas Aircraft Company** as the manufacturer and **Douglass DB-7** as the manufacturer's name for the vehicle for the following vehicles:
        - **Havoc Mk. I**
        - **Boston Mk. I**
        - **DB-7**

- #### Changes:

    - Reorganized all of rank 1 of the German ground tree. This does not affect anything ingame and is purely a change within `units.csv` for better organization.
    - Moved the location of the text entries for the tutorial version of the **M4A2 (76) W**. This does not affect anything ingame and is purely a change within `units.csv` for better organization.
    - Changed the **Flakpanzer I A**'s name to **Pz.Kpfw. I A (2cm Fla.K. 38)**. The long name has been adjusted accordingly.
    - Changed the **Flakpanzer 38**'s name to **Flak.Pz. 38** to match up with other German vehicles
    - Changed the folder name for the **Pz.Kpfw. I A (2cm Fla.K. 38)** and **Flak.Pz. 38** to reflect their new names.
    - Changed the **F-100D-65-NA**'s name to **F-100D-66-NA**.
    - Changed the **F-100A-15-NA**'s name to **F-100A-16-NA**.
    - Changed the **F-100F-6-NA**'s name to **F-100F-6-NA**.
    - Changed the **F-100D-35-NH**'s name to **F-100D-10-NA**.
    - **Panzeräger I** short name changed to **Pz.Jgr. I** to match the format of other German WWII ground vehicles.
    - Corrected the Chinese **PB4Y-2** to the **P4Y-2** to reflect the year that the ROC obtained it.
    - The following vehicles have had their roundels removed due to their names not being the same as any other country's name for them or for them being entirely unique:
        - **Boomerang Mk. I**
        - **Boomerang Mk. II**
        - **Wirriway Mk. I**
        - **Hellcat F. Mk. II**
        - **Havoc Mk. I**
        - **Boston Mk. I**
        - **Avenger T.R. Mk. II**
        - **Catalina Mk. IIIa**
        - **Hudson Mk. V**
        - **Corsair F. Mk. II**
    - Changed the **Ki-44-I 34**'s name to **Ki-44-I (Hikō No. 47 Chūtai)**. The long name has been adjusted accordingly.
    - Minor French aircraft rework:
        - Corrected the French **PB4Y-2** to the **PB4Y-2S**.
        - **M.B.162**'s name changed to **M.B.162.01** to reflect its prototype status.
        - **Potez 630**'s name changed to **Potez 630.01** to reflect its prototype status.
        - **Potez 631**'s name changed to **Potez 631.01** to reflect its prototype status.
        - **Potez 633**'s name changed to **Potez 633.01** to reflect its prototype status.
        - **M.B.157**'s name changed to **M.B.157-C1**.
        - **M.B.152C1**'s name changed to **M.B.152-C1**.
        - **M.S.405C1**'s name changed to **M.S.405-C1**.
        - **M.S.406C1**'s name changed to **M.S.406-C1**.
        - **M.S.410**'s name changed to **M.S.410-C1**.
        - **VB.10C-1**'s name changed to **VB 10-C1**.
        - **VB.10-02**'s name changed to **VB 10-02**.
        - **V.G.33C-1**'s name changed to **VG 33-C1**.
        - **C.R.174C1**'s name changd to **CR.174-C1**.
        - **H-75A-1**'s name changed to **H75-C1 (1ère série)**.
        - **H-75A-4**'s name changed to **H75-C1 (1ème série)**.
        - The name of the **H-75A-1 / 4** folder has been changed to reflect the new names of the vehicles in it.
        - **Mirage 4000**'s short name changed to **Mirage 4000 (1986)**. This change already existed in the long name, but has now been applied to the short name.
    - **DB-7**'s name changed to **DB-7 B-3** to match its French designation because it is a French vehicle. It has also had an additional French roundel added to reflect it being a vehicle that, if in the French tree, would have a roundel attached, in addition to it being a French vehicle in the British tree. This means it now has 2 roundels.
    - **Merkava Mk. 3B** changed to **Merkava Mk. 3 Ramaqh**.
    - **Namer (RCWS-30)**'s long name changed to **Nagmash Merkava (RCWS-30)**. The short name has remained the same.

- #### Bug fixes:

    - Fixed a missing space before the slash in the **Pz.Kpfw. 38 (t) F / n.A.** folder.
    - Corrected the order of the variants listed in the **Pz.Kpfw. III E / B**. Previously the B and E were switched which does not reflect the order of the vehicles in the folder.

### Weaponry:

- #### Changes:

    - The **PG 02**'s default gun has been changed from **20 mm rotary cannon JM61** to **20 mm Machine Gun, JM61-RFS**.
    - The **PG 02**'s lower fire rate gun that can be gotten through a modification has been changed from **20 mm rotary cannon JM61** to **20 mm Machine Gun, JM61-M**. The modification has been changed accordingly.

### Modifications:

- #### Changes:

    - The names and tooltips of all naval modifications, excluding specific weapon and ammunition types, have been reworked.