### **Commonly Used Port Numbers**

|**Port Number**|**Protocol**|**Usage**|
|---|---|---|
|**20, 21**|FTP|File Transfer Protocol|
|**22**|SSH|Secure Shell for remote login|
|**23**|Telnet|Unsecured remote login|
|**25**|SMTP|Sending emails|
|**53**|DNS|Domain Name System queries|
|**80**|HTTP|Web traffic (insecure)|
|**110**|POP3|Receiving emails|
|**119**|NNTP|Network News Transfer Protocol|
|**123**|NTP|Network Time Protocol|
|**143**|IMAP|Internet Message Access Protocol|
|**161, 162**|SNMP|Simple Network Management Protocol|
|**389**|LDAP|Lightweight Directory Access Protocol|
|**443**|HTTPS|Secure web traffic (SSL/TLS)|
|**465**|SMTPS|Secure SMTP for sending emails|
|**514**|Syslog|Logging protocol|
|**993**|IMAPS|Secure IMAP for email retrieval|
|**995**|POP3S|Secure POP3|

### **Development & Database Ports**

|**Port Number**|**Service**|**Usage**|
|---|---|---|
|**3306**|MySQL|MySQL Database|
|**5432**|PostgreSQL|PostgreSQL Database|
|**27017**|MongoDB|MongoDB Database|
|**6379**|Redis|Redis Database|
|**8080**|HTTP Alternate|Common for local web development|
|**8443**|HTTPS Alternate|Secure local web traffic|
|**9200**|Elasticsearch|Search Engine Database|

### **Application & Cloud Services**

|**Port Number**|**Service**|**Usage**|
|---|---|---|
|**3389**|RDP|Remote Desktop Protocol|
|**5985, 5986**|WinRM|Windows Remote Management|
|**8888**|Jupyter Notebook|Python development|
|**9090**|Prometheus|Monitoring System|

### **HDFS (Hadoop Distributed File System)**

- **NameNode**: `50070` (Web UI), `8020` (IPC)
- **Secondary NameNode**: `50090` (Web UI)
- **DataNode**: `50075` (Web UI), `9866` (Data Transfer)

### **YARN (Yet Another Resource Negotiator)**

- **ResourceManager**: `8088` (Web UI), `8032` (IPC)
- **NodeManager**: `8042` (Web UI)
- **JobHistory Server**: `19888` (Web UI)

### **MapReduce**

- **JobTracker (deprecated in YARN)**: `50030`
- **TaskTracker (deprecated in YARN)**: `50060`

### **Other Services**

- **ZooKeeper**: `2181` (Client connection)

Let me know if you need more details! 🚀