import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
import telepot
from URLsource import *
from utils import *

#### 엔진 가동 ####

# 1. URL 별 데이터 수집

urls = [KOSPI, KOSDAQ, KPI200, USDKRW, EURKRW, JPYKRW, CNYKRW, GBPKRW, HKDKRW, CHFKRW, IRR_CD91, IRR_CALL, IRR_GOVT_3Y,IRR_CORP_3Y,
        DJI, SPX, IXIC, PHIL, DAX30, CAC40, FTSE100, FTSEMIB, RTSI, SHS, HSI, NI225, BSE30, GBPUSD, EURUSD, USDJPY, USDCNY, WTI,
        OIL_DU, GOLD, COPPER, CORN, BDI, FX_USDX]

url = "https://kr.investing.com/portfolio/?portfolioID=NzE3bW4xYjY0Z29mMGEzMA%3D%3D"

collect_data(url)

test
'''
    # 스케줄러에 URL별로 수집 시간을 등록
    schedule.every().day.at("10:00").do(collect_data, url)

# 2. 수집된 데이터 엑셀 시트화

# 3. 엑셀 시트에서 필요 데이터 수집 및 글 작성

# 4. 가공된 데이터 텔레그램 전송

# 5. 반복 진행

while True:
    schedule.run_pending()
    time.sleep(1)
'''