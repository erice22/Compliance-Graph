[[BSIMM]] #deployment #configuration_management #vulnerability_management
**[CMVM2.3: 65] Develop an operations inventory of software delivery value streams.**


The organization has a map of its software deployments, related containerization and orchestration automation code, and deployment automation code, along with the respective owners that contribute to business value streams. If a software asset needs to be changed, operations or DevOps teams can reliably identify both the stakeholders and all the places where the change needs to be deployed. Common components shared between multiple projects can be noted so that, when an error occurs in one application, other applications that share the same components can be fixed as well. Accurately representing an inventory will likely involve enumerating at least the source code, the open source incorporated both during the build and during dynamic production updates, the orchestration software incorporated into production images, and any service discovery or invocation that occurs in production.


