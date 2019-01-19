import requests
import json


class DoubanSpider:
    def __init__(self):
        self.url_temp_list =[ 
                              {
                                "url_temp":"https://cgi.datamore.qq.com/datamore/smobac/team/games?page={}&page_size=5&start_date=2018-10-20&end_date=2019-01-18&sort_field=game_time&sort_dir=desc&season_id=all&op_team_id=all&team_id=26&export=0&acctype=qq"
                                # ,"country":"UK"
                            }
                            # ,{
                            #     "url_temp":"https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start={}"
                            #     "country":"日本动漫"
                            # }
                            ]
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36"}

    def paral_url(self,url):  # 发送请求，获取响应
        response = requests.get(url,headers=self.headers) 
        return response.content.decode()


    def get_content_list(self,json_str):  # 提取数据
        dict_ret = json.loads(json_str)
        # content_list = dict_ret["data"]
        return dict_ret


    def save_content_list(self,content_list):  # 保存
        with open("wangzhe.txt","a") as f:
            for content in content_list:
                # content["country"]=country
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")


    def run(self):
        for url_temp in self.url_temp_list:
            num = 0
            while True:
                # 1.start_url
                url = url_temp["url_temp"].format(num)
                # 2.发送请求，获取响应
                json_str = self.paral_url(url)
                # 3.提取数据
                content_list = self.get_content_list(json_str)
                # 4.保存
                self.save_content_list(content_list)
                # 5.构造下一页的url，进入循环
                # print("----------")
                # print(content_list)
                # print("---------")
                if len(content_list)<10:
                    break
                num +=1


if __name__ == "__main__":
    douban_spider = DoubanSpider()
    douban_spider.run()