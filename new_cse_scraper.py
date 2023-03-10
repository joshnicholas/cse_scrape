#%%

import requests

import datetime 
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
today = utc_now.astimezone(pytz.timezone("Asia/Colombo"))


today_stem = today.strftime('%Y%m%d')
today = today.strftime('%Y-%m-%d')


#%%


import requests

cookies = {
    # 'AWSALB': 'VYHV7fnR3Hkt1wnhVCNDRHq7on7JvsSpPwkO2GYFwQE3JAOp0u1l+31JP1cFQSCYITavRpyLX7WVFhzJi2w6xdQqMi2tEwPR/hGbN6rhLiXw73QZzuSrpJimwKQg',
    # 'AWSALBCORS': 'VYHV7fnR3Hkt1wnhVCNDRHq7on7JvsSpPwkO2GYFwQE3JAOp0u1l+31JP1cFQSCYITavRpyLX7WVFhzJi2w6xdQqMi2tEwPR/hGbN6rhLiXw73QZzuSrpJimwKQg',
    # '_ga': 'GA1.2.618747044.1678063884',
    # '_fbp': 'fb.1.1678063886300.1902614845',
    # '_gid': 'GA1.2.23049639.1678418700',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Referer': 'https://www.cse.lk/pages/trade-summary/trade-summary.component.html',
    'Origin': 'https://www.cse.lk',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': 'AWSALB=VYHV7fnR3Hkt1wnhVCNDRHq7on7JvsSpPwkO2GYFwQE3JAOp0u1l+31JP1cFQSCYITavRpyLX7WVFhzJi2w6xdQqMi2tEwPR/hGbN6rhLiXw73QZzuSrpJimwKQg; AWSALBCORS=VYHV7fnR3Hkt1wnhVCNDRHq7on7JvsSpPwkO2GYFwQE3JAOp0u1l+31JP1cFQSCYITavRpyLX7WVFhzJi2w6xdQqMi2tEwPR/hGbN6rhLiXw73QZzuSrpJimwKQg; _ga=GA1.2.618747044.1678063884; _fbp=fb.1.1678063886300.1902614845; _gid=GA1.2.23049639.1678418700',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'headers': {
        'normalizedNames': {},
        'lazyUpdate': None,
    },
}

r = requests.post('https://www.cse.lk/api/tradeSummary', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"headers":{"normalizedNames":{},"lazyUpdate":null}}'
#response = requests.post('https://www.cse.lk/api/tradeSummary', cookies=cookies, headers=headers, data=data)


#%%

print(r.text)
print(r.status_code)
# %%
