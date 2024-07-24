# Changelog

In this document you will find the changelog for this mod documenting every change made in every version. This changelog was started with version 1.08.58, but will be retroactively updated for older versions of the mod, starting with version 1.06.04 since 1.06.03 is the first version to be committed to GitHub and thus differences can only be documented from 1.06.04.

In the case of a weapon name changing, that change will not be listed in the modifications section. Instead, it will be listed in the weapons section with a note saying the modification name was changed accordingly, unless there is a reason for the modification's name to be different, in which case a seperate entry will exist in the modifications section.

In the case of a weapon being renamed in the same patch that its weight or caliber and weapon type tags are added, the list of tag changes will use the renamed version of the weapon.

All dates are listed in DD-MM-YYYY format.

## 1.08.65 - 24-07-2024

### General:

- #### Changes:

    - All loading screens with vehicle names in their name have been adjusted to use the vehicles' proper names and to ensure consistent formatting across all of them. I know this seems like a small change, but the game has 177 loading screens and I went insane doing this.

### Vehicles:

- #### Additions:

    - Updated for the Skilled Marksman Battle Pass season and the Flight of the Albatross event.
    - **Sikorsky Aircraft Corperation / Elbit Systems / Israeli Air Force** added as the manufacturer for the **AH-60**.
    - **Vultee Aircraft** added as the manufacturer for the **A-35B**. **Vultee V-88** has been added as the manufacturer's designation.

- #### Changes:

    - Long name of the **Ki 200** changed from **Ki 200 Shusui** to **J8M1 | Ki 200 Shūsui**
    - **AH-60** renamed to **Yanshuf Hamush**. Its long long story, but the short version is that the Sikorsky Armed Black Hawk Demonstrator, while similar, is not the same vehicle. The Yanshuf Hamush was developed from the ABH Demonstrator by a combination of teams from the Sikorsky Aircraft Corperation, Elbit Systems, and the Israeli Air Force. I nor anyone I know has been able to find an actual name for it so **Yanshuf Hamush**, its nickname, is the best we have. If you can find an actual name, please report it.
    - **AH-1G** long name changed from **AH-1G Tzefa** to **AH-1G Tzefa Alef**.
    - **AH-1Q** long name changed from **AH-1Q Tzefa** to **AH-1Q Tzefa Bet**.
    - **AH-1S (FMC)** long name changed from **AH-1S Tzefa (Fully Modernized Cobra)** to **AH-1S Tzefa Dalet (Fully Modernized Cobra)**.
    - **MD 500/Orev** long name changed from **MD 500/Orev Defender ""Lahatut""** to **MD 500/Orev Lahatut**
    - **Peten** (USA and Israel) short name changed to **AH-64A**. The long name has been changed from **McDonnell Douglas Helicopter Systems | Peten** to **McDonnell Douglas Helicopter Systems | AH-64A Peten**.
    - **Peten (PV264)** short name changed to **AH-64A (PV264)**. The long name has been changed from **McDonnell Douglas Helicopter Systems | Peten (PV264)** to **McDonnell Douglas Helicopter Systems | AH-64A Peten (PV264)**.
    - **Saraph** short name changed to **AH-64D-I**. The long name has been changed from **Boeing Rotorcraft Systems | Saraph** to **Boeing Rotorcraft Systems | AH-64D-I Saraph**.
    - **MD 500/Orev** long name changed from **MD 500/Orev Defender "Lahatut"** to **MD 500/Orev Lahatut**.
    - **Rooivalk Mk1F** renamed to **Rooivalk Mk. 1F**.
    - "Alcione" added to the long name of the **Z.1007bis III** and **Z.1007bis V**.
    - **Alcione** (the ship, not the **Z.1007bis**) renamed to **Alcione (F 544)**. The long name has been changed from **Albatross-class, Alcione F544** to **Albatross-class, Alcione (F 544)**.
    - The short name of the **Sholef** has been changed to the **Sholef V1**.
    - **PBM-5A "Mariner"** renamed to **PBM-5A Mariner**. The short name has been changed to the **PBM-5A**.
    - The **PBM-3** has been moved in the files to match the reorganization of the US air tree. I had forgotten to do this earlier. This has no affect ingame, but does make `units.csv` more organized.
    - "Cobra" added to the long names of the **AH-1F** and **AH-1G**.
    - **Schützenpanzer lang Typ 12-3 mit 105mm Leichtgeschütz M40A1** renamed to **Schützenpanzer lang Typ 12-3 mit 106mm Leichtgeschütz M 40 A1**. The short name has been changed to **SPz 12-3 (LGs M 40 A1).
    - Roundel removed from the **VBCI 2 (MCT-30)**.
    - **M247** given the name "Sergeant York" in its long name.
    - "Cicogna" added to the long names of the **BR.20 BR** and **BR.20M M1**.
    - **Challenger 1** folder changed from **Challenger Mk. 2 / 3** to **Challenger 1, Mk. 2 / 3** to match the names of the vehicles in it.
    - "Moderna" removed from the short name of the **T-72M2 Moderna**.
    - **A-35B** changed to **A-35B-VU**.
    - **TK №106** renamned to **TK No. 106**.

### Weaponry:

- #### Additions:

    - Added the **M401** shell.
    - Added the **M401 (PF)** shell.
    - Added the **Soltam M839** howitzer used by the **Sholef V1**.
    - Added the **305 mm Mk.4 depth charge**.

- #### Changes:

    - Corrected updated file name for the **BGM-71A-3**. Both file name entries are now in `units_weaponry.csv` because I'm not sure if the other one is still being used.
    - The **155 mm Soltam M839 cannon** has been renamed to the **Model 839P**.
    - The caliber and type tag has been added to the **Model 839P** howitzer.
    - Renamed the **305 mm Mk.4 depth charge** to the **305 mm Mk. 4 depth charge**. It'll get a proper rename later but right now it's just to fit with the rest of the mod's formatting.
    - the **HWZ** tag has been changed to **CNN-HWZ**.
    - **Rb 05 A** renamed to **Rb 05A**.

### Modifications:

- #### Additions:

    - Added missing text for the **T-90S**' **Dozer Blade** modification.

- #### Changes:

    - "Hexachloroethane" changed to not be capitalized in the description of the naval **Exhaust smokescrean** modification.
    - Tank modifications rework (all descriptions have been accordingly reworked):
        - **Parts improvement** renamed to **Repair equipment**.
        - **Improved FSE** renamed to **Fire extinguishers**.
        - **Tracks** renamed to **Track maintenance**.
        - **Tires** renamed to **Tire maintainance**.
        - **Suspension** renamed to **Suspension maintainance**.
        - **Filters** renamed to **Filter maintainance**.
        - **Brake System** renamed to **Brake maintainance**.
        - **Transmission** renamed to **Transmission maintainance**.
        - **Engine** renamed to **Engine maintainance**.
        - **Crew Replenishment** renamed to **Crew replenishment**.
        - **Horizontal Drive** renamed to **Horizontal traverse lubrication**.
        - **Adjustment of Fire** renamed to **Gun maintainance**.
        - **Elevation Mechanism** renamed to **Vertical traverse lubrication**.
        - **Rangefinder**: only description reworked
        - **Laser rangefinder**: only description reworked
        - **Laser warning system**: only description reworked
        - **LWS / LR** renamed to **LRF / LWS**.
        - **LWS / LR** renamed to **1V528-1 + 1G46 / TShU-1 + 1-11** (this is specifically the **T-90A**'s laser rangefinder and laser warning recievers).
        - **Artillery Support** renamed to **Artillery support**.
        - **Smoke grenade** renamed to **Smoke grenades**.
        - **TVD** renamed to **Thermal imager**.
        - **NVD** renamed to **Image intensifier**.
        - **ESS** renamed to **Exhaust smokescreen**.
        - **Dozer Blade** renamed to **Entrenching bade**.

## 1.08.64 - 20-07-2024

### Vehicles:

- #### Changes:

    - "Kai" removed from the distance name of the **Ki-108 Kai** to match other vehicles.
    - **Artilleriefährprahm Typ D1, AF 99** changed to **Artilleriefährprahm Typ D 1 | AF 99**.
    - **Artilleriefährprahm Typ D3, AF 128** changed to **Artilleriefährprahm Typ D 3 | AF 128**.
    - **A-4E (AFC 418)** (USA and Israel) changed to **A-4E (AFC 418-II)**. The folder containing the Israeli **A-4E (AFC 418-II)** has been adjusted accordingly.
    - The "AFC" modification has been moved to after the vehicle's name in the long name for the **A-4E (AFC 418-II)** (USA and Israel) and the **A-4E (AFC 482)**.
    - "otsu" changed to "Otsu" in the long name of the **Ki 43-III Otsu**.
    - **Ki-84** changed to **Ki 84-I**.
    - **Ki 10-II (№77 Sentai)** changed to **Ki 10-II (No. 77 Sentai)**.
    - "-I" added to the closer of the 2 distance names for the **Ki 10-I** and **Ki 10-I (No. 1 Sentai)** to match the format of other vehicles.
    - "-II" added to the closer of the 2 distance names for the **Ki 10-II** and **Ki 10-II (No. 77 Sentai)** to match the format of other vehicles.
    - "-II" added to the closer of the 2 distance names for the **Ki 100-II** to match the format of other vehicles.
    - "Otsu" added to the closer of the 2 distance names for the **Ki 102 Otsu** and **Ki 102 Otsu** to match the format of other vehicles.
    - Every Japanese "Ki-" plane (including ones captured by other countries) has been changed from "Ki-" to "Ki " because Japanese writing does not use the "-" character and that appears to be to be a postwar addition in English. This means that, for example, the **Ki-44-I** becomes the **Ki 44-I**. This change has happened to the following vehicles and all folders associated with them:
        - **Ki 43-II** (USA)
        - **Ki 61-Ib** (USA)
        - **Ki 43-III Otsu**
        - **Ki 43-II**
        - **Ki 61-I Hei**
        - **Tada's Ki 61-I Hei**
        - **Ki 61-I Kō**
        - **Ki 61-I Otsu**
        - **Ki 84-I**
        - **Ki 200**
        - **Ki 49-I**
        - **Ki 49-II Kō**
        - **Ki 49-II Otsu**
        - **Ki 49-II Otsu (late)**
        - **Ki 67-I Otsu**
        - **Ki 67-I Kō**
        - **Ki 10-II (No. 77 Sentai)**
        - **Ki 10-I**
        - **Ki 10-I (No. 1 Sentai)**
        - **Ki 10-II**
        - **Ki 45 Kai Kō**
        - **Ki 45 Kai Kō (Tei)**
        - **Ki 45 Otsu**
        - **Ki 45 Hei**
        - **Ki 45 Kai Hei (Tei)**
        - **Ki 45 (Tei)**
        - **Ki 48-II Otsu**
        - **Ki 32**
        - **Ki 96**
        - **Ki 102 Otsu**
        - **Ki 84-I Kō**
        - **Ki 84-I Kō** (China)
        - **Ki 84-I Otsu**
        - **Ki 84-I Hei**
        - **Ki 27 Otsu**
        - **Ki 27 Otsu (No. 4 Sentai)**
        - **Ki 43-I**
        - **Ki 21-Ia**
        - **Ki 44-I**
        - **Ki 44-I (Hikō No. 47 Chūtai)**
        - **Ki 61-I Tei**
        - **Ki 44-II Otsu**
        - **Ki 44-II Hei**
        - **Ki 44-II Hei** (China)
        - **Ki 27 Otsu** (China)
        - **Ki 43-III Kō**
        - **Ki 45 Kai Hei (Tei)** (China)
        - **Ki 61-I Otsu** (China)
        - **Ki 83**
        - **Ki 61-II Kai Kō**
        - **Ki 100-I**
        - **Ki 87**
        - **Ki 94-II**
        - **Ki 21-I Hei**
        - **Ki 100-II**
        - **Ki 109**
        - **Ki 108 Kai**
    - **IS-4M** corrected to have **Ob"yekt 701-6** in its long name. This was done to the tutorial **IS-4M**, but I forgot to do it to the standard tech tree one.
    - **T-2(K)** renamed to **T-2 (late)**
    - **T-2(K) (conversion)** renamed to **T-2 (late) (ADTW)**. It's an annoying story and I don't want to talk about it.

## 1.08.63 - 17-07-2024

### Vehicles:

- #### Changes:

    - **Albatross F543** renamed to **Albatross (F 543)**.
    - **HMS Valhalla** year changed from 1924 to 1922.
    - **Saetta P-494** renamed to **Saetta (P 494)**.
    - **Freccia P-493** renamed to **Freccia (P 493)**.
    - Short name for the **Sparviero** boat has been changed to **Sparviero (P 420)**. The long name has stayed the same.

## 1.08.62 - 17-07-2024

### Vehicles:

- #### Changes:

    - Belgian **F-16A-15OCU-CF** renamed to **F-16A-15-CF**.
    - **Messerschmitt-Bölkow-Blohm BO 105 CB-3, Helikopter 9A** renamed to **Messerschmitt-Bölkow-Blohm | Helikopter 9A**.
    - **BO 105 CB-2 | försökspansarvärnshelikopter med pansarvärnrobotsystemet HeliTOW** renamed to **Messerschmitt-Bölkow-Blohm / Försökscentralen | Helikopter 9A (HeliTOW)**. The short name has been changed to **hkp 9A (HeliTOW)** and its roundel has been removed. This vehicle is a mutant but this is the closest I could get.
    - **Sud-Aviation SE 3130 Alouette II, Helikopter 2** renamed to **Sud-Aviation | Helikopter 2**.
    - The "Fully Modernized Cobra" text has been moved to after the word "Tzefa" in the long name of the Israeli **AH-1S (FMC)**.
    - **Agusta 204B, Helikopter 3C** renamed to **Agusta | Agusta 204B | Helikopter 3C**.
    - The following vehicles have had their manufacturers added:
        - **hkp 3C**
        - **hkp 9A**
        - **hkp 9A (HeliTOW)**
        - **SE 313 B**
        - **SA 316 B**
        - **AH-64A** (Sweden)
    - "A.H. Mk. 1" has been removed from the furthest distance name of the **Lynx A.H. Mk. 1** to match standard formatting for this mod.
    - "A.H. Mk. 1" has been removed from the furthest distance name of the **Scout A.H. Mk. 1** to match standard formatting for this mod.
    - The Argentinian **SK105-A2** has gotten a new roundel.

### Weapons:

- #### Additions:

    - Added missing short text for the **HOT** missile.
    - Added missing text for the **HOT-K3S**.
    - Added missing text for the **UH Tiger**'s and all of the French **Tigre**s' **AIM-92A**.
    - Added missing text for the **Swingfire**'s launcher.
    - Added missing text for the **L37A2** machine gun.
    - Added missing split countermeasure text (this whole split countermeasures thing is a text nightmare lol).
    - Added missing text for the **60 APC (ATM-1)**'s launcher.
    - Added missing text for the **JSW L/52** cannon.
    - Added missing text for the **Type 56** cannon.
    - Added missing text for the **GIAT М693/mod F2** autocannon.
    - Added missing text for the **MIT 12.7 CRC F1** machine gun.
    - Added missing text for the **kan m/41** cannon.
    - Added missing short text for the **BGM-71A3**.
    - Added missing text for the **BTM1** shell.
    - Added text for the new **RVV-AE**. The modification has been added too.
    - The following bombs have had weight and type tags added:
        - **BAFG-230**
        - **BFA-230/2**
        - **BAFG-460**
        - **BFA-460/2**
        - **BAFG-920**
        - **BINC-300**
        - **BAFG-230 (Lizard 2)**
        - **RVV-AE**
    - Added the new default weapon texts for the following missiles:
        - **RVV-AE**
        - **AIM-54A**
        - **AIM-54C**
        - **AIM-7M**
        - **AIM-120B**
        - **R-27R**
        - **R-77**
        - **Skyflash**
        - **AIM-9L**
        - **V4**
        - **AIM-7F**
        - **PL8**
        - **R-27R1**
        - **Matra Super 530D**
        - **MICA-EM**
        - **Rb 71**
        - **Rb 99**
        - **AIM-9M-4**
        - **Python 3**
        - **Derby**

- #### Changes:

    - **BGM-71A3** renamed to **BGM-71A-3**.
    - **DTB-1** renamed to **DTB1**.
    - **230 kg BAFG-230 bomb** renamed to **Bombas Aéreas de Fins Gerais 230**.
    - **230 kg BAF-230/2 ballute-type retarted bomb** renamed to **Bomba com Freio Aerodinâmico 230/2**.
    - **460 kg BAFG-460 bomb** renamed to **Bombas Aéreas de Fins Gerais 460**.
    - **460 kg BAF-460/2 ballute-type retarted bomb** renamed to **Bomba com Freio Aerodinâmico 460/2**.
    - **920 kg BAFG-460 bomb** renamed to **Bombas Aéreas de Fins Gerais 920**.
    - **BINC-300 incendiary bomb** renamed to **Bombas Incendiárias 300**.
    - **BA-FG-230-Lizard-2 guided bomb** renamed to **Bombas Aéreas de Fins Gerais 230 (Lizard 2)**

## 1.08.61 - 07-07-2024

### Vehicles:

- #### Changes:

    - **MiG-23ML** changed from **Izdeliye 23-12** to **Izdeliye 23-12A**. This was supposed to be done in 1.08.60, but there was a typo and I only wrote "12" instead of "12A".

## 1.08.60 - 06-07-2024

Note: I wanted to push this update in a later and more complete state, but I'm about to disappear for 2 weeks so I have to push it now.

### General:

- #### Changes:

    - The format for all countries ingame has been reworked to now display the full English name of the country and, when possible, the name of that country in its native language transliterated to Latin characters. These 2 names are seperated by a slash. The names in the bar in the hangar where you select what country you are playing have remained unchanged, except for **Great Britain** which has been renamed to the **UK** in its short name.
    - The **War Tinder's Lang Mod** text has been changed to **War Tinder's Historical Localization Mod**.

### Vehicles:

- #### Changes:

    - **MiG-23ML** changed from **Izdeliye 23-16** to **Izdeliye 23-12A**.
    - The **Stormer HVM** has been renamed to the **F.V.4333 (HVM)** because **Stormer** is the name of the missile system, not the vehicle.

### Weaponry

- #### Changes:

    - **High explosive obstracle reduction shell** changed to **High explosive obstacle reduction shell**.

### Modifcations:

- #### Changes:

    - Renamed **BLU-1** modification to **BLU-1/B**.
    - **GBU-8/15** modification renamed to **GBU-8/B / 15(V)1/B**.
    - **GBU-38 JDAM** modification renamed to **GBU-38**.
    - **GBU-12** modification renamed to **GBU-12/B**.
    - **GBU-16** modification renamed to **GBU-16/B**.
    - **GBU-24** modification renamed to **GBU-24/B**.
    - **GBU-10** modification renamed to **GBU-10/B**.
    - **GBU-10 / 24** modification renamed to **GBU-10/B / 24/B**.
    - **AGM-123 Skipper** renamed to **AGM-123A**.
    - **Mk. 77 Mod 4** renamed to **Mk 77 Mod 4**.
    - **Mk78** renamed to **Mk 78 Mod 0**.
    - **Mk77 mod 4** renamed to **Mk 77 Mod 4**.
    - **Mk79** renamed to **Mk 79 Mod 1**.

## 1.08.59 - 01-07-2024

### General:

- #### Changes:

    - Changed the color of the "War Tinder's Lang Mod [version]" text to match the color of the text right above it listing how many players are online.

### Vehicles:

- #### Additions:

    - Added **Cadillac Motor Car Division** as the manufacturer for the **M551** and **M551 (M32A1)**.

- #### Changes:

    - The **Torpedo-Schnellboot, Libelle-Klasse, Projekt 131.400** has been renamed to **kleines Torpedoschnellboot Projekt 131 ""Libelle"" | Nr. 401**. The short name has been adjusted to **Nr. 401** accordingly.
    - Missing **KPz** added to the short name of the **Leopard 2 A7 HU**.
    - The **M4** from the War Thunder Mobile promotion has been changed over to use the **Tank, Medium** nomenclature. This was missed in 1.08.56 when the rest of the M4s were switched over to use this nomenclature.
    - **leichter Kampfpanzer M 41** changed to **leichter Kampfpanzer M 41 G**. The short name was already **M 41 G**, but the "G" was missing in the long name.
    - The long name of the **Project 89.2UR, Bernau (343)** has been changed to **Projekt 89.2 UR, Bernau (343), 1985**. This will probably be changed back at a later date when I do a review of naval formatting as a whole, but for now, it has been changed to fit with the format of all other vessels in the game.
    - The long name of the **Flakträger Krischan der Große (1943)** has been changed to **Flakträger Krischan der Große, 1943**. This will probably be changed back at a later date when I do a review of naval formatting as a whole, but for now, it has been changed to fit with the format of all other vessels in the game.
    - **Panzerjäger I / Sd.Kfz. 251/10** folder renamed to **Pz.Jgr. I / m.S.P.W. D (7,5cm K.)** to match the short names of the vehicles.
    - Seperator removed from the long name of the **Vextra 105** because GIAT Industries named it the **Vextra 105** while the French Army never had a name for it because it never adopted it.
    - **Flugabwehrraketenradwagen 1 A2 Roland auf Lkw 15t mil gl Kat 1A1** renamed to **Flugabwehrraketenradwagen 1 A2 Roland auf Lkw 15t mil gl Kat 1 A1**.
    - The **Super AMX 30** has been corrected to use the **Engin principal de combat** nomenclature. The other **AMX 30**s had it, but the **Super AMX 30** was missing it.

### Weaponry:

- #### Additions:

    - Missing text entires have been added for the following weapons and explosives:
        - **HE-OR** shell type.
        - **SAPHEI-T** round type
        - **Pl-3** HEAT rocket.
        - **Oerlikon Typ 3Z 8Dla** rocket launcher
        - **MILAN** ATGM used on the **Marder 1 A1 (-)** and the **Marder 1 A3**
        - **T140E3 cannon**
        - **M8C machine gun**
        - **6P49MT machine gun**
        - **82 mm M-8 rocket** (there was already text for this in the game but a second text entry for it was missing)
        - **9M113** (there was already text for this in the game but a second text entry for it was missing)
        - **D-126 gun-launcher**
        - **3M7**
        - **50 mm countermeasures** (this is specifically for MAWS because there are like 50 gaijillion text entires for this)
        - **YaK-B machine gun** (a second text entry for this)
        - **PKT machine gun**
        - **TKB-481 machine gun**
        - **FAB-100sv** (the default version of the weapon)
        - **BGM-71** (the **Belgleitpanzer 57** uses a different text entry which was missing)
        - **FIM-92E** (some short name was missing)
        - **HN6** (some short name was missing)
        - **Octol/TNT**
        - **Anti-Tank Guided Missile** (the text for the file `atgm_ke_tank` was missing)
        - **MIM-72A** (text entires already existed for it but one was missing)
        - **Napalm**
        - **7.62 mm FN 60.30 machine gun**
        - **30 mm MK103/38 cannon** (the Zerstörer 45's guns)
    - The **Guided Missile, Air to Air** nomenclature has been added to certain **AIM-9E**, **AIM-9L**, and **AIM-9M-4** text entires that were previously missing it.
    - The following weapons and launchers have had their caliber and weapon type tags added:
        - **FN MAG 60-40**
        - **M37E1**
        - **M134**
        - **M85**
        - **AN/M2** (the cannon, not the machine gun)
        - **LW25**
        - **M139**
        - **M242**
        - **M195**
        - **M197** (both the standard and the one that Gaijin calls the TM197B)
        - **ADEN**
        - **ADEN Mk. 4**
        - **ADEN 25**
        - **LR30**
        - **M4** (the 37 mm one)
        - **M9**
        - **M10**
        - **GAU-4/A**
        - **GAU-13/A**
        - **GAU-19/A**
        - **GAU-12/U**
        - **GAU-8/A**
        - **Mk 11 Mod 0**
        - **Mk 11 Mod 5**
        - **Mk 12 Mod 0**
        - **Mk 12 Mod 3**
        - **M1** (the 40 mm automatic one, not the 6 billion other cannons named **M1**)
        - **M266**
        - **M1** (the 57 mm one, I told you there like 6 billion of them)
        - **M1897A4**
        - **M32** (the gun)
        - **M2** (the 75 mm cannon)
        - **M6**
        - **M3** (the 75 mm one)
        - **T15E1** (the 75 mm cannon on the **XA-38**, not the 90 mm cannon on the **T26E4-1**)
        - **M5**
        - **T13E1**
        - **M3** (the 90 mm one)
        - **M3A1**
        - **M36**
        - **Cannone da 90/50 M3A1**
        - **M41**
        - **PzK M 41**
        - **M54**
        - **T15E1** (the 90 mm one on the **T26E4-1**)
        - **T15E2**
        - **T54**
        - **T208E9**
        - **M4** (the 105 mm howitzer)
        - **T5E1**
        - **T5E2**
        - **T140E2**
        - **T140E3**
        - **XM35**
        - **IMI MG251**
        - **T53**
        - **M81**
        - **M162**
        - **XM150E5**
        - **T7**
        - **M2** (the 155 mm howitzer)
        - **BGM-71** (certain text entires of it were missing it)
        - **BGM-71C**
        - **BGM-71D-5**
        - **Launcher, Tubular, Guided Missile, M220A1**
        - **Launcher, Tubular, Guided Missile, M220A2, Dual Launcher**
        - **Guided Missile System, Aerial-Intercept, M54A2**
        - **FIM-92X** (I'm not really sure why I'm changing an April Fools Day event missile over a year after the event ended)
        - **MGM-166A LOSAT Launch System**
        - **Roland SAM**
        - **Grenade, Launcher, 40mm, M129**
        - **Grenade, Launcher, 40mm, M75**
        - **HVAR**
        - **M8**
        - **Grenade, Launcher, Smoke, M82**
        - **Schnellnebelkerze 39**
        - **11.75-inch AR**
        - **5-inch AR**
        - **Sani-Flush**
        - **AN/M30A1**
        - **AN/M57**
        - **Mk 81 Mod 0**
        - **Mk 81 Mod 1**
        - **AN/M64A1**
        - **Mk 82 Mod 0**
        - **Mk 82 Mod 1 (BSU-49/B)**
        - **Mk 82 Mod 1**
        - **M32** (the bomb)
        - **M117**
        - **JM117**
        - **AN/M65A1**
        - **AN/M65A1 (M129)**
        - **Mk 9 Mod 0**
        - **AN/Mk 33 Mod 0**
        - **Mk 83 Mod 1**
        - **Mk 83 Mod 0**
        - **Mk 13 Mod 0**
        - **AN/Mk 1**
        - **AN/M66A1**
        - **Mk 84 Mod 0**
        - **Mk 84 Mod 1 (BSU-50/B)**
        - **AN/M34** (type tag only because I couldn't find the weight due to it being unused ingame)
        - **M63** (type tag only because I couldn't find the weight due to it being unused ingame)
        - **M118**
        - **AN/M56**
        - **Mk 13 Mod 7**
        - **Mk 13 Mod 3**
        - **Mk 79 Mod 1**
        - **BLU-27/B (finned)**
        - **BLU-1/B**
        - **BLU-10/B** (type tag only because I couldn't find the weight due to it being unused ingame)
        - **BLU-23/B** (type tag only because I couldn't find the weight due to it being unused ingame)
        - **M116A2**
        - **Mk 77 Mod 2**
        - **Mk 77 Mod 4**
        - **Mk 77 Mod 0**
        - **Mk 78 Mod 2**
        - **AS.34**
        - **BK 27**.

- #### Changes:

    - US gun rework (the short names for all of them have been adjusted accordingly):
        - **7.62 mm M37 machine gun** renamed to **Machine Gun, 7.62mm, M37E1**.
        - **7.62 mm M134 Minigun machine gun** renamed to **Machine Gun, 7.62mm, M134**.
        - **12.7 mm M85 machine gun** renamed to **Machine Gun, Caliber .50, M85**.
        - **20 mm AN/M2 cannon** renamed to **Gun, 20mm, Automatic, AN/M2**. This is not the same as the 12.7 mm machine gun that is also named the **AN/M2**. That machine gun was fixed ages ago.
        - **25 mm LW25 cannon** renamed to **Gun, Automatic, 25mm, LW25**.
        - **20 mm M139 cannon** renamed to **Gun, Automatic, 20mm, M139**.
        - **25 mm M242 cannon** renamed to **Gun, Automatic, 25mm, M242**.
        - **20 mm M195 cannon** renamed to **Cannon, 20mm, M195**.
        - **20 mm M197 cannon** renamed to **Cannon, 20mm, M197**.
        - **20 mm TM197B cannon** renamed to **Cannon, 20mm, M197** (**TM197B** is the turret system; **M197** is the gun).
        - **30 mm LR30 cannon** renamed to **LR30**.
        - **37 mm M4 cannon** renamed to **Gun, 37mm, M4**.
        - **37 mm M9 cannon** renamed to **Gun, 37mm, M9**.
        - **105 mm M68 cannon** renamed to **Gun, 105mm, M68** (this is for the M60A1 AOS and the Italian premium M60A1). This was already done for the M68 cannon, but for some unfathomable reason, the M60A1 AOS and the Italian premium M60A1 use a different text entry for the same gun.
        - **37 mm M10 cannon** renamed to **Gun, 37mm, Automatic, M10**.
        - **20 mm GAU-4 cannon** renamed to **Cannon, 20mm, GAU-4/A**.
        - **30 mm GAU-13/A cannon** renamed to **Cannon, 30mm, GAU-13/A**.
        - **12.7 mm GAU-19 machine gun** renamed to **Gun, Automatic, 12.7mm, GAU-19/A**.
        - **25 mm GAU-12/U cannon** renamed to **Cannon, 25mm, GAU-12/U Equalizer**.
        - **25 mm GAU-12U cannon** renamed to **Cannon, 25mm, GAU-12/U Equalizer** (this is the same gun but for the LAV-AD).
        - **20 mm GAU-8/A cannon** renamed to **Cannon, 30mm, GAU-8/A Avenger**.
        - **20 mm Browning-Colt Mk12 Mod 0 cannon** renamed to **Cannon, 20mm, Mk 12 Mod 0**.
        - **20 mm Browning-Colt Mk12 Mod 3 cannon** renamed to **Cannon, 20mm, Mk 12 Mod 3**.
        - **20 mm Mk. 11 cannon** renamed to **Cannon, 20mm, Mk 11 Mod 0**.
        - **20 mm Mk. 11 mod 5 cannon** renamed to **Cannon, 20mm, Mk 11 Mod 5**.
        - **40 mm Dual Automatic Gun M2** renamed to **Gun, 40mm, Automatic, M1**. **M1** is the gun, **M2** is the carriage.
        - **40 mm M266 automatic cannon** renamed to **Gun, Automatic, 40mm, M266**.
        - **57 mm M1 cannon** renamed to **Gun, 57mm, M1**.
        - **75 mm M1897A4 cannon** renamed to **Gun, 75mm, M1897A4**.
        - **75 mm M32 cannon** renamed to **Gun, 75mm, M32**.
        - **75 mm M2 cannon** renamed to **Gun, 75mm, M2**.
        - **75 mm M6 cannon** renamed to **Gun, 75mm, M6**.
        - **75 mm M3 cannon** renamed to **Gun, 75mm, M3**.
        - **75 mm M10 cannon** renamed to **Gun, 75mm, T15E1**. It was put into service as the **M10** but when mounted on the **XA-38** it was still the **T15E1**.
        - **75 mm T13E1 cannon** renamed to **Gun, 75mm, M5**.
        - **75 mm T13E1 cannon** renamed to **Gun, 75mm, T13E1** (there are 2 guns that Gaijin calls the **T13E1**: the actual **T13E1** (this one) and the **M5** which Gaijin has called the T13E1 even though the file name and the real name are both **M5**).
        - **75 mm XM274 cannon** renamed to **Gun, 75mm, XM274**.
        - **90 mm M3 cannon** renamed to **Gun, 90mm, M3**.
        - **90 mm M3A1 cannon** renamed to **Gun, 90mm, M3A1**.
        - **90 mm M36 cannon** renamed to **Gun, 90mm, M36**.
        - **90 mm M41 cannon** renamed to **Gun, 90mm, M41**.
        - **90 mm M54 cannon** renamed to **Gun, 90mm, M54**.
        - **90 mm T15E1 cannon** renamed to **Gun, 90mm, T15E1**.
        - **90 mm T15E2 cannon** renamed to **Gun, 90mm, T15E2**.
        - **90 mm T54 cannon** renamed to **Gun, 90mm, T54**.
        - **90 mm T208E9 cannon** renamed to **Gun, 90mm, T208E9**.
        - **105 mm M4 howitzer** renamed to **Howitzer, 105mm, M4**.
        - **105 mm T5E1 cannon** renamed to **Gun, 105mm, T5E1**.
        - **105 mm T5E2 cannon** renamed to **Gun, 105mm, T5E2**.
        - **105 mm T140E2 cannon** renamed to **Gun, 105mm, T140E2**.
        - **105 mm T140E3 cannon** renamed to **Gun, 105mm, T140E3**.
        - **105 mm XM35 cannon** renamed to **Gun, 105mm, XM35**.
        - **120 mm M58 cannon** renamed to **Gun, 120mm, M58**.
        - **120 mm T53 cannon** renamed to **Gun, 120mm, T53**.
        - **152 mm gun/launcher M81** renamed to **Gun-Launcher, 152mm, M81**.
        - **152 mm M162 gun/launcher** renamed to **Gun-Launcher, 152mm, M162**.
        - **152 mm XM150E5 gun/launcher** renamed to **Gun-Launcher, 152mm, XM150E5**.
        - **155 mm T7 cannon** renamed to **Gun, 155mm, T7**.
        - **75 mm M2 howitzer** renamed to **Howitzer, 75mm, M2**.
    - US missile and rocket rework (the short names for all of them have been adjusted accordingly):
        - **BGM-71 TOW** renamed to **Launcher, Tubular, Guided Missile, M220A1**. This is NOT the **BGM-71 TOW** missile. This is the **Wiesel 1 A2 TOW**'s launcher that Gaijin has called the **BGM-71 TOW** instead of the name of the launcher. The missile has stayed the same.
        - **BGM-71 TOW** renamed to **Launcher, Tubular, Guided Missile, M220A2, Dual Launcher**. This is NOT the **BGM-71 TOW** missile. This is the **M3A3 CFV**'s launcher that Gaijin has called the **BGM-71 TOW** instead of the name of the launcher. The missile has stayed the same.
        - **BGM-71 TOW** renamed to **Launcher, Tubular, Guided Missile, M220A2, Dual Launcher**. This is NOT the **BGM-71 TOW** missile. This is a launcher that Gaijin has called the **BGM-71 TOW** instead of the name of the launcher. The missile has stayed the same. I do not remember what vehicle this launcher is for.
        - **BGM-71B TOW** renamed to **Launcher, Tubular, Guided Missile, M220A1**. This is NOT the **BGM-71B TOW** missile. This is a launcher that Gaijin has called the **BGM-71B TOW** instead of the name of the launcher. The missile has stayed the same. I do not remember what vehicle this launcher is for.
        - **BGM-71 TOW** renamed to **Launcher, Tubular, Guided Missile, M220A1**. This is NOT the **BGM-71 TOW** missile. This is a launcher that Gaijin has called the **BGM-71 TOW** instead of the name of the launcher. The missile has stayed the same. I do not remember what vehicle this launcher is for.
        - **BGM-71C ITOW** renamed to **Launcher, Tubular, Guided Missile, M220A1**. This is NOT the **BGM-71C ITOW** missile. This is a launcher that Gaijin has called the **BGM-71C ITOW** instead of the name of the launcher. The missile has stayed the same. I do not remember what vehicle this launcher is for.
        - **FFAR Mighty Mouse rocket** renamed to **Rocket Motor, 2.75-inch FFAR Mk 4**.
        - **FFAR Mighty Mouse rocket M429** renamed to **Rocket Motor, 2.75-inch FFAR Mk 4, M429**.
        - **FFAR Mighty Mouse rocket M429** renamed to **Rocket Motor, 2.75-inch FFAR Mk 4, M439**.
        - **Zuni Mk32 Mod 0 ATAP rocket** renamed to **Rocket Motor, 5-inch FFAR Mk 32 Mod 0 ATAP**.
        - **Tiny Tim rocket** renamed to **Rocket Motor, 11.75-inch AR**.
        - **AR rocket** renamed to **Rocket Motor, 5-inch AR**
        - **HN-6** renamed to **HN6** to fit with other Chinese designations.
        - **FIM-92 Stinger** renamed to **FIM-92X Stinger** (this is the **FIM-92X** from the mobile infantry event and I'm not really sure why I changed this one).
        - **BGM-71D** renamed to **BGM-71D-5**. The modifications have been adjusted accordingly.
        - The following missiles have been changed to use the **Guided Missile, Surface Attack** nomenclature:
            - **BGM-71C**
            - **BGM-71D-5**
        - **40 mm M129 grenade launcher** renamed to **Grenade, Launcher, 40mm, M129**.
        - **40 mm M75 grenade launcher** renamed to **Grenade, Launcher, 40mm, M75**.
        - **HVAR rocket** renamed to **Rocket Motor, 5-inch HVAR**.
        - **M8 rocket** renamed to **Rocket, 4.5-inch, HE, M8**.
        - **Shilleglagh** has been removed from the name of the **MGM-51B** to match the short names of other missiles. The **MGM-51B** does not have a long name ingame but this is done to match the short name.
        - The following missiles have been changed to the use **Guided Missile, Air to Surface** nomenclature:
            - **AGM-65A**
            - **AGM-65B**
            - **AGM-65D**
            - **AGM-65G**
            - **AGM-65H**
    - US bomb, mine, and torpedo rework (the short names for all of them have been adjusted accordingly):
        - **100 lb AN-M30A1 bomb** renamed to **Bomb, 100lb, GP, AN/M30A1**.
        - **250 lb AN-M57 bomb** renamed to **Bomb, 250lb, GP, AN/M57**.
        - **250 lb LDGP Mk 81 bomb** renamed to **Bomb, 250lb, GP, Mk 81 Mod 0**.
        - **500 lb Mk 81 Snakeye high-drag tail fin retarded bomb** renamed to **Bomb, 250lb, GP, Mk 81 Mod 1 Snakeye**.
        - **300 lb H.E. M31 bomb** renamed to **Bomb, 300lb, Demolition, M31**.
        - **500 lb AN-M64A1 bomb** renamed to **Bomb, 500lb, GP, AN/M64A1**.
        - **500 lb LDGP Mk. 82 bomb** renamed to **Bomb, 500lb, GP, Mk 82 Mod 0**.
        - **500 lb Mk 82 AIR ballute-type retarded bomb** renamed to **Bomb, 500lb, GP, Mk 82 Mod 1 (BSU-49/B)**
        - **500 lb Mk 82 Snakeye high-drag tail fin retarded bomb** renamed to **Bomb, 500lb, GP, Mk 82 Mod 1 Snakeye**.
        - **600 lb H.E. M32 bomb** renamed to **Bomb, 600lb, GP, M32**.
        - **750 lb M117 cone 45 bomb** renamed to **Bomb, 750lb, GP, M117**.
        - **750 lb M117 cone 90 bomb** renamed to **Bomb, 750lb, GP, M117**.
        - **1000 lb AN-M65A1 bomb** renamed to **Bomb, 1000lb, GP, AN/M65A1**.
        - **1000 lb AN-M65A1 Fin M129 bomb** renamed to **Bomb, 1000lb, GP, AN/M65A1 (M129)**.
        - **1000 lb GP Mk9 bomb** renamed to **Bomb, 1000lb, GP, Mk 9 Mod 0**.
        - **1000 lb A.P. AN-MK 33 bomb** renamed to **Bomb, 1000lb, AP, AN/Mk 33 Mod 0**.
        - **1000 lb Mk 83 AIR ballute-type retarded bomb** renamed to **Bomb, 1000lb, GP, Mk 83 Mod 1 Snakeye**.
        - **1000 lb LDGP Mk. 83 bomb** renamed to **Bomb, 1000lb, GP, Mk 83 Mod 0**.
        - **1000 lbs Type A Mark I aircraft laid magnetic mine** renamed to **Mine, Mk 13 Mod 0, Magnetic Induction**.
        - **1600 lb AN-Mk. 1 armor-piercing bomb** renamed to **Bomb, 1600lb, AP, AN/Mk 1**.
        - **2000 lb AN-M66A2 bomb** renamed to **Bomb, 2000lb, GP, AN/M66A1**.
        - **2000 lb LDGP Mk. 84 bomb** renamed to **Bomb, 2000lb, GP, Mk 84 Mod 0**.
        - **2000 lb LDGP Mk. 84 Air bomb** renamed to **Bomb, 2000lb, GP, Mk 84 Mod 1 (BSU-50/B)**.
        - **2000 lb H.E. M34 bomb** renamed to **Bomb, 2000lb, GP, AN/M34**. This bomb doesn't get a weight tag due to me not being able to find its weight because I'm pretty sure nothing ingame actually uses this bomb.
        - **1400 lb A.P. M63 bomb** renamed to **Bomb, 1400lb, AP, M63**. This bomb doesn't get a weight tag due to me not being able to find its weight because I'm pretty sure nothing ingame actually uses this bomb.
        - **3000 lb M118 Demolition bomb** renamed to **Bomb, 3000lb, GP, M118**.
        - **4000 lb AN-M56 bomb** renamed to **Bomb, 4000lb, LC, AN/M56**
        - **Mk. 13-6 Case Torpedo (2216 lbs)** renamed to **Torpedo, 22.5-inch, Mk 13 Mod 7**.
        - **Mk. 13-6 Torpedo (2216 lbs)** renamed to **Torpedo, 22.5-inch, Mk 13 Mod 3**.
        - **1000 lb Mk. 79 Mod 1 incendiary bomb** renamed to **Bomb, 1000lb, Fire, Mk 79 Mod 1**.
        - **BLU-27/B incendiary bomb** renamed to **Bomb, 750lb, Fire, BLU-27/B (finned)**.
        - **BLU-1/B incendiary bomb** renamed to **Bomb, 750lb, Fire, BLU-1/B**.
        - **BLU-10/B incendiary bomb** renamed to **Bomb, 250lb, Fire, BLU-10/B**. This bomb doesn't get a weight tag due to me not being able to find its weight because I'm pretty sure nothing ingame actually uses this bomb.
        - **BLU-23/B incendiary bomb** renamed to **Bomb, 500lb, Fire, BLU-23/B**. This bomb doesn't get a weight tag due to me not being able to find its weight because I'm pretty sure nothing ingame actually uses this bomb.
        - **Mk. 77 mod 2 incendiary bomb** renamed to **Bomb, 500lb, Fire, Mk 77 Mod 2**.
        - **Mk. 77 mod 4 incendiary bomb** renamed to **Bomb, 500lb, Fire, Mk 77 Mod 4**.
        - **Mk. 78 incendiary bomb** renamed to **Bomb, 750lb, Fire, Mk 78 Mod 2**.
    - **Mk. 77 mod 0 incendiary bomb** renamed to **Bomb, 500lb, Fire, Mk 77 Mod 0**.
    - **M116A2 incendiary bomb** renamed to **Bomb, 750lb, Fire, M116A2**.
    - **750 lb JM117 cone 45 bomb** renamed to **Bomb, 750lb, GP, JM117**.
    - **66 mm smoke grenade launcher** renamed to **Grenade, Launcher, Smoke, M82** (this is the American 66 mm one because there are like a billion of them).
    - **90 mm M41 cannon** renamed to **PzK M 41** (this is the German **M41** cannon, not the American one which has renamed to the American designation)
    - Corrected the **FAB-250M-54**'s weight class from 500 kg to 250 kg. This is not its weight tag. It does not have that yet. This is the way Gaijin formats weights.
    - **Smoke grenade launcher** renanmed to **Schnellnebelkerze 39** (this is the German 91 mm smoke grenade).
    - **27 mm Mauser BK27** renamed to **BK 27**.

### Modifications:

- #### Changes:

    - The names and tooltips for the **Mk. II year 1942** and **Mk. II year 1943** modifications have been reworked to be **Hispano Mk. II (1942)** and **Hispano Mk. II (1943)** in order to be more understandable and to clarify in the name that both are modifications of the **Hispano Mk. II**.
    - The following modification names have been reworked to align with the US weapon review:
        - **Mk81** renamed to **Mk 81 Mod 0**.
        - **Mk82** renamed to **Mk 82 Mod 0**.
        - **Mk83** renamed to **Mk 83 Mod 0**.
        - **Mk84** renamed to **Mk 84 Mod 0**.
        - **AN-M57A1 BOX** renamed to **AN/M57**.
        - **AN-M64A1 BOX** renamed to **AN/M64A1**.
        - **M83** renamed to **Mk 83 Mod 0**.
        - **M83-2** renamed to **Mk 83 Mod 0 (x4)**.
        - **Mk. 13 Mod 0** renamed to **Mk 13 Mod 0**.
        - **M64** renamed to **AN/M64A1**.
        - **M82** renamed to **Mk 82 Mod 0**.
        - **M82-2** renamed to **Mk 82 Mod 0 (x4)**.
        - **Mk118** renamed to **M118**.
        - **AN-M56** renamed to **AN/M56**.
    - Descriptions have been reworked for the following modifications:
        - **LAU-3/A**
        - **JLAU-3/A**
        - **Mk 81 Mod 0**
        - **Mk 82 Mod 0**
        - **Mk 83 Mod 0**
        - **Mk 84 Mod 0**
        - **M117**
        - **AN/M57**
        - **AN/M64A1**
        - **Mk 83 Mod 0 (x4)**
        - **Mk 13 Mod 0**
        - **Mk 82 Mod 0 (x4)**
        - **M118**
        - **AN/M56**

## 1.08.58 - 25-06-2024

### Vehicles:

- #### Additions:

    - Added **SEPECAT** as manufacturer and **SEPECAT Jaguar A** as the manufacturer and manufacturer's name for the vehicle for the **Jaguar A** nuclear bombers, as well as to the standard **Jaguar A**, the **Jagaur E**, **Jaguar G.R. Mk. 1**, **Jaguar G.R. Mk. 1B**, and only as the manufacturer's name for the vehicle for the **Jaguar IS (DARIN II)**.
    - Added **SEPECAT / Hindustan Aeronautics Limited** as the manufacturer for the **Jaguar IS (DARIN II)**.
    - Added **Avions Marcel Dassault-Breguet Aviation / Dornier Flugzeugwerke** as the manufacturer for the **Alpha Jet A** and **Alpha Jet E**.
    - **4,7cm Pa.K. 36(t) (Sfl.) auf Fahrgestell Panzerkampfwagen I (II Serie)** added as alternate name in the long name for the **Panzerjäger I**.
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
    - Changed the folder name for the **Marder / StuG III** folder to **Marder III / StuG III A** to specify the variants.
    - Changed the **F-100D-65-NA**'s name to **F-100D-66-NA**.
    - Changed the **F-100A-15-NA**'s name to **F-100A-16-NA**.
    - Changed the **F-100F-6-NA**'s name to **F-100F-6-NA**.
    - Changed the **F-100D-35-NH**'s name to **F-100D-10-NA**.
    - **Panzeräger I** short name changed to **Pz.Jgr. I** to match the format of other German WWII ground vehicles.
    - Corrected the Chinese **PB4Y-2** to the **P4Y-2** to reflect the year that the ROC obtained it.
    - **F-47D-23 / 30** changed to **P-47D-23 / F-47D-30**.
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
        - **H-75A-4**'s name changed to **H75-C1 (4ème série)**.
        - The name of the **H-75A-1 / 4** folder has been changed to reflect the new names of the vehicles in it.
        - **Mirage 4000**'s short name changed to **Mirage 4000 (1986)**. This change already existed in the long name, but has now been applied to the short name.
    - **DB-7**'s name changed to **DB-7 B-3** to match its French designation because it is a French vehicle. It has also had an additional French roundel added to reflect it being a vehicle that, if in the French tree, would have a roundel attached, in addition to it being a French vehicle in the British tree. This means it now has 2 roundels.
    - **Merkava Mk. 3B** changed to **Merkava Mk. 3 Ramaqh**.
    - **Namer (RCWS-30)**'s long name changed to **Nagmash Merkava (RCWS-30)**. The short name has remained the same.

- #### Bug fixes:

    - Fixed a missing space before the slash in the **Pz.Kpfw. 38 (t) F / n.A.** folder.
    - Corrected the order of the variants listed in the **Pz.Kpfw. III E / B**. Previously the B and E were switched which does not reflect the order of the vehicles in the folder.

### Weaponry:

- #### Additions:

    - The following weapons have had their caliber and weapon type tags added:
        - **JM61-RFS**
        - **JM61-M**

- #### Changes:

    - The **PG 02**'s default gun has been changed from **20 mm rotary cannon JM61** to **20 mm Machine Gun, JM61-RFS**.
    - The **PG 02**'s lower fire rate gun that can be gotten through a modification has been changed from **20 mm rotary cannon JM61** to **20 mm Machine Gun, JM61-M**. The modification has been changed accordingly.

### Modifications:

- #### Changes:

    - The names and tooltips of all naval modifications, excluding specific weapon and ammunition types, have been reworked.

## 1.08.57 - 24-06-2024

### Vehicles:

- #### Changes:

    - Changed the **J11A**'s name to the **J11A (MLU)**.

### Weaponry:

- #### Changes:

    - The **LKk/42**'s long name has been changed to the **12,70 mm LentoKonekivääri m/42**. The short name has been adjusted to **12,70 LKk/42**.
    - The **FN-Browning M.36 No.3** used on the **FRm sarja I** and **FR-76 (1937)** has had its name changed to the **7,70 mm LentoKonekivääri m/36**. Its short name has beeen adjusted to **7,70 LKk/36**.
    - The following weapons have had their caliber and weapon type tags added:
        - **Hispano Mk. I**
        - **Hispano Mk. II**
        - **Hispano Mk. V**
        - **12,70 LKk/42**
        - **7,70 LKk/36**
        - **FN-Browning M.36 No.3**
        - **FN-Browning M.36 No.4**

## 1.08.56 - 22-06-2024

### Vehicles:

- #### Changes:

    - **F-47D-23 / 30** folder changed to **P / F-47**.
    - **M4A3E2** name changed to **M4A3E2 (75) W**.
    - The following vehicles have been changed to use the **Tank, Light** nomenclature in their long name:
        - **M5A1**
        - **M5A1 (Twitch Drop)**
        - **M5A1 (China)**
        - **M3A3 (China)**
        - **M3A3 (1st PTG)**
    - The following vehicles have been changed to use the **Tank, Medium** nomenclature in their long name:
        - **M4A1**
        - **M4**
        - **M4A2**
        - **M4A3 (105) HVSS**
        - **M4A1 (76) W**
        - **M4A2 (76) W**
        - **M4A2 (76) W (tutorial)**
        - **M4A3E8 (76) W HVSS**
        - **M4A3E2 (75) W**
        - **M4 (M3)**
        - **M4A3E2 (76) W**
        - **M4A3E2 (76) W (37th T.Bat.)**
        - **M4A2 (1944)**
            - Note: this vehicle is unused and will likely never be added
        - **M4A4 (China)**
        - **M4A4 (1st PTG)**
        - **M4A1 (75) W**
        - **M4A3E8 (76) W HVSS (Japan)**
    - The following vehicles have been changed to use the **Tank, Heavy** nomenclature in their long name:
        - **M6A1**
        - **M6A2E1-1**
        - **T1E1**
    - **2A6M4** added as alternate name in the long name of the **ZSU-23-4M4**.
    - **2A6** added as alternate name in the long name of the **ZSU-23-4**.
    - The French **Medium Tank M4A3 (105) HVSS Sherman** has been changed to **Char moyen M4A3 (105) HVSS Sherman**.
    - **Sherman M4A1 tourelle FL10** changed to **Char moyen M4A1 Sherman (tourelle FL 10)**.
    - The French **Assault Tank M4A3E2 Jumbo** has been changed to **Char d'assaut M4A3E2 (75) W**.
    - **Vultee Aircraft / Central Aircraft Manufacturing Company** added as the manufacturer for the **V-11-G** and **V-12-D**.
    - **V-11-G** and **V-12-D** changed in their long names to **Vultee V-11-G** and **Vultee V-12-D** respectively to reflect **V-11-G** and **V-12-D** being Vultee's names for the aircraft.
    - **"Type 58"** nickname for the **T-34-85 (1960s)** moved to after the vehicle name as a nickname for the whole vehicle, instead of inside the parentheses with "1960s" where it used to be.

### Weaponry:

- #### Additions:

    - The following bombs have been changed to use the **Bomb, Guided** nomenclature in their long name:
        - **GBU-12/B**
        - **GBU-16/B**
        - **GBU-10/B**
        - **GBU-24/B**
        - **GBU-15(V)1/B**
        - **GBU-15(V)2/B**
        - **GBU-8/B**
        - **GBU-38 JDAM**
    - **Guided Missile, Air to Surface** nomenclature added to the long name of the **AGM-123**.

- #### Changes:

    - The following bombs have had their weight tags corrected to match their ingame weight:
        - **KAB-500Kr**
        - **KAB-500Kr-E**
        - **KAB-500L-F-E**
        - **KAB-1500Kr**
        - **AGM-62A**
        - **AGM-62A ER**
    - The following bombs have had their weight tags switched over from pounds to kilograms to universalize the weight tag system:
        - **GBU-16/B**
        - **GBU-24/B**
        - **GBU-15(V)1/B**
        - **GBU-15(V)2/B**
        - **GBU-8/B**
        - **GBU-38 JDAM**
    - **AGM-123 Skipper** renamed to the **AGM-123A Skipper II**.
    - Weapon type tag of the **AGM-123A** changed from **BMB-LG-RKT** to **AGM-LG**.
    - **1000-фн Mk.13 №117**'s name changed to **1000 lb Mk. 13 No. 117**.
    - The **Drop tank «Hindenburg» (495 gal)** has been renamed to the **2250 Litre External Fuel Tank** as part of the project to give all fuel tanks their correct names. Fuel tank names are extremely hard to find so this is a very slow project.
    - **MIM146** corrected to **MIM-146A**. The launcher has been corrected too.
    - The weapon type tag of the **V4 Radar Darter** has been corrected. Previously there was a typo in the closing color tag which made the entire stat card of the missile orange instead of just the weapon type tag.
    - **QJC88A machine gun** renamed to **QJC88A 12.7mm Vehicle Anti-Aircraft Machine Gun**.
    - **Type 86 machine gun** renamed to **QJT86 7.62mm Vehicle Machine Gun**.
    - **SA45 cannon** renamed to **Canon de 90mm SA 45**.
    - **SA47 cannon** renamed to **Canon de 90mm SA 47**.
    - **SA 49 cannon** renamed to **Canon de 75mm SA 49**.
    - **SA 50 L/57 cannon** renamed to **Canon de 75mm SA 50 L/57**.
### Modifications:

- #### Changes:

    - **GBU-8** renamed to **GBU-8/B**.
