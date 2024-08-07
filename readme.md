# War Tinder's Historical Localization Mod

## Description

This mod corrects many of the names ingame due to most of them being anywhere between mildly and horribly inaccurate, as well as adding a lot of new formatting. This mod corrects and reformats vehicle names, weapon names, modification names, engine names, nation names, loading screen names, tips, and some menu texts, with new updates coming very frequently!

You can get the mod by downloading the mod's `.zip` file from the release marked as "latest" here: https://github.com/Addysaurus/lang_modding/releases

You can report a bug or make a suggestion for the mod here: https://github.com/Addysaurus/lang_modding/issues

You can find the changelog for the mod here: https://github.com/Addysaurus/lang_modding/blob/main/changelog.md

Below, you can learn how to install the mod. Please note that this mod is meant for English. These localizations do not work in other languages.

## Installation instructions

1. Go to your War Thunder folder and open the file called `config.blk`.

2. Find the section titled `debug` within `config.blk`.

3. Within the `debug` section, add the line `testLocalization:b=yes`. This must be a new line. It can be anywhere in the section, but adding it at the end is preferable. For example, this is what the `debug` section in my `config.blk` file looks like (you shouldn't copy this, this is just an example):

```
debug{
  screenshotAsJpeg:b=yes
  512mboughttobeenoughforanybody:b=yes
  enableNvHighlights:t="auto"
  netLogerr:b=yes
  testLocalization:b=yes
}
```

4. Launch the game. Once you have launched the game, a folder called `lang` will appear in your War Thunder folder.

5. Drop every file ending in `.csv` from this mod's folder that you dowloaded into that `lang` folder. Also drop in the file `localization.blk`. It will tell you that this is replacing an existing file. THIS IS OKAY. This modified `localization.blk` file does not remove any of the things already in the base file. It simply adds this mod's files to the end of the load order so they will be read after the base game files, allowing the mod to work.

6. Launch the game. The mod should now be installed and working.

7. This step is optional. One of the files you added is called `userlang.csv`. This file exists for you to add anything you add or change anything you want about the mod. Want to rename a vehicle? Go for it. An engine? You can do that too. A weapon or a menu text? Sure! It's all doable. This file exists at the end of the load order, so even if a text entry for what you are changing already exists in a different file, your change will apply. It is recommended that you find the text you are trying to change in either the WTHLM files or the base files, copy that line into `userlang.csv`, and then make your change.

## Additional things to know

There are some other things to note.

The biggest thing to know is that lang mods for War Thunder, much like sound mods, are entirely allowed. Instructions exist for installing them on the War Thunder Wiki (link: https://wiki.warthunder.com/Instructions_for_the_user_localizations), as well as guidelines for making lang mods, though the guidelines are really more just suggestions (link: https://wiki.warthunder.com/Localization_Guidelines). Nothing about this mod is illicit in any way and you will not be banned or penalized for it.

Another thing to know is that every time this mod updates, you will have to reinstall it. You do not need to go through the entire process again, you just need to download the newest version and drop its files into the `lang` folder.

Also be aware that if the game updates to add a new piece of text or a new vehicle or anything like that, you will need to delete the `lang` folder. This does not do anything bad. All you need to do is delete the `lang` folder and then when you run the game, a new one will be generated. Then, just drop the mod files in that new `lang` folder. You do not need to change anything about `config.blk`.

The final thing to know is that sometimes, usually when the game updates, the first time you load into the game after that update, several texts will be broken. Achievements, events, and stuff like that will show the names of the files instead of the text they are supposed to show. I have no idea why War Thunder does this. But don't worry, the fix is simple! Just close the game and reload it. That's it. I don't know why War Thunder does this, but reloading the game fixes it.

Thank you for downloading this mod and I hope you enjoy it (and aren't caught offguard by the level of changes lol).