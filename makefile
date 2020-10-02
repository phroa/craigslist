install:
	install -b scrape-craigslist.service /etc/systemd/system
	install -b scrape-craigslist.timer /etc/systemd/system
	systemctl enable scrape-craigslist.timer