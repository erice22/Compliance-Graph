[[BSIMM]] #deployment #configuration_management #vulnerability_management
**[CMVM3.5: 8] Automate verification of operational infrastructure security.**


The SSG works with engineering teams to facilitate a controlled self-service process that replaces some traditional IT efforts, such as application and infrastructure deployment, and includes verification of security properties (e.g., adherence to agreed-upon security hardening). Engineers now create networks, containers, and machine instances, orchestrate deployments, and perform other tasks that were once IT’s sole responsibility (see [AM3.3 Monitor automated asset creation]). In facilitating this change, the organization uses machine-readable policies and configuration standards to automatically detect issues such as configuration drift and report on infrastructure that does not meet expectations (see [SE2.2 Define secure deployment parameters and configurations]). In some cases, the automation makes changes to running environments to bring them into compliance. In many cases, organizations use a single policy to manage automation in different environments, such as in multi-cloud and hybrid-cloud environments.


  

**[CMVM3.6: 0] Publish risk data for deployable artifacts.**


The organization collects and publishes risk telemetry about the applications, services, APIs, containers, and other software it deploys. Published information extends beyond basic software security (see [SM2.1 Publish data about software security internally]) and inventory data (see [SM3.1 Use a software asset tracking application with portfolio view]) to include information about constituency of the software (e.g., [bill of materials](https://www.synopsys.com/blogs/software-security/software-bill-of-materials-bom/)), what group created it and how, and the risks associated with vulnerability, security controls, or other characteristics intrinsic to each artifact. This approach stimulates cross-functional coordination and helps stakeholders take informed risk management action. In some cases, much of this information is created by automated processes and associated with a registry that provides stakeholder visibility. Making a list of risks that aren’t used for decision support won’t achieve useful results.


