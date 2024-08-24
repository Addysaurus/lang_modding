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

## A note about version numbering

Version numbering is generally standard. 1.08.66, 1.08.67, 1.08.68, etc. That is how incremental versions work. Every time there is a major update, the second level version number changes (e.g. when Seek and Destroy came out, the version number rolled over from 1.07.XX to 1.08.XX). If you check the commit history, you will also see variants with "d" in their names (e.g. 1.08.69d9). The "d" stands for "dev" and is the marker of a dev build. These are not the official releases of the mod, those can be found in the releases tab, but you still can download and install them if you want. Just be aware that they are unfinished and may be inconsistent with themselves due to being work-in-progress. The version numbering of dev builds are also more inconsistent. You won't see commits for, for example, 1.08.69d9, 1.08.69d10, 1.08.69d11, etc. You may see, for example, a commit for 1.08.69d9, and then the next commit may be 1.08.69d12 because not all dev builds get pushed to GitHub. You can run dev builds if you want, but you will have the download the files manually because they are not part of the releases and, given the frequency at which dev builds update, I recommmend you just wait for the next release because you will be updating the mod way more times than you need to if you download every dev build.

## Transliteration

All languages are transliterated; none are translated.

### Russian

Russian is transliterated with a modified version of GOST 7.79-2000 A (ISO 9:1995). Below you can find the transliteration chart used for Russian.

#### Russian transliteration chart:

- А а &nbsp; &nbsp;→ &nbsp; &nbsp;A a
- Б б &nbsp; &nbsp;→ &nbsp; &nbsp;B b
- В в &nbsp; &nbsp;→ &nbsp; &nbsp;V v
- Г г &nbsp; &nbsp;→ &nbsp; &nbsp;G g
- Д д &nbsp; &nbsp;→ &nbsp; &nbsp;D d
- Е е &nbsp; &nbsp;→ &nbsp; &nbsp;Ye ye
- Ё ё &nbsp; &nbsp;→ &nbsp; &nbsp;Ë ë
- Ж ж &nbsp; &nbsp;→ &nbsp; &nbsp;Ž ž
- З з &nbsp; &nbsp;→ &nbsp; &nbsp;Z z
- И и &nbsp; &nbsp;→ &nbsp; &nbsp;I i
- Й й &nbsp; &nbsp;→ &nbsp; &nbsp;J j
- І і &nbsp; &nbsp;→ &nbsp; &nbsp;Ì ì (this is not a standard Russian alphabet character and is only used in this mod in Pavyel Âkaŭlyevìč Galavačoŭ's name)
- К к &nbsp; &nbsp;→ &nbsp; &nbsp;K k
- Л л &nbsp; &nbsp;→ &nbsp; &nbsp;L l
- М м &nbsp; &nbsp;→ &nbsp; &nbsp;M m
- Н н &nbsp; &nbsp;→ &nbsp; &nbsp;N n
- О о &nbsp; &nbsp;→ &nbsp; &nbsp;O o
- П п &nbsp; &nbsp;→ &nbsp; &nbsp;P p
- Р р &nbsp; &nbsp;→ &nbsp; &nbsp;R r
- С с &nbsp; &nbsp;→ &nbsp; &nbsp;S s
- Т т &nbsp; &nbsp;→ &nbsp; &nbsp;T t
- У у &nbsp; &nbsp;→ &nbsp; &nbsp;U u
- Ў ў &nbsp; &nbsp;→ &nbsp; &nbsp;Ŭ ŭ (this is not a standard Russian alphabet character and is only used in this mod in Pavyel Âkaŭlyevìč Galavačoŭ's name)
- Ф	ф &nbsp; &nbsp;→ &nbsp; &nbsp;F f
- Х	х &nbsp; &nbsp;→ &nbsp; &nbsp;Kh kh
- Ц	ц &nbsp; &nbsp;→ &nbsp; &nbsp;Cz cz (C before I, E, Y, and J)
- Ч	ч &nbsp; &nbsp;→ &nbsp; &nbsp;Č č
- Ш	ш &nbsp; &nbsp;→ &nbsp; &nbsp;Š š
- Щ	щ &nbsp; &nbsp;→ &nbsp; &nbsp;Ŝ ŝ
- Ъ	ъ &nbsp; &nbsp;→ &nbsp; &nbsp;"
- Ы	ы &nbsp; &nbsp;→ &nbsp; &nbsp;Y y
- Ь	ь &nbsp; &nbsp;→ &nbsp; &nbsp;'
- Э	э &nbsp; &nbsp;→ &nbsp; &nbsp;È è
- Ю	ю &nbsp; &nbsp;→ &nbsp; &nbsp;Û û
- Я	я &nbsp; &nbsp;→ &nbsp; &nbsp;Â â