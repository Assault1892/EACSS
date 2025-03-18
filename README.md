# Easy Anti Cheat Splash Swapper - EACSS

Easy Anti Cheat (EAC) のスプラッシュ画像をゲーム起動時にランダムに差し替えるプログラム。  
VRChat以外では動作確認してません。

パスやファイル名を書き換えればUE4のスプラッシュ画像とか、そもそも画像じゃない奴らも差し替えできると思います。サポートはしません。

## つかいかた

1. 最新のリリースをダウンロード
2. `EACSS.exe` と `config.toml` をスプラッシュ画像を差し替えたいゲームのexeと同じフォルダに配置
3. `config.toml` を開き `src_dir` を差し替えたい画像群が入ってるフォルダパスに変更
   1. バックスラッシュは `\\` か `/` に置き換え
4. ゲームの起動引数の頭に `[EACSS.exeのフルパス] %COMMAND%` を追加
5. おわり

こんなかんじ: `"C:\Program Files (x86)\Steam\steamapps\common\VRChat\EACSS.exe" %COMMAND%`