#### References

Key review before running big API queries:
- https://www.mediawiki.org/wiki/API:Etiquette

technical
- Time series templates
    - https://machinelearningmastery.com/autoregression-models-time-series-forecasting-python/
- API:RecentChanges
    - https://www.mediawiki.org/wiki/API:RecentChanges
    - https://www.mediawiki.org/w/api.php?action=help&modules=main#main/datatype/timestamp
- EventStream
    - https://stream.wikimedia.org/v2/stream/recentchange
    - https://codepen.io/ottomata/pen/VKNyEw/
    - https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams#When_not_to_use_EventStreams
    - https://stream.wikimedia.org/?doc#/streams/get_v2_streaam_recentchange
    - https://towardsdatascience.com/introduction-to-apache-kafka-with-wikipedias-eventstreams-service-d06d4628e8d9
    - https://github.com/wikimedia/mediawiki-event-schemas/blob/master/jsonschema/mediawiki/recentchange/current.yaml
- API: Categories
    - https://vcat.toolforge.org/render?wiki=enwiki&category=Butterflies
    - https://www.mediawiki.org/w/api.php?action=help&modules=query%2Bcategories
    - https://www.mediawiki.org/wiki/Manual:Categorylinks_table
    - https://stackoverflow.com/questions/17432254/wikipedia-category-hierarchy-from-dumps
    - https://stackoverflow.com/questions/27279649/how-to-build-wikipedia-category-hierarchy?noredirect=1&lq=1
    - https://kodingnotes.wordpress.com/2014/12/03/parsing-wikipedia-page-hierarchy/
- API: Revisions
    - https://www.mediawiki.org/wiki/API:Revisions
    - https://www.mediawiki.org/wiki/Manual:Revision_table
- Migrating MySQL dumps -> PostgreSQL
    - https://mariadb.com/kb/en/mysql-command-line-client/
    - https://mariadb.org/download/?t=repo-config&d=20.04+%22focal%22&v=10.3&r_m=ossplanet
    - FAILED https://mariadb.org/download/?t=repo-config&d=20.04+%22focal%22&v=10.3&r_m=blendbyte
    - https://askubuntu.com/questions/806738/mariadb-10-1-and-ubuntu-16-04-unable-to-set-password-for-the-mariadb-root-use
    - https://mariadb.com/docs/deploy/topologies/single-node/community-server-10-3/
    - MAYBE NOT THIS ONE https://computingforgeeks.com/install-mariadb-on-ubuntu-and-centos/
    - https://wiki.postgresql.org/wiki/Converting_from_other_Databases_to_PostgreSQL
    - https://ubuntu.com/server/docs/databases-mysql
    - https://datawookie.dev/blog/2021/03/resurrecting-a-mysql-database/
- Dumps
    - https://dumps.wikimedia.org/other/mediawiki_history/2021-10/enwiki/
    - https://wikitech.wikimedia.org/wiki/Analytics/Data_Lake/Edits/MediaWiki_history
    - https://dumps.wikimedia.org/other/analytics/
    - https://dumps.wikimedia.org/other/mediawiki_history/readme.html
- Look it up later
    - https://towardsdatascience.com/wikipedia-as-a-valuable-data-science-tool-6769991b43b7
- Research Ideas
    - https://meta.wikimedia.org/wiki/Research:Effects_of_collaboration_patterns_on_article_quality
    - https://www.sciencedirect.com/science/article/pii/S2212094721000475
- Research nexi
    - https://meta.wikimedia.org/wiki/Research:Index
    - https://meta.wikimedia.org/wiki/Research:Projects
    - https://research.wikimedia.org/projects.html                   **************
- Wikiprojects
    - https://stackoverflow.com/questions/54729496/how-to-get-wikipedia-data-of-wikiprojects
- Jawiki
    - 
alternative
- https://www.kaggle.com/c/wikichallenge

https://serverfault.com/questions/146525/how-can-i-speed-up-a-mysql-restore-from-a-dump-file 
https://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session

- cron
- nohup

- SQL
    - https://medium.com/analytics-vidhya/importing-data-from-a-mysql-database-into-pandas-data-frame-a06e392d27d7