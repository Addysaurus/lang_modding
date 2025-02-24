## Installation instructions

1. Go to your War Thunder folder and open the file called config.blk.

2. Find the section titled "debug" within config.blk.

3. Within the debug section, add the line "testLocalization:b=yes". This must be a new line. It can be anywhere in the section, but adding it at the end is preferable. For example, this is what the debug section in my config.blk file looks like (you shouldn't copy this, this is just an example):

debug{
  screenshotAsJpeg:b=yes
  512mboughttobeenoughforanybody:b=yes
  enableNvHighlights:t="auto"
  netLogerr:b=yes
  testLocalization:b=yes
}

4. Launch the game. Once you have launched the game, a folder called lang will appear in your War Thunder folder.

5. Drop every file ending in .csv and the file localization.blk from this mod's Mod files folder that you dowloaded into that lang folder. It will tell you that this is replacing an existing file. THIS IS OKAY. This modified localization.blk file does not remove any of the things already in the base file. It simply adds this mod's files to the end of the load order so they will be read after the base game files, allowing the mod to work.

6. Launch the game. The mod should now be installed and working.

7. This step is optional. One of the files you added is called userlang.csv. This file exists for you to add anything you add or change anything you want about the mod. Want to rename a vehicle? Go for it. An engine? You can do that too. A weapon or a menu text? Sure! It's all doable. This file exists at the end of the load order, so even if a text entry for what you are changing already exists in a different file, your change will apply. It is recommended that you find the text you are trying to change in either the WTHLM files or the base files, copy that line into userlang.csv, and then make your change.

## Installing packages

This mod has additional packages you can install to modify vehicle names and put vehicles and weapons in their original languages for non-Latin scripts. To install these packages, do the following:

1. Find the packages you want from this mod's `Packages` folder.

2. Drop the package folders you select into your `lang` folder. That's it! You're done.

Available packages:
- Language packages:
  - Japanese:
    - This package puts Japanese vehicles and weapons into Japanese.
  - Farsi:
    - This package puts Japanese vehicles and weapons into Farsi.
  - Thai:
    - This package puts Japanese vehicles and weapons into Thai.
- Other packages:
  - Finnish Ps. designators
    - This packages makes the short names of Finnish ground vehicles their Ps. designations.