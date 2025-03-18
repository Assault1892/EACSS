# Easy Anti Cheat Splash Swapper - EACSS

https://github.com/user-attachments/assets/a56c266e-3d90-451e-9cb3-87a65f2f2629

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
6. 
EACSSの引数はこんなかんじ: `"C:\Program Files (x86)\Steam\steamapps\common\VRChat\EACSS.exe" %COMMAND%`

`EACSS.exe restore` で初期状態に戻せます。
