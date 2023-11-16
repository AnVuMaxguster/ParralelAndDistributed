# Note stuff
Giải thuật xử lý song song và phân bố - NT538.O11.MMCL

* RULES:
  1) Mỗi người chia **1 branch làm việc của mình** ( tên tùy thích ), code chính thức được **merge** vào **branch main**. 
  2) Commit code theo structure như sau:
     |- **Lecture n** ( folder )
           |- **Tên bài toán** ( folder )
                  |- ( code files )
  3) ...
     
* GIT BASH COMMANDS:
  ( Ae có thể note đóng góp vào đây các cmd Git Bash thông dụng để tiện ghi nhớ, edit thẳng vào Readme này của **branch main** )


-BAO



Clone from an existing repo with:   

git clone “repo url”

git remote add origin https://github.com/....	- use to link local folder to a remote repo

Status:


git status - check files status locally

Commit:


Cd to the local folder need to be commited
Git Add .
Git Commit -m “{your message}”
Git push

Pull data from repo:


Git pull


Branch:


Git fetch	- up-to-date with remote repo
Git checkout -b {local branch name }     -  only -b if local branch has not been created, use to change to/create a new local branch

Git branch --set-upstream-to=origin/{repoBranchName} {localbranch name}  - use to connect local branch to track repo branch

##SUBMITION_KEY##


    AEpHomGqxIZfGdnPnASL+d2JEqTlNHddxBQDxT195yvKOwWJSw==

# Hadoop environment setup for worker nodes

Để tối ưu power tính toán, mình sẽ triển khai cluster với **3 workers** luôn. Với 1 máy vừa làm worker vừa làm master.
- An ( Master + Worker 0 )
- Duy ( Worker 1 )
- Bảo ( Worker 2 )  


## Cài đặt Ubuntu dual boot với Windows
**Cần**:
- USB ( 20GB+ )
- Phần mềm Rufus
- Ubuntu image (.iso): mình thống nhất dùng Ubuntu Desktop 20.04 LTS. Tải file .iso [tại đây](https://releases.ubuntu.com/focal/) 
  ( Nếu có sẵn file .iso rồi thì không cần tải )

[Video](https://www.youtube.com/watch?v=-iSAyiicyQY) hướng dẫn. Thích cài theo hướng dẫn khác cũng được. Cẩn thận khi cài không sẽ mất Windows.

Khi setup Ubuntu tới đoạn cần cung cấp **Full name**, **Username**, **Machine name**. Cần đặt **ĐÚNG** theo như mô tả dưới đây nha:
- Full name: tùy thích.
- Username: group1
- Machine name: hadoop-worker1 ( Duy ), hadoop-worker2 ( Bảo )

Lý do là vì trong Hadoop máy master cần SSH tới workers để quản lý, phân công, ... Mà khi master nó SSH nó sẽ tự động SSH bằng username của chính nó đến các máy workers. Vì vậy 3 máy cần cài Hadoop với username như nhau để không lỗi.

Mặc dù hoàn toàn có thể tạo 1 user group1 riêng sau, nhưng mà làm tại đây luôn cho nhanh.

Machine name đặt vậy để dễ phân biệt thôi.
  

## Tải, cài đặt và configure môi trường Hadoop trên worker machine.
*Vì cả 2 máy ( Duy & Bảo ) đều đóng vai trò Worker nên đều thao tác phần này giống nhau.*

Bắt đầu tại thư mục home ( ~ ).

## Cài đặt các packages cần thiết
Update:
```bash
sudo apt update && sudo apt upgrade -y
```

Cài JDK:
```bash
sudo apt install default-jdk default-jre -y
```

Cài SSH service:
```bash
sudo apt install openssh-server openssh-client -y
```

Tải Hadoop & giải nén:
```bash
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xvzf hadoop-3.3.6.tar.gz
```

Chuyển Hadoop đến /usr/local:
```bash
sudo mv hadoop-3.3.4 /usr/local/hadoop
```

Tạo thư mục chứa logs & phân quyền sở hữu:
```bash
sudo mkdir /usr/local/hadoop/logs
sudo chown -R group1:group1 /usr/local/hadoop
```


### Thiết lập biến môi trường

Mở file **.bashsrc**:
```bash
sudo nano ~/.bashrc
```

Đi đến cuối file bằng tổ hợp `Alt+/`, sau đó paste đống này vào:
```bash
export HADOOP_HOME=/usr/local/hadoop

export HADOOP_INSTALL=$HADOOP_HOME

export HADOOP_MAPRED_HOME=$HADOOP_HOME

export HADOOP_COMMON_HOME=$HADOOP_HOME

export HADOOP_HDFS_HOME=$HADOOP_HOME

export YARN_HOME=$HADOOP_HOME

export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native

export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin

export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
```
**Save & exit nano**: `Ctrl+x+Enter`

Áp dụng thay đổi:
```bash
source ~/.bashrc
```

Mở file **hadoop-env.sh**:
```bash
sudo nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh
```
Đi đến cuối file bằng tổ hợp `Alt+/`, sau đó paste đống này vào:
```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

export HADOOP_CLASSPATH+=" $HADOOP_HOME/lib/*.jar"
```
Save & exit.

Kiểm tra:
```bash
hadoop version
```
Output in ra "Hadoop version 3.3.6 ..." là được.


### Configure tùm lum la

Mở file **core-site.xml**:
```bash
sudo nano $HADOOP_HOME/etc/hadoop/core-site.xml
```
Đi đến cuối file bằng tổ hợp `Alt+/`, sau đó paste đống này vào giữa cặp `<configuration></configuration>`:
```bash
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://master:9000</value>
    </property>
```
Save & exit.

Tạo thư mục chứa tài nguyên tính toán & phân quyền sở hữu:
```bash
sudo mkdir -p /home/group1/hdfs/datanode
sudo chown -R group1:group1 /home/group1/hdfs
```


Mở file **hdfs-site.xml**:
```bash
sudo nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```
Đi đến cuối file bằng tổ hợp `Alt+/`, sau đó paste đống này vào giữa cặp `<configuration></configuration>`:
```bash
      <property>
          <name>dfs.datanode.data.dir</name>
          <value>/home/group1/hdfs/datanode</value>
      </property>
```
Save & exit.


Mở file **mapred-site.xml**:
```bash
sudo nano $HADOOP_HOME/etc/hadoop/mapred-site.xml
```
Đi đến cuối file bằng tổ hợp `Alt+/`, sau đó paste đống này vào giữa cặp `<configuration></configuration>`:
```bash
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
```
Save & exit.


Mở file **yarn-site.xml**:
```bash
sudo nano $HADOOP_HOME/etc/hadoop/yarn-site.xml
```
Đi đến cuối file bằng tổ hợp `Alt+/`, sau đó paste đống này vào giữa cặp `<configuration></configuration>`:
```bash
     <property>
         <name>yarn.nodemanager.aux-services</name>
         <value>mapreduce_shuffle</value>
     </property>
     <property>
         <name>yarn.nodemanager.auxservices.mapreduce.shuffle.class</name>
         <value>org.apache.hadoop.mapred.ShuffleHandler</value>
     </property>
     <property>
         <name>yarn.resourcemanager.hostname</name>
         <value>master</value>
     </property>
     <property>
         <name>yarn.resourcemanager.address</name>
         <value>master:8032</value>
     </property>
```
Save & exit.



**XONG ! ĐẦY ĐỦ CHO MÁY WORKER ĐỂ CHẠY ĐƯỢC TRONG CLUSER**



## Khởi động cluster.
Phần này cần cả 3 máy cùng kết nối chung 1 mạng LAN. 

## BONUS.
```bash
sudo nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```
Đi đến cuối file bằng tổ hợp `Alt+/`, sau đó paste đống này vào:
```bash
      <property>
          <name>dfs.replication</name>
          <value>3</value>
      </property>
```

```bash
sudo nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```
Đi đến cuối file bằng tổ hợp `Alt+/`, sau đó paste đống này vào:
```bash
      <property>
          <name>dfs.replication</name>
          <value>3</value>
      </property>
```

```bash
sudo nano $HADOOP_HOME/etc/hadoop/yarn-site.xml
```
Xoa cap <property> cuoi cung

```bash
sudo nano $HADOOP_HOME/etc/hadoop/mapred-site.xml
```
Đi đến cuối file bằng tổ hợp `Alt+/`, sau đó paste đống này vào:
```bash
 <property>
  <name>yarn.app.mapreduce.am.env</name>
  <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
 </property>
 <property>
  <name>mapreduce.map.env</name>
  <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
 </property>
 <property>
  <name>mapreduce.reduce.env</name>
  <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
 </property>
```
