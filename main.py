# MARK: IMPORTS
from tomllib import load
import pathlib
import random
import shutil
import sys
from PIL import Image

with open("config.toml", "rb") as conf_file:
    conf = load(conf_file)

# MARK: VARIABLES

SRC_DIR = conf["src_dir"]

# ソースディレクトリの画像ファイルをリスト化
SRC_FILES = list(
    pathlib.Path(SRC_DIR).glob("*.png")
)
# ソースファイルのリスト数を上限にランダムな整数を生成
SRC_RAND = random.randint(0, len(SRC_FILES) - 1)

ARGS = sys.argv

# MARK : FUNCTIONS


def get_random_image():
    # これいる？
    return SRC_FILES[SRC_RAND]


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

# MARK: MAIN


print("# =========================================== #")
print("# EasyAntiCheat Splash Screen Changer - EACSS #")
print("# =========================================== #")

# 起動引数を取得。restoreの場合はバックアップから復元のみ。
if len(ARGS) >= 2:
    if ARGS[1] == "restore":
        restore_splashscreen(check_splashscreen())
# 起動引数が与えられていない (通常起動) か、restore以外の場合は通常動作。
else:
    backup_splashscreen(check_splashscreen())
    # 画像選択
    print("ランダムな画像を選択します！")
    random_image = get_random_image()
    # 画像をリサイズ
    print("画像をリサイズします！")
    img = Image.open(random_image)
    (width, height) = conf["res_width"], conf["res_height"]
    img_resized = img.resize((width, height))
    # リサイズした画像を保存
    print("リサイズした画像を上書きします！")
    img_resized.save("./EasyAntiCheat/SplashScreen.png")

print("処理が完了しました！")
