import scrapy
import sqlite3


class CraigslistSpider(scrapy.Spider):
    name = "crag"
    start_urls = [
        "https://seattle.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=217&nearbyArea=466&nearbyArea=9&nearbyArea=461&nearbyArea=325&nearbyArea=246"
    ]

    def __init__(self):
        self.conn = sqlite3.connect("crag.db")
        self.c = self.conn.cursor()

        # Create table
        self.c.execute(
            """CREATE TABLE if not exists crag
                    (id int not null primary key, title text, ccs int, description text, price real, year int, location text, latitude text, longitude text, post_date text, remove_date text, miles int, model text, vin text, title_status text, condition text)"""
        )

        # Save (commit) the changes
        self.conn.commit()

    def parse(self, response):
        for title in response.css("a.result-title"):
            yield response.follow(title, self.parse_bike)

        # for next_page in response.css('div.search-legend:nth-child(3) > div:nth-child(3) > span:nth-child(2) > a:nth-child(6)'):
        #     yield response.follow(next_page, self.parse)

    def parse_bike(self, response):
        post_id = int(
            response.css(".postinginfos p:first-child::text").get().strip().split()[-1]
        )
        title = response.css("#titletextonly::text").get().strip()
        description = "\n".join(
            response.xpath('//*[@id="postingbody"]/*/text()').getall()
        ).strip()
        if description == "":
            description = (
                response.xpath('//*[@id="postingbody"]/text()[2]').get().strip()
            )

        ccs = response.xpath(
            "//span[contains(text(), 'engine displacement')]/b/text()"
        ).get()
        if ccs is not None:
            ccs = int(ccs.split()[-1])
        price = response.css("span.price::text").get()
        model = response.xpath(
            "/html/body/section/section/section/div[1]/p[1]/span/b/text()"
        ).get()
        if model is not None:
            model = model.strip()

        try:
            year = int(model.split()[0])
            model = " ".join(model.split()[1:])
        except:
            try:
                year = int(title.split()[0])
            except:
                year = None

        location = response.css(".postingtitletext small::text").get()
        if location is not None:
            location = location[2 : (len(location) - 1)]
        latitude = response.xpath('//*[@id="map"]/@data-latitude').get()
        longitude = response.xpath('//*[@id="map"]/@data-longitude').get()
        post_date = response.xpath(
            "/html/body/section/section/header/div[2]/p[1]/time/@datetime"
        ).get()
        # remove_date =

        miles = response.xpath("//span[contains(text(), 'odometer')]/b/text()").get()
        if miles is not None:
            miles = miles.split()[-1]

        vin = response.xpath("//span[contains(text(), 'VIN')]/b/text()").get()
        if vin is not None:
            vin = vin.split()[-1]

        condition = response.xpath(
            "//span[contains(text(), 'condition')]/b/text()"
        ).get()
        if condition is not None:
            condition = condition.split()[-1]

        title_status = response.xpath(
            "//span[contains(text(), 'title status')]/b/text()"
        ).get()
        if title_status is not None:
            title_status = title_status.split()[-1]

        data = [
            post_id,
            title,
            ccs,
            description,
            price,
            year,
            location,
            latitude,
            longitude,
            post_date,
            None,
            miles,
            model,
            vin,
            title_status,
            condition,
        ]

        self.c.execute(
            """
        INSERT INTO crag
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
            # on conflict update
            # set
            #     title=excluded.title,
            #     ccs=excluded.ccs,
            #     description=excluded.description,
            #     price=excluded.price,
            #     year=excluded.year,
            #     location=excluded.location,
            #     latitude=excluded.latitude,
            #     longitude=excluded.longitude,
            #     post_date=excluded.post_date,
            #     remove_date=excluded.remove_date,
            #     miles=excluded.miles,
            #     model=excluded.model,
            #     vin=excluded.vin,
            #     condition=excluded.condition,
            #     title_status=excluded.title_status
            ,
            data,
        )
        self.conn.commit()

        yield {"item": data}
