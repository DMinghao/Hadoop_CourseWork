# Hadoop_CourseWork
 
## Usage 

### Dependency 
```
Java    >= 1.8      # java 15 is recommended 
Python  >= 3.5      # python 3.8 is recommended 
Hadoop  == 2.7.1    # snapshot in util folder 
Spark   == 3.0.1
pySpark == 3.0.1
``` 
---
### Setup
- All projects must in their own folder 
- For MapReduce project: 
    - In each project there should contain: 
        - mapper.py for mapper
        - reducer.py for reducer 
        - *.dat or *.txt for test data
    - Test MapReduce project: 
        1. Open terminal and go to util folder 
            ```bash
            cd util
            ```
        2. Run test with follow command: 
            ```bash
            python mapReduceTest.py
            ```
            or
            ```bash
            python mapReduceTest.py {ProjectFolder} {DataFileName}
            ```
- For *Spark* project
    - Include following code if *Hadoop* is not installed: <div id="fixhadoop"/>
        ```python
        import os 
        os.environ['HADOOP_HOME'] = os.path.abspath(os.path.join(os.getcwd(), os.pardir)).replace('\\', '/')+'/util/hadoop-2.7.1'
        ```
    - Troubleshooting: 
        - If the following error has occurred while `SparkContext`: 
            ```console
            Py4JJavaError: An error occurred while calling None.org.apache.spark.api.java.JavaSparkContext.
            : java.net.BindException: Cannot assign requested address: bind: Service 'sparkDriver' failed after 16 retries (on a random free port)! Consider explicitly setting the appropriate binding address for the service 'sparkDriver' (for example spark.driver.bindAddress for SparkDriver) to the correct binding address.
                at java.base/sun.nio.ch.Net.bind0(Native Method)
                at java.base/sun.nio.ch.Net.bind(Net.java:550)
                at java.base/sun.nio.ch.ServerSocketChannelImpl.bind(ServerSocketChannelImpl.java:249)
                at io.netty.channel.socket.nio.NioServerSocketChannel.doBind(NioServerSocketChannel.java:134)
                ...
            ```
            Use the following code to set `SparkContext`: 
            ```python
            sc = None 
            # count = 0
            while sc is None: 
                try: 
                    sc = SparkContext.getOrCreate(SparkConf().setMaster("local"))
                except: 
                    pass
                    # print(f"tried {count} time", end='\r')
                    # count += 1 
            ```
        - If the following (or simpular) error has occurred while using `saveAsTextFile`: 
            ```console
            Py4JJavaError: An error occurred while calling o9614.saveAsTextFile.
            : org.apache.spark.SparkException: Job aborted.
                at org.apache.spark.internal.io.SparkHadoopWriter$.write(SparkHadoopWriter.scala:100)
                at org.apache.spark.rdd.PairRDDFunctions.$anonfun$saveAsHadoopDataset$1(PairRDDFunctions.scala:1090)
                at scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23)
                ...
            ```
            Hadoop is not installed in your machine, use [this](#fixhadoop) code. 

---