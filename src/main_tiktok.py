import tiktok_utils
import weixin
import os
import config
import json

file_path = 'data.json'

if __name__ == "__main__":
    try:
        if config.user_config['switch_run']:
            tiktok_cookie = config.user_config['tiktok_cookie']
            wxpusher_token = config.user_config['wxpusher_token']
            wechat_uid = os.environ['WECHAT_UID']
            accounts = os.environ['TIKTOK_ACCOUNTS']

            data = None
            if os.path.exists(file_path):
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    print(data)
            else:
                print(f"The file {file_path} does not exist.")

            list = accounts.split(',')
            users = []
            result = ""
            for item in list:
                info = tiktok_utils.getUserInfo(item, tiktok_cookie)
                if info == None:
                    print("获取用户信息失败")
                    result += "用户信息丢失:"+item
                else:
                    users.append(info)
                    print(item)

                    yesterday = None
                    try:
                        if data is not None:
                            for tmpItem in data:
                                if tmpItem.get("username") == info.username:
                                    yesterday = tmpItem
                                    break
                    except Exception as err:
                        print('获取对比信息错误')
                        print(err)

                    if yesterday == None:
                        result += info.toString1()
                    else:
                        result += info.toString2(yesterday['followCount'], yesterday['fansCount'],
                                                yesterday['likeCount'], yesterday['videoCount'])

            weixin.wxpusher_send_by_webapi(
                result, "TikTok日报", wxpusher_token, wechat_uid)

            # 保存文件

            # 将结构体列表转换为字典列表
            user_dicts = [user.to_dict() for user in users]

            # 将字典列表转换为JSON字符串
            json_str = json.dumps(user_dicts)
            with open(file_path, 'w') as json_file:
                json.dump(user_dicts, json_file)
        else:
            print('本次不执行')
    except Exception as err:
        print("运行错误")
        print(err)
