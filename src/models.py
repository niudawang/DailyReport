import enums
import json


class UserInfo:
    def __init__(self, username: str, nickname: str, platform: enums.PlatformType, date, followCount, fansCount,
                 likeCount, videoCount) -> None:
        self.username = username
        self.nickname = nickname
        self.platform = platform
        self.date = date,
        self.followCount = followCount
        self.fansCount = fansCount
        self.likeCount = likeCount
        self.videoCount = videoCount

    def toString1(self):
        result = """账号：{0}
关注数量：{1}
粉丝数量：{2}
点赞数量：{3}
视频数量：{4}
""".format(self.nickname, self.followCount, self.fansCount, self.likeCount, self.videoCount)
        return result

    def toString2(self, yesterdayFollow, yseterdatFans, yesterdayLike, yesterdayVideo):
        reslut = self.toString1()
        reslut += """关注数量变化：{0}
        粉丝数量变化：{1}
        点赞数量变化：{2}
        视频数量变化：{3}
        
        """.format(str(self.followCount - yesterdayFollow), str(self.fansCount - yseterdatFans),
                   str(self.likeCount - yesterdayLike),
                   str(self.videoCount - yesterdayVideo))
        return reslut

    def to_dict(self, yesterdayFollow=None, yesterdayFans=None, yesterdayLikes=None, yesterdayVideos=None):
        result = {
            "username": self.username,
            "nickname": self.nickname,
            "platform": self.platform.name,
            "date": self.date,
            "followCount": self.followCount,
            "fansCount": self.fansCount,
            "likeCount": self.likeCount,
            "videoCount": self.videoCount
        }

        if yesterdayFollow is not None:
            result["yesterdayFollow"] = yesterdayFollow
            result["yesterdayFans"] = yesterdayFans
            result["yesterdayLikes"] = yesterdayLikes
            result["yesterdayVideos"] = yesterdayVideos

        return result

    def to_json(self, yesterdayFollow=None, yesterdayFans=None, yesterdayLikes=None, yesterdayVideos=None):
        data = self.to_dict(yesterdayFollow, yesterdayFans, yesterdayLikes, yesterdayVideos)
        return json.dumps(data)
