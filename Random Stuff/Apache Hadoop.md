### **1. HDFS (Hadoop Distributed File System) Commands**

#### **Start/Stop HDFS**

```bash
start-dfs.sh       # Start HDFS
stop-dfs.sh        # Stop HDFS
```

#### **File Operations**

```bash
hdfs dfs -ls /             # List files in HDFS root directory
hdfs dfs -mkdir /mydir     # Create a directory in HDFS
hdfs dfs -put localfile.txt /mydir/  # Upload a file to HDFS
hdfs dfs -get /mydir/localfile.txt . # Download a file from HDFS
hdfs dfs -rm /mydir/localfile.txt    # Delete a file in HDFS
hdfs dfs -rmdir /mydir      # Remove an empty directory in HDFS
hdfs dfs -du -h /           # Show disk usage in HDFS
hdfs dfs -chmod 777 /mydir  # Change permissions
hdfs dfs -chown user:group /mydir  # Change ownership
```

#### **HDFS Admin Commands**

```bash
hdfs dfsadmin -report      # Get HDFS cluster status
hdfs dfsadmin -safemode get  # Check safe mode status
hdfs dfsadmin -safemode leave  # Exit safe mode
```

---

### **2. YARN (Yet Another Resource Negotiator) Commands**

#### **Start/Stop YARN**

```bash
start-yarn.sh       # Start YARN
stop-yarn.sh        # Stop YARN
```

#### **YARN Application Management**

```bash
yarn application -list   # List running applications
yarn application -kill <app_id>   # Kill a running application
yarn node -list          # List active nodes
```

---

### **3. MapReduce Commands**

```bash
yarn jar /path/to/hadoop-mapreduce-examples.jar wordcount /input /output
```

_(Runs a WordCount example using MapReduce)_

```bash
mapred job -list         # List running MapReduce jobs
mapred job -kill <job_id>  # Kill a specific job
```

---

### **4. Hadoop Daemon Management**

```bash
jps   # List running Hadoop daemons
```

#### **Restart all Hadoop Services**

```bash
stop-all.sh
start-all.sh
```

---

These are some of the most commonly used Hadoop commands! Let me know if you need more. 🚀

To start Apache Hadoop in Linux and access its Web UI, follow these steps:

### **1. Start Hadoop Services**

Run the following commands in the Hadoop installation directory:

```bash
start-dfs.sh  # Start HDFS (Namenode, Datanode, Secondary Namenode)
start-yarn.sh # Start YARN (ResourceManager, NodeManager)
```

For single-node mode (if running standalone):

```bash
hadoop namenode -format  # Format HDFS (only required for first-time setup)
start-all.sh  # Starts both HDFS and YARN
```

### **2. Check Running Services**

To verify that Hadoop services are running:

```bash
jps
```

You should see services like `NameNode`, `DataNode`, `SecondaryNameNode`, `ResourceManager`, and `NodeManager`.

### **3. Access Hadoop Web UI**

- **HDFS Namenode UI** → [http://localhost:9870](http://localhost:9870)
- **YARN Resource Manager UI** → [http://localhost:8088](http://localhost:8088)

If Hadoop is installed on a different machine, replace `localhost` with the server's IP address.

Let me know if you need more details! 🚀