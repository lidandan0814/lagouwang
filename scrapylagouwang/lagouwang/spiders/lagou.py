# -*- coding: utf-8 -*-
import scrapy
from lagouwang.items import LagouItem


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/']

    def parse(self, response):
        jobs = response.css('.item_con_list li')
        for job in jobs:
            item = LagouItem()
            item['岗位名称'] = job.css('.position .p_top .position_link h3::text').extract_first()
            item['工作地点'] = job.css('.position_link .add em::text').extract_first()
            item['发布时间'] = job.css('.p_top .format-time::text').extract_first()
            item['薪资范围'] = job.css('.p_bot .li_b_l span::text').extract_first()
            item['工作经验'] = job.css('.position .p_bot .li_b_l::text').extract()[-1].split('/')[0].strip()
            item['学历要求'] = job.css('.position .p_bot .li_b_l::text').extract()[-1].split('/')[-1].strip()
            item['公司名称'] = job.css('.company_name a::text').extract_first().strip()
            item['所属行业'] = job.css('.company .industry::text').extract_first().split('/')[0].strip()
            item['融资阶段'] = job.css('.company .industry::text').extract_first().split('/')[-2]
            item['公司规模'] = job.css('.company .industry::text').extract_first().split('/')[-1]
            item['职位诱惑'] = job.css('.list_item_bot .li_b_r::text').extract_first()
            item['关键字'] = " ".join(job.css('.list_item_bot .li_b_l span::text').extract()).strip()
            yield item



        next = response.css('.pager_container a:last-child::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
