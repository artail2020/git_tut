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

# 2021年の祝日を確認
result: list[tuple[date, str]] = jpholiday.year_holidays(2021)
logger.debug(f"取得した祝日は{result} です")
print(f"取得した祝日は {result} です")
