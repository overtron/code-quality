'''
Created on Apr 6, 2015

@author: nnair
'''

import re


DEFAULT_NAMES = [
    re.compile('^Abort( \d)*$'),
    re.compile('^Add a checksum( \d)*$'),
    re.compile('^Add constants( \d)*$'),
    re.compile('^Add sequence( \d)*$'),
    re.compile('^Add value fields changing sequence( \d)*$'),
    re.compile('^Add XML( \d)*$'),
    re.compile('^Aggregate Rows( \d)*$'),
    re.compile('^Agile( \d)*$'),
    re.compile('^Analytic Query( \d)*$'),
    re.compile('^Append streams( \d)*$'),
    re.compile('^ARFF Output( \d)*$'),
    re.compile('^Automatic Documentation Output( \d)*$'),
    re.compile('^Avro input( \d)*$'),
    re.compile('^Block this step until steps finish( \d)*$'),
    re.compile('^Blocking Step( \d)*$'),
    re.compile('^Bulk loading( \d)*$'),
    re.compile('^Calculator( \d)*$'),
    re.compile('^Call DB Procedure( \d)*$'),
    re.compile('^Cassandra input( \d)*$'),
    re.compile('^Cassandra output( \d)*$'),
    re.compile('^Change file encoding( \d)*$'),
    re.compile('^Check if a column exists( \d)*$'),
    re.compile('^Check if file is locked( \d)*$'),
    re.compile('^Check if webservice is available( \d)*$'),
    re.compile('^Clone row( \d)*$'),
    re.compile('^Closure Generator( \d)*$'),
    re.compile('^Combination lookup/update( \d)*$'),
    re.compile('^Concat Fields( \d)*$'),
    re.compile('^Copy rows to result( \d)*$'),
    re.compile('^CouchDB Input( \d)*$'),
    re.compile('^Credit card validator( \d)*$'),
    re.compile('^CSV file input( \d)*$'),
    re.compile('^Data Grid( \d)*$'),
    re.compile('^Data Validator( \d)*$'),
    re.compile('^Database join( \d)*$'),
    re.compile('^Database lookup( \d)*$'),
    re.compile('^De-serialize from file( \d)*$'),
    re.compile('^Delay row( \d)*$'),
    re.compile('^Delete( \d)*$'),
    re.compile('^Detect empty stream( \d)*$'),
    re.compile('^Dimension lookup/update( \d)*$'),
    re.compile('^Dummy (do nothing)( \d)*$'),
    re.compile('^Dynamic SQL row( \d)*$'),
    re.compile('^Edi to XML( \d)*$'),
    re.compile('^ElasticSearch Bulk Insert( \d)*$'),
    re.compile('^Email messages input( \d)*$'),
    re.compile('^ESRI Shapefile Reader( \d)*$'),
    re.compile('^ETL Metadata Injection( \d)*$'),
    re.compile('^Example plugin( \d)*$'),
    re.compile('^Execute a process( \d)*$'),
    re.compile('^Execute row SQL script( \d)*$'),
    re.compile('^Execute SQL script( \d)*$'),
    re.compile('^File exists( \d)*$'),
    re.compile('^Filter Rows( \d)*$'),
    re.compile('^Fixed file input( \d)*$'),
    re.compile('^Flow( \d)*$'),
    re.compile('^Formula( \d)*$'),
    re.compile('^Fuzzy match( \d)*$'),
    re.compile('^Generate random credit card numbers( \d)*$'),
    re.compile('^Generate random value( \d)*$'),
    re.compile('^Generate Rows( \d)*$'),
    re.compile('^Get data from XML( \d)*$'),
    re.compile('^Get File Names( \d)*$'),
    re.compile('^Get files from result( \d)*$'),
    re.compile('^Get Files Rows Count( \d)*$'),
    re.compile('^Get ID from slave server( \d)*$'),
    re.compile('^Get previous row fields( \d)*$'),
    re.compile('^Get repository names( \d)*$'),
    re.compile('^Get rows from result( \d)*$'),
    re.compile('^Get SubFolder names( \d)*$'),
    re.compile('^Get System Info( \d)*$'),
    re.compile('^Get table names( \d)*$'),
    re.compile('^Get Variables( \d)*$'),
    re.compile('^Google Analytics( \d)*$'),
    re.compile('^Google Docs Input( \d)*$'),
    re.compile('^GPLoad( \d)*$'),
    re.compile('^Greenplum Load( \d)*$'),
    re.compile('^Group by( \d)*$'),
    re.compile('^GZIP CSV Input( \d)*$'),
    re.compile('^Hadoop File Input( \d)*$'),
    re.compile('^Hadoop File Output( \d)*$'),
    re.compile('^HBase input( \d)*$'),
    re.compile('^HBase output( \d)*$'),
    re.compile('^HBase Row Decoder( \d)*$'),
    re.compile('^HL7 Input( \d)*$'),
    re.compile('^HL7Input( \d)*$'),
    re.compile('^HTTP client( \d)*$'),
    re.compile('^HTTP Post( \d)*$'),
    re.compile('^IBM Websphere MQ Consumer( \d)*$'),
    re.compile('^IBM Websphere MQ Producer( \d)*$'),
    re.compile('^Identify last row in a stream( \d)*$'),
    re.compile('^If field value is null( \d)*$'),
    re.compile('^Infobright Loader( \d)*$'),
    re.compile('^Ingres VectorWise Bulk Loader( \d)*$'),
    re.compile('^Injector( \d)*$'),
    re.compile('^Input( \d)*$'),
    re.compile('^Insert / Update( \d)*$'),
    re.compile('^Java Filter( \d)*$'),
    re.compile('^JMS Consumer( \d)*$'),
    re.compile('^JMS Producer( \d)*$'),
    re.compile('^JmsInput( \d)*$'),
    re.compile('^JmsOutput( \d)*$'),
    re.compile('^Job Executor( \d)*$'),
    re.compile('^JobExecutor( \d)*$'),
    re.compile('^Join Rows \(cartesian product\)( \d)*$'),
    re.compile('^Joins( \d)*$'),
    re.compile('^Joins( \d)*$'),
    re.compile('^JSON Input( \d)*$'),
    re.compile('^JSON output( \d)*$'),
    re.compile('^Knowledge Flow( \d)*$'),
    re.compile('^Knowledge Flow( \d)*$'),
    re.compile('^LDAP Input( \d)*$'),
    re.compile('^LDAP Output( \d)*$'),
    re.compile('^LDIF Input( \d)*$'),
    re.compile('^Load file content in memory( \d)*$'),
    re.compile('^LucidDB Bulk Loader( \d)*$'),
    re.compile('^LucidDB Streaming Loader( \d)*$'),
    re.compile('^Mail Validator( \d)*$'),
    re.compile('^Mail( \d)*$'),
    re.compile('^Mapping( \d)*$'),
    re.compile('^Mapping \(sub-transformation\)( \d)*$'),
    re.compile('^Mapping input specification( \d)*$'),
    re.compile('^Mapping output specification( \d)*$'),
    re.compile('^MapReduce Input( \d)*$'),
    re.compile('^MapReduce Output( \d)*$'),
    re.compile('^MaxMind GeoIP Lookup( \d)*$'),
    re.compile('^Memory Group by( \d)*$'),
    re.compile('^Merge Join( \d)*$'),
    re.compile('^Merge Rows (diff)( \d)*$'),
    re.compile('^Metadata structure of stream( \d)*$'),
    re.compile('^Microsoft Access Input( \d)*$'),
    re.compile('^Microsoft Access Output( \d)*$'),
    re.compile('^Microsoft Excel Input( \d)*$'),
    re.compile('^Microsoft Excel Output( \d)*$'),
    re.compile('^Microsoft Excel Writer( \d)*$'),
    re.compile('^Modified Java Script Value( \d)*$'),
    re.compile('^Mondrian Input( \d)*$'),
    re.compile('^MonetDB Agile Mart( \d)*$'),
    re.compile('^MonetDB Bulk Loader( \d)*$'),
    re.compile('^MongoDB Input( \d)*$'),
    re.compile('^MongoDB Output( \d)*$'),
    re.compile('^MQInput( \d)*$'),
    re.compile('^MQOutput( \d)*$'),
    re.compile('^Multiway Merge Join( \d)*$'),
    re.compile('^MySQL Bulk Loader( \d)*$'),
    re.compile('^Null if...( \d)*$'),
    re.compile('^Number range( \d)*$'),
    re.compile('^OLAP Input( \d)*$'),
    re.compile('^OpenERP Object Delete( \d)*$'),
    re.compile('^OpenERP Object Input( \d)*$'),
    re.compile('^OpenERP Object Output( \d)*$'),
    re.compile('^OpenERPObjectDelete( \d)*$'),
    re.compile('^OpenERPObjectOutputImport( \d)*$'),
    re.compile('^Oracle Bulk Loader( \d)*$'),
    re.compile('^Output( \d)*$'),
    re.compile('^Output steps metrics( \d)*$'),
    re.compile('^Output( \d)*$'),
    re.compile('^Palo Cell Input( \d)*$'),
    re.compile('^Palo Cell Output( \d)*$'),
    re.compile('^Palo Dimension Input( \d)*$'),
    re.compile('^Palo Dimension Output( \d)*$'),
    re.compile('^PaloCellInput( \d)*$'),
    re.compile('^PaloCellOutput( \d)*$'),
    re.compile('^PaloDimInput( \d)*$'),
    re.compile('^PaloDimOutput( \d)*$'),
    re.compile('^Pentaho Reporting Output( \d)*$'),
    re.compile('^PostgreSQL Bulk Loader( \d)*$'),
    re.compile('^Prioritize streams( \d)*$'),
    re.compile('^Process files( \d)*$'),
    re.compile('^Properties Output( \d)*$'),
    re.compile('^Property Input( \d)*$'),
    re.compile('^R script executor( \d)*$'),
    re.compile('^Regex Evaluation( \d)*$'),
    re.compile('^Replace in string( \d)*$'),
    re.compile('^Reservoir Sampling( \d)*$'),
    re.compile('^REST Client( \d)*$'),
    re.compile('^Row denormaliser( \d)*$'),
    re.compile('^Row flattener( \d)*$'),
    re.compile('^Row Normaliser( \d)*$'),
    re.compile('^RSS Input( \d)*$'),
    re.compile('^RSS Output( \d)*$'),
    re.compile('^Rule Accumulator( \d)*$'),
    re.compile('^Rule Executor( \d)*$'),
    re.compile('^Run SSH commands( \d)*$'),
    re.compile('^S3 CSV Input( \d)*$'),
    re.compile('^S3 File Output( \d)*$'),
    re.compile('^Salesforce Delete( \d)*$'),
    re.compile('^Salesforce Input( \d)*$'),
    re.compile('^Salesforce Insert( \d)*$'),
    re.compile('^Salesforce Update( \d)*$'),
    re.compile('^Salesforce Upsert( \d)*$'),
    re.compile('^Sample rows( \d)*$'),
    re.compile('^SAP Input( \d)*$'),
    re.compile('^SAS Input( \d)*$'),
    re.compile('^Script( \d)*$'),
    re.compile('^Secret key generator( \d)*$'),
    re.compile('^Select values( \d)*$'),
    re.compile('^Send message to Syslog( \d)*$'),
    re.compile('^Send messages to a JMS server( \d)*$'),
    re.compile('^Serialize to file( \d)*$'),
    re.compile('^Set field value to a constant( \d)*$'),
    re.compile('^Set field value( \d)*$'),
    re.compile('^Set files in result( \d)*$'),
    re.compile('^Set Variables( \d)*$'),
    re.compile('^SFTP Put( \d)*$'),
    re.compile('^Simple Mapping( \d)*$'),
    re.compile('^SimpleMapping( \d)*$'),
    re.compile('^Single Threader( \d)*$'),
    re.compile('^Socket reader( \d)*$'),
    re.compile('^Socket writer( \d)*$'),
    re.compile('^Sort rows( \d)*$'),
    re.compile('^Sorted Merge( \d)*$'),
    re.compile('^Split field to rows( \d)*$'),
    re.compile('^Split Fields( \d)*$'),
    re.compile('^Splunk Input( \d)*$'),
    re.compile('^Splunk Output( \d)*$'),
    re.compile('^SQL File Output( \d)*$'),
    re.compile('^SSTable Output( \d)*$'),
    re.compile('^Statistics( \d)*$'),
    re.compile('^Stream lookup( \d)*$'),
    re.compile('^Streaming XML Input( \d)*$'),
    re.compile('^String operations( \d)*$'),
    re.compile('^Strings cut( \d)*$'),
    re.compile('^Switch / Case( \d)*$'),
    re.compile('^Symmetric Cryptography( \d)*$'),
    re.compile('^Synchronize after merge( \d)*$'),
    re.compile('^Table Agile Mart( \d)*$'),
    re.compile('^Table Compare( \d)*$'),
    re.compile('^Table exists( \d)*$'),
    re.compile('^Table input( \d)*$'),
    re.compile('^Table output( \d)*$'),
    re.compile('^TableCompare( \d)*$'),
    re.compile('^Teradata Fastload Bulk Loader( \d)*$'),
    re.compile('^Teradata TPT Insert Upsert Bulk Loader( \d)*$'),
    re.compile('^Text file input( \d)*$'),
    re.compile('^Text file output( \d)*$'),
    re.compile('^Transform( \d)*$'),
    re.compile('^Transformation Executor( \d)*$'),
    re.compile('^Unique rows (HashSet)( \d)*$'),
    re.compile('^Unique rows( \d)*$'),
    re.compile('^Univariate Statistics( \d)*$'),
    re.compile('^Update( \d)*$'),
    re.compile('^User Defined Java Class( \d)*$'),
    re.compile('^User Defined Java Expression( \d)*$'),
    re.compile('^Utility( \d)*$'),
    re.compile('^Value Mapper( \d)*$'),
    re.compile('^Vertica Bulk Loader( \d)*$'),
    re.compile('^Web services lookup( \d)*$'),
    re.compile('^Write to log( \d)*$'),
    re.compile('^XBase input( \d)*$'),
    re.compile('^XML Input Stream (StAX)( \d)*$'),
    re.compile('^XML Input( \d)*$'),
    re.compile('^XML Join( \d)*$'),
    re.compile('^XML Output( \d)*$'),
    re.compile('^XSD Validator( \d)*$'),
    re.compile('^XSL Transformation( \d)*$'),
    re.compile('^Yaml Input( \d)*$'),
    re.compile('^Zip File( \d)*$'),
    re.compile('^ZipFile( \d)*$'),
    re.compile('^Abort job( \d)*$'),
    re.compile('^Add filenames to result( \d)*$'),
    re.compile('^Amazon EMR Job Executor( \d)*$'),
    re.compile('^Amazon Hive Job Executor( \d)*$'),
    re.compile('^Big Data( \d)*$'),
    re.compile('^BulkLoad from Mysql into file( \d)*$'),
    re.compile('^BulkLoad into MSSQL( \d)*$'),
    re.compile('^BulkLoad into Mysql( \d)*$'),
    re.compile('^Check Db connections( \d)*$'),
    re.compile('^Check files locked( \d)*$'),
    re.compile('^Check if a folder is empty( \d)*$'),
    re.compile('^Check if connected to repository( \d)*$'),
    re.compile('^Check if XML file is well formed( \d)*$'),
    re.compile('^Check webservice availability( \d)*$'),
    re.compile('^Checks if files exist( \d)*$'),
    re.compile('^Columns exist in a table( \d)*$'),
    re.compile('^Compare folders( \d)*$'),
    re.compile('^Convert file between Windows and Unix( \d)*$'),
    re.compile('^Copy Files( \d)*$'),
    re.compile('^Copy or Move result filenames( \d)*$'),
    re.compile('^Create a folder( \d)*$'),
    re.compile('^Create file( \d)*$'),
    re.compile('^Decrypt files with PGP( \d)*$'),
    re.compile('^Delete file( \d)*$'),
    re.compile('^Delete filenames from result( \d)*$'),
    re.compile('^Delete files( \d)*$'),
    re.compile('^Delete folders( \d)*$'),
    re.compile('^Display Msgbox Info( \d)*$'),
    re.compile('^DTD Validator( \d)*$'),
    re.compile('^DUMMY \(internal: SPECIAL\)( \d)*$'),
    re.compile('^Dummy( \d)*$'),
    re.compile('^Encrypt files with PGP( \d)*$'),
    re.compile('^Evaluate files metrics( \d)*$'),
    re.compile('^Evaluate rows number in a table( \d)*$'),
    re.compile('^Example plugin( \d)*$'),
    re.compile('^Execute Hive jobs in Amazon EMR( \d)*$'),
    re.compile('^Execute MapReduce jobs in Amazon EMR( \d)*$'),
    re.compile('^Export repository to XML file( \d)*$'),
    re.compile('^File Compare( \d)*$'),
    re.compile('^File Exists( \d)*$'),
    re.compile('^FTP Delete( \d)*$'),
    re.compile('^General( \d)*$'),
    re.compile('^Get a file with FTP( \d)*$'),
    re.compile('^Get a file with FTPS( \d)*$'),
    re.compile('^Get a file with SFTP( \d)*$'),
    re.compile('^Get mails (POP3/IMAP)( \d)*$'),
    re.compile('^Hadoop Copy Files( \d)*$'),
    re.compile('^Hadoop job executor( \d)*$'),
    re.compile('^HadoopJobExecutorPlugin( \d)*$'),
    re.compile('^HL7 MLLP Acknowledge( \d)*$'),
    re.compile('^HL7 MLLP Input( \d)*$'),
    re.compile('^HTTP( \d)*$'),
    re.compile('^JavaScript( \d)*$'),
    re.compile('^Job( \d)*$'),
    re.compile('^Mail validator( \d)*$'),
    re.compile('^Mail( \d)*$'),
    re.compile('^Move Files( \d)*$'),
    re.compile('^MS Access Bulk Load( \d)*$'),
    re.compile('^Oozie Job Executor( \d)*$'),
    re.compile('^Palo( \d)*$'),
    re.compile('^Palo Cube Create( \d)*$'),
    re.compile('^Palo Cube Delete( \d)*$'),
    re.compile('^PALO_CUBE_CREATE( \d)*$'),
    re.compile('^PALO_CUBE_DELETE( \d)*$'),
    re.compile('^Pentaho MapReduce( \d)*$'),
    re.compile('^Pig Script Executor( \d)*$'),
    re.compile('^Ping a host( \d)*$'),
    re.compile('^Process result filenames( \d)*$'),
    re.compile('^Put a file with FTP( \d)*$'),
    re.compile('^Put a file with SFTP( \d)*$'),
    re.compile('^Send information using Syslog( \d)*$'),
    re.compile('^Send Nagios passive check( \d)*$'),
    re.compile('^Send SNMP trap( \d)*$'),
    re.compile('^SEND_NAGIOS_PASSIVE_CHECK( \d)*$'),
    re.compile('^Set variables( \d)*$'),
    re.compile('^Shell( \d)*$'),
    re.compile('^Simple evaluation( \d)*$'),
    re.compile('^SQL( \d)*$'),
    re.compile('^Sqoop Export( \d)*$'),
    re.compile('^Sqoop Import( \d)*$'),
    re.compile('^SSH2 Get( \d)*$'),
    re.compile('^SSH2 Put( \d)*$'),
    re.compile('^START (internal: SPECIAL)( \d)*$'),
    re.compile('^Start a YARN Kettle Cluster( \d)*$'),
    re.compile('^Start( \d)*$'),
    re.compile('^Stop a YARN Kettle Cluster( \d)*$'),
    re.compile('^Stops a YARN Kettle Cluster( \d)*$'),
    re.compile('^Success( \d)*$'),
    re.compile('^Table exists( \d)*$'),
    re.compile('^Talend Job Execution( \d)*$'),
    re.compile('^Transformation( \d)*$'),
    re.compile('^Truncate tables( \d)*$'),
    re.compile('^Unzip file( \d)*$'),
    re.compile('^Upload files to FTPS( \d)*$'),
    re.compile('^Use the Dummy job entry to do nothing in a job.( \d)*$'),
    re.compile('^Utility( \d)*$'),
    re.compile('^Verify file signature with PGP( \d)*$'),
    re.compile('^Wait for file( \d)*$'),
    re.compile('^Wait for SQL( \d)*$'),
    re.compile('^Wait for( \d)*$'),
    re.compile('^Write to file( \d)*$'),
    re.compile('^Write To Log( \d)*$'),
    re.compile('^XSD Validator( \d)*$'),
    re.compile('^XSL Transformation( \d)*$'),
    re.compile('^Zip file( \d)*$')
]