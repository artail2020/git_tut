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
logger.debug("入力値は1000です")
logger.warning("ファイルの容量が200GBを超えました")
logger.error("ファイルが存在していません")
