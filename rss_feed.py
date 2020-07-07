import feedparser


def feed_data():

	RSSFeed = feedparser.parse("https://www.upwork.com/ab/feed/jobs/rss?sort=recency&paging=0%3B10&api_params=1&q=&securityToken=2c2762298fe1b719a51741dbacb7d4f5c1e42965918fbea8d2bf1185644c8ab2907f418fe6b1763d5fca3a9f0e7b34d2047f95b56d12e525bc4ba998ae63f0ff&userUid=424312217100599296&orgUid=424312217104793601")

	feed_dict = {}

	for i in range(len(RSSFeed.entries)):
		feed_list = []
		feed_list.append(RSSFeed.entries[i].title)
		feed_list.append(RSSFeed.entries[i].link)
		feed_list.append(RSSFeed.entries[i].summary)
		published = RSSFeed.entries[i].published
		feed_list.append(published[:len(published)-6])
		feed_dict[i] = feed_list

	return feed_dict


if __name__=='__main__':
	feed_dict = feed_data()
