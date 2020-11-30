DROP TABLE IF EXISTS tweets_raw;
CREATE EXTERNAL TABLE tweets_raw (
  tweet_id int,
  airline string,
  text string
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS
INPUTFORMAT
'com.amazonaws.emr.s3select.hive.S3SelectableTextInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION '${INPUT}tweets/'
TBLPROPERTIES (
  "s3select.format" = "csv",
  "s3select.headerInfo" = "ignore"
);

DROP TABLE IF EXISTS dictionary;
CREATE EXTERNAL TABLE dictionary (
  word string,
  polarity string
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS
INPUTFORMAT
'com.amazonaws.emr.s3select.hive.S3SelectableTextInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION '${INPUT}dictionary/'
TBLPROPERTIES (
  "s3select.format" = "csv",
  "s3select.headerInfo" = "ignore"
);

drop view if exists l1;
create view l1 as select tweet_id, words from tweets_raw lateral view explode(sentences(lower(text))) dummy as words;
drop view if exists l2;
create view l2 as select tweet_id, word from l1 lateral view explode( words ) dummy as word;

drop view if exists l3;
create view l3 as select
  tweet_id,
  l2.word,
  case d.polarity
    when  'negative' then -1
    when 'positive' then 1
    else 0 end as polarity
from l2 left outer join dictionary d on l2.word = d.word;

DROP TABLE IF EXISTS tweets_sentiment;
create table tweets_sentiment stored as orc as select
  tweet_id,
  case
  when sum( polarity ) > 0 then 'positive'
  when sum( polarity ) < 0 then 'negative'
  else 'neutral' end as sentiment
from l3 group by tweet_id;

INSERT OVERWRITE DIRECTORY '${OUTPUT}' SELECT * FROM tweets_sentiment;