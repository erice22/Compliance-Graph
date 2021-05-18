[[BSIMM]] #SSDL #security_testing
**[ST1.3: 89] Drive tests with security requirements and security features.**


QA targets declarative security mechanisms with tests derived from requirements and security features. A test could try to access administrative functionality as an unprivileged user, for example, or verify that a user account becomes locked after some number of failed authentication attempts. For the most part, security features can be tested in a fashion similar to other software features—security mechanisms such as account lockout, transaction limitations, entitlements, and so on are tested with both expected and unexpected input as derived from requirements. Software security isn’t security software, but testing security features is an easy way to get started. New software architectures and deployment automation, such as with container and cloud infrastructure orchestration, might require novel test approaches.


