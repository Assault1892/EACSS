# MARK: IMPORTS
from tomllib import load
import pathlib
import random
import shutil
import os
import sys
from PIL import Image

try:
    with open("config.toml", "rb") as conf_file:
        conf = load(conf_file)
except FileNotFoundError:
    print("config.tomlが見つかりません！")
    sys.exit(1)

# MARK: VARIABLES

SRC_DIR = conf["src_dir"]

# ソースディレクトリの画像ファイルをリスト化
SRC_FILES = list(
    pathlib.Path(SRC_DIR).glob("*.png")
)

ARGS = sys.argv

# MARK: FUNCTIONS


def get_random_image():
    # これいる？
    return SRC_FILES[random.randint(0, len(SRC_FILES) - 1)]


def check_source_dir():
    """
    _summary_
    パス自体の確認や、パスが存在するかどうか、画像ファイルが存在するかどうかの確認を行う
    Returns:
        bool : Trueの場合はソースディレクトリが存在し、使用可能。Falseの場合は存在しないか、何らかの理由で使用不可能。
    """
    # ソースディレクトリの設定確認
    if SRC_DIR == "":
        print("ソースディレクトリが設定されていません！")
        return False
    # ソースディレクトリの存在確認
    elif pathlib.Path(SRC_DIR).exists() is False:
        print("ソースディレクトリが存在しません！")
        return False
    elif len(SRC_FILES) == 0:
        print("ソースディレクトリに画像ファイルが存在しません！")
        return False
    else:
        return True


def check_splashscreen():
    """_summary_
    スプラッシュスクリーンのバックアップファイルが存在するかどうかの確認。
    Returns:
        bool : Trueの場合はバックアップファイルが存在する。Falseの場合は存在しない。
    """
    if pathlib.Path("./EasyAntiCheat/SplashScreen.png.orig").exists():
        print("バックアップファイルがすでに存在します！")
        return True
    else:
        print("オリジナルのファイルが存在しません。おそらく初回起動のようです！")
        return False


def backup_splashscreen(isSplashExist: bool):
    if isSplashExist is False:
        print("バックアップを作成します！")
        shutil.copy(
            "./EasyAntiCheat/SplashScreen.png",
            "./EasyAntiCheat/SplashScreen.png.orig"
        )
        print("バックアップが完了しました！")
    else:
        pass


def restore_splashscreen(isSplashExist: bool):
    if isSplashExist is True:
        print("バックアップから復元します！")
        shutil.copy(
            "./EasyAntiCheat/SplashScreen.png.orig",
            "./EasyAntiCheat/SplashScreen.png"
        )
        print("バックアップからの復元が完了しました！")
    else:
        print("バックアップファイルが存在しません！")
        pass

# MARK: MAIN FUNCTION


print(str(ARGS))


def main():
    print("# =========================================== #")
    print("# EasyAntiCheat Splash Screen Changer - EACSS #")
    print("# =========================================== #")

    if check_source_dir():
        pass
    else:
        print("config.tomlを確認してください！")
        sys.exit(1)

    # 起動引数を取得。restoreの場合はバックアップから復元のみ。
    if len(ARGS) > 1 and ARGS[1] == "restore":
        restore_splashscreen(check_splashscreen())
        sys.exit()
    # 起動引数が与えられていない (通常起動) か、restore以外の場合は通常動作。
    else:
        backup_splashscreen(check_splashscreen())
        # 画像選択
        print("ランダムな画像を選択します！")
        random_image = get_random_image()
        # 画像をリサイズ
        print("画像をリサイズします！")

        try:
            img = Image.open(random_image)
            (width, height) = conf["res_width"], conf["res_height"]
            img_resized = img.resize((width, height))
            # リサイズした画像を保存
            print("リサイズした画像を上書きします！")
            img_resized.save("./EasyAntiCheat/SplashScreen.png")
        except Exception as e:
            print("画像のリサイズに失敗しました！")
            print(e)
    print("処理が完了しました！")

# MARK: RUN GAME


if __name__ == "__main__":
    main()
    os.startfile("start_protected_game.exe")
    sys.exit()
