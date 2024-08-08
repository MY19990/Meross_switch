import logging
 
# ログの出力名を設定（1）
logger = logging.getLogger('LoggingTest')
 
# ログをコンソール出力するための設定（2）
sh = logging.StreamHandler()
logger.addHandler(sh)

#ログレベルを設定 - (30 < setLevel)なら出力！
logger.setLevel(30)

# log関数でログ出力処理（3）
logger.log(20, 'info')
logger.log(30, 'warning')
logger.log(100, 'test')


import logging
 
# ログの出力名を設定
logger = logging.getLogger('LoggingTest')
 
#ログレベルを設定 - (30 < setLevel)なら出力！
logger.setLevel(10)
 
# ログのコンソール出力の設定
sh = logging.StreamHandler()
logger.addHandler(sh)
 
# ログのファイル出力先を設定
fh = logging.FileHandler('test.log')
logger.addHandler(fh)
 
# ログの出力形式の設定
formatter = logging.Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
 
logger.log(20, 'info')
logger.log(30, 'warning')
logger.log(100, 'test')
 
logger.info('info')
logger.warning('warning')