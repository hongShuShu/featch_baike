# !/usr/bin/evn python3
# coding:utf-8
#
# 视频地址 http://www.imooc.com/video/10674

from featch_baike import url_manger, html_downloader, html_parser, html_outputer

class SpiderMain(object):

    def __init__(self):
        self.urls = url_manger.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.Html_Parser()
        self.outputer = html_outputer.HtmlOutputer()

    # 爬虫的调度程序
    def craw(self, root_url):
        count = 1
        # 待爬取的url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                # 打印次数和RUL
                print('爬取 %d : %s' % (count, new_url))
                html_cont = self.downloader.downloader(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将url添加进url管理器
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                count += 1
                if count == 10:
                    break
            except Exception as e:
                print(e)
        self.outputer.output_html()

if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
