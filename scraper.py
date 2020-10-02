import scrapy
import sqlite3


class CraigslistSpider(scrapy.Spider):
    name = "crag"
    start_urls = [
        "https://seattle.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=217&nearbyArea=233&nearbyArea=350&nearbyArea=322&nearbyArea=94&nearbyArea=324&nearbyArea=654&nearbyArea=655&nearbyArea=466&nearbyArea=321&nearbyArea=9&nearbyArea=368&nearbyArea=459&nearbyArea=232&nearbyArea=461&nearbyArea=95&nearbyArea=325&nearbyArea=246",
        "https://portland.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=233&nearbyArea=350&nearbyArea=94&nearbyArea=232&nearbyArea=2&nearbyArea=246",
        "https://milwaukee.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=1",
        "https://wyoming.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=657&nearbyArea=658&nearbyArea=424&nearbyArea=287&nearbyArea=448&nearbyArea=351",
        "https://charlestonwv.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=438&nearbyArea=674&nearbyArea=442&nearbyArea=441&nearbyArea=632&nearbyArea=194",
        "https://spokane.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=1",
        "https://richmond.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=290&nearbyArea=457&nearbyArea=366&nearbyArea=48&nearbyArea=556&nearbyArea=10",
        "https://vermont.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=59&nearbyArea=686&nearbyArea=198&nearbyArea=338&nearbyArea=683&nearbyArea=247",
        "https://saltlakecity.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=424&nearbyArea=652&nearbyArea=448&nearbyArea=351&nearbyArea=292&nearbyArea=469",
        "https://sanantonio.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=15&nearbyArea=265&nearbyArea=647&nearbyArea=327&nearbyArea=449&nearbyArea=564",
        "https://houston.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=264&nearbyArea=326&nearbyArea=645&nearbyArea=470&nearbyArea=284&nearbyArea=564",
        "https://dallas.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=645&nearbyArea=327&nearbyArea=649&nearbyArea=308&nearbyArea=270&nearbyArea=365",
        "https://austin.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=326&nearbyArea=327&nearbyArea=53&nearbyArea=449&nearbyArea=564&nearbyArea=270",
        "https://nashville.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=342&nearbyArea=465&nearbyArea=670&nearbyArea=560&nearbyArea=231&nearbyArea=377",
        "https://sd.craigslist.org/search/mca?bundleDuplicates=1&searchNearby=2&nearbyArea=666&nearbyArea=682&nearbyArea=681&nearbyArea=341&nearbyArea=679&nearbyArea=665",
        "https://myrtlebeach.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=128&nearbyArea=101&nearbyArea=273&nearbyArea=464&nearbyArea=634&nearbyArea=274",
        "https://providence.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=4&nearbyArea=239&nearbyArea=281&nearbyArea=44&nearbyArea=378&nearbyArea=240",
        "https://philadelphia.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=349&nearbyArea=193&nearbyArea=279&nearbyArea=167&nearbyArea=278&nearbyArea=286",
        "https://oklahomacity.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=422&nearbyArea=650&nearbyArea=433&nearbyArea=649&nearbyArea=70&nearbyArea=365",
        "https://cleveland.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=251&nearbyArea=700&nearbyArea=436&nearbyArea=573&nearbyArea=703&nearbyArea=252",
        "https://nd.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=666&nearbyArea=192&nearbyArea=435&nearbyArea=667&nearbyArea=682&nearbyArea=681",
        "https://nh.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=4&nearbyArea=686&nearbyArea=338&nearbyArea=93&nearbyArea=173&nearbyArea=240",
        "https://newyork.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=349&nearbyArea=249&nearbyArea=561&nearbyArea=250&nearbyArea=168&nearbyArea=170",
        "https://albuquerque.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=653&nearbyArea=568&nearbyArea=334&nearbyArea=420&nearbyArea=218&nearbyArea=651",
        "https://cnj.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=561&nearbyArea=167&nearbyArea=3&nearbyArea=170&nearbyArea=17&nearbyArea=286",
        "https://lasvegas.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=1",
        "https://omaha.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=98&nearbyArea=693&nearbyArea=432&nearbyArea=282&nearbyArea=341&nearbyArea=694",
        "https://raleigh.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=367&nearbyArea=335&nearbyArea=273&nearbyArea=61&nearbyArea=634&nearbyArea=272",
        "https://billings.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=658&nearbyArea=661&nearbyArea=192&nearbyArea=660&nearbyArea=659&nearbyArea=197",
        "https://stlouis.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=222&nearbyArea=569&nearbyArea=699&nearbyArea=345&nearbyArea=225&nearbyArea=697",
        "https://memphis.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=560&nearbyArea=558&nearbyArea=425&nearbyArea=100&nearbyArea=375&nearbyArea=566",
        "https://minneapolis.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=664&nearbyArea=242&nearbyArea=421&nearbyArea=692&nearbyArea=316&nearbyArea=369",
        "https://detroit.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=172&nearbyArea=259&nearbyArea=629&nearbyArea=555&nearbyArea=573&nearbyArea=204",
        "https://worcester.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=4&nearbyArea=281&nearbyArea=44&nearbyArea=38&nearbyArea=378&nearbyArea=173",
        "https://baltimore.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=460&nearbyArea=328&nearbyArea=633&nearbyArea=279&nearbyArea=10&nearbyArea=357",
        "https://maine.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=4&nearbyArea=239&nearbyArea=198&nearbyArea=338&nearbyArea=93&nearbyArea=240",
        "https://neworleans.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=199&nearbyArea=230&nearbyArea=374&nearbyArea=643&nearbyArea=283&nearbyArea=200",
        "https://louisville.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=229&nearbyArea=342&nearbyArea=35&nearbyArea=227&nearbyArea=133&nearbyArea=673",
        "https://kansascity.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=222&nearbyArea=695&nearbyArea=347&nearbyArea=428&nearbyArea=694&nearbyArea=280",
        "https://indianapolis.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=1",
        "https://chicago.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=552&nearbyArea=698&nearbyArea=47&nearbyArea=223&nearbyArea=228&nearbyArea=572",
        "https://boise.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=424&nearbyArea=322&nearbyArea=652&nearbyArea=654&nearbyArea=368&nearbyArea=469",
        "https://honolulu.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1",
        "https://micronesia.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1",
        "https://atlanta.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=258&nearbyArea=372&nearbyArea=343&nearbyArea=559&nearbyArea=257&nearbyArea=636",
        "https://orlando.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=238&nearbyArea=639&nearbyArea=376&nearbyArea=333&nearbyArea=331&nearbyArea=37",
        "https://miami.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=330&nearbyArea=125&nearbyArea=639&nearbyArea=376&nearbyArea=237&nearbyArea=332",
        "https://delaware.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=460&nearbyArea=34&nearbyArea=328&nearbyArea=279&nearbyArea=17&nearbyArea=286",
        "https://washingtondc.craigslist.org/search/mca?bundleDuplicates=1&searchNearby=2&nearbyArea=460&nearbyArea=34&nearbyArea=328&nearbyArea=633&nearbyArea=457&nearbyArea=556",
        "https://hartford.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=281&nearbyArea=249&nearbyArea=168&nearbyArea=354&nearbyArea=173&nearbyArea=240",
        "https://denver.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=319&nearbyArea=210&nearbyArea=713&nearbyArea=287&nearbyArea=288&nearbyArea=315",
        "https://phoenix.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=244&nearbyArea=419&nearbyArea=651&nearbyArea=468&nearbyArea=57&nearbyArea=370",
        "https://anchorage.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=677&nearbyArea=678",
        "https://huntsville.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=127&nearbyArea=220&nearbyArea=560&nearbyArea=559&nearbyArea=32&nearbyArea=636",
        "https://sfbay.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=373&nearbyArea=285&nearbyArea=96&nearbyArea=102&nearbyArea=12&nearbyArea=97",
        "https://sandiego.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=455&nearbyArea=104&nearbyArea=7&nearbyArea=103&nearbyArea=209&nearbyArea=370",
        "https://sacramento.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=187&nearbyArea=373&nearbyArea=96&nearbyArea=1&nearbyArea=97&nearbyArea=456",
        "https://orangecounty.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=104&nearbyArea=7&nearbyArea=209&nearbyArea=8&nearbyArea=62&nearbyArea=208",
        "https://losangeles.craigslist.org/search/mca?hasPic=1&bundleDuplicates=1&searchNearby=2&nearbyArea=63&nearbyArea=104&nearbyArea=103&nearbyArea=209&nearbyArea=62&nearbyArea=208"
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
        try:
            self.c.execute(
                """
            INSERT INTO crag
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                ,
                data,
            )
            self.conn.commit()
        except:
            pass

        yield {"item": data}
