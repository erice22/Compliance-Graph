[[BSIMM]] #deployment #software_environment
**[SE1.1: 73] Use application input monitoring.**


The organization monitors the input to the software that it runs in order to spot attacks. For web code, a WAF can do this job, while other kinds of software likely require other approaches, including runtime instrumentation. The SSG might be responsible for the care and feeding of the monitoring system, but incident response isn’t part of this activity. For web applications, WAFs that write log files can be useful if someone periodically reviews the logs and takes action. Other software and technology stacks, such as mobile and IoT, likely require their own input monitoring solutions. Serverless and containerized software can require interaction with vendor software to get the appropriate logs and monitoring data. Cloud deployments and platform-as-a-service usage can add another level of difficulty to the monitoring, collection, and aggregation approach.


