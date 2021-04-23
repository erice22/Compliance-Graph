[[BSIMM]] #intelligence #security_feature_design
**[SFD1.1: 102] Integrate and deliver security features.**


Rather than having each project team implement its own security features (e.g., authentication, role management, key management, logging, cryptography, protocols), the SSG provides proactive guidance by acting as or facilitating a clearinghouse of security features for engineering groups to use. These features might be discovered during SSDL activities, created by the SSG or specialized development teams, or defined in configuration templates (e.g., cloud blueprints) and delivered via mechanisms such as containers, microservices, and APIs. Generic security features often have to be tailored for specific platforms. For example, each mobile and cloud platform will likely need their own means by which users are authenticated and authorized, secrets are managed, and user actions are centrally logged and monitored. Project teams benefit from implementations that come preapproved by the SSG, and the SSG benefits by not having to repeatedly track down the kinds of subtle errors that often creep into security features


