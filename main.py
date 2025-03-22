# MARK: IMPORTS
import subprocess
from tomllib import load
import pathlib
import random
import shutil
import os
import sys
import cv2

# MARK: FUNCTIONS
def load_config():
    """設定ファイルを読み込む"""
    try:
        with open("config.toml", "rb") as conf_file:
            return load(conf_file)
    except FileNotFoundError:
        print("config.tomlが見つかりません！")
        sys.exit(1)

def get_source_files(src_dir):
    """ソースディレクトリから画像ファイルのリストを取得"""
    # 複数の画像形式をサポート
    image_extensions = ["*.png", "*.jpg", "*.jpeg", "*.gif"]
    files = []
    src_path = pathlib.Path(src_dir)
    
    for ext in image_extensions:
        files.extend(src_path.glob(ext))
    
    return files

def get_random_image(src_files):
    """ランダムな画像を選択"""
    if not src_files:
        raise ValueError("画像ファイルが見つかりません")
    return random.choice(src_files)

def validate_config(src_dir, src_files):
    """config.tomlの設定を検証"""
    if not src_dir:
        print("ソースディレクトリが設定されていません！")
        return False
    
    src_path = pathlib.Path(src_dir)
    if not src_path.exists():
        print(f"ソースディレクトリ '{src_dir}' が存在しません！")
        return False
    
    if not src_path.is_dir():
        print(f"'{src_dir}' はディレクトリではありません！")
        return False
        
    if not src_files:
        print(f"'{src_dir}' に画像ファイルが見つかりません！")
        return False
        
    return True

def handle_backup(action: str):
    """バックアップの作成または復元"""
    splash_dir = pathlib.Path("./EasyAntiCheat")
    splash_path = splash_dir / "SplashScreen.png"
    backup_path = splash_dir / "SplashScreen.png.orig"
    
    # ディレクトリの存在チェック
    if not splash_dir.exists():
        print("EasyAntiCheatディレクトリが見つかりません！")
        return False
    
    if action == "backup":
        if not splash_path.exists():
            print("SplashScreen.pngが見つかりません！")
            return False
            
        if not backup_path.exists():
            try:
                print("バックアップを作成します！")
                shutil.copy2(splash_path, backup_path)  # copy2でメタデータも保持
                print("バックアップが完了しました！")
                return True
            except IOError as e:
                print(f"バックアップの作成に失敗しました: {e}")
                return False
        else:
            print("バックアップはすでに存在します")
            return True
            
    elif action == "restore":
        if backup_path.exists():
            try:
                print("バックアップから復元します！")
                shutil.copy2(backup_path, splash_path)
                print("バックアップからの復元が完了しました！")
                return True
            except IOError as e:
                print(f"復元に失敗しました: {e}")
                return False
        else:
            print("バックアップファイルが存在しません！")
            return False
    
    return False

def resize_image(image_path, width, height):
    """画像をリサイズして保存"""
    try:
        img = cv2.imread(str(image_path))
        # より高速なリサイズ手法を使用
        img_resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite("./EasyAntiCheat/SplashScreen.png", img_resized, [cv2.IMWRITE_PNG_COMPRESSION, 3])
        print("リサイズした画像を上書きしました！")
        return True
    except Exception as e:
        print("画像のリサイズに失敗しました！", e)
        return False

# MARK: MAIN FUNCTION
def main():
    print("# EasyAntiCheat Splash Screen Changer - EACSS #")
    
    # 設定ファイルの読み込みを関数内で行う
    conf = load_config()
    src_dir = conf["src_dir"]
    
    # 必要な時だけファイルリストを取得
    src_files = get_source_files(src_dir)
    
    if not validate_config(src_dir, src_files):
        print("config.tomlを確認してください！")
        sys.exit(1)

    args = sys.argv
    game_executable = args[1:]

    if len(args) > 1 and args[1] == "restore":
        handle_backup("restore")
    else:
        handle_backup("backup")
        print("ランダムな画像を選択します！")
        resize_image(get_random_image(src_files), conf["res_width"], conf["res_height"])
    
    print("処理が完了しました！")
    
    try:
        if len(game_executable) > 0:
            subprocess.Popen(game_executable)
    except FileNotFoundError:
        print("ゲームの実行ファイルが見つかりませんでした。パスを確認してください。")
    
    sys.exit()

if __name__ == "__main__":
    main()
