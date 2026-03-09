from logging import getLogger, FileHandler, DEBUG, ERROR, Formatter

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

# テスト関数を定義
def func(t: list[int]) -> list[int]:
    logger.debug(f"func関数が呼び出されました。引数t: {t}")
    t.append(999)
    logger.debug(f"func関数の結果: {t}")
    return t

x: list[int] = [1, 2, 3]
y: list[int] = func(x)

print(f"{x} {y}")
logger.info("プログラムが終了しました")
