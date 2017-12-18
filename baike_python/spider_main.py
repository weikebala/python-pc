# coding:utf-8

import html_downloader, html_parser, html_outputer, url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.download = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutPuter()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_con = self.download.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_con)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 50:
                    break
                count = count + 1
            except:
                print 'craw failed'
        self.outputer.output_html()

    def test(self):
        count = 1
        initcoumt = 98

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/%E9%AD%8F%E5%A8%9C/7176911"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
