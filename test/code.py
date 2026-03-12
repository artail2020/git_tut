from logging import getLogger, FileHandler, DEBUG, ERROR, Formatter
from datetime import date
import jpholiday

# formatter,logger設定
formatter = Formatter("[%(levelname)s] %(asctime)s - %(message)s (%(filename)s)")
logger = getLogger(__name__)

# DEBUGハンドラー設定
handler = FileHandler("./logs/log.txt", encoding="utf-8")
handler.setLevel(DEBUG)
handler.setFormatter(formatter)

# ERRORハンドラー設定
err_handler = FileHandler("./logs/error.txt", encoding="utf-8")
err_handler.setLevel(ERROR)
err_handler.setFormatter(formatter)

# loggerにハンドラーを追加
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.addHandler(err_handler)

# ログ出力
logger.info("プログラムが開始されました")

# 可変長引数の関数を定義
def func(x: int, **kwargs) -> None:
    logger.debug(f"引数{x}: {kwargs}で関数を実行")
    print(f"{x}")
    for k, v in kwargs.items():
        print(f"{k}: {v}")

func(1, name="斉藤", user_id=222)
func(2, item="牛乳", item_id=111, price=100)
