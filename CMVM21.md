[[BSIMM]] #deployment #configuration_management #vulnerability_management
**[CMVM3.2: 11] Enhance the SSDL to prevent software bugs found in operations.**


Experience from operations leads to changes in the SSDL, which can in turn be strengthened to prevent the reintroduction of bugs found during operations. To make this process systematic, incident response postmortem could include a feedback-to-SSDL step. The outcomes of the postmortem might result in changes such as tool-based policy rulesets in a CI/CD pipeline and adjustments to automated deployment configuration (see [SM3.4 Integrated software-defined lifecycle governance]). This works best when root-cause analysis pinpoints where in the software lifecycle an error could have been introduced or slipped by uncaught. DevOps engineers might have an easier time with this because all the players are likely involved in the discussion and the solution. An ad hoc approach to SSDL improvement isn’t sufficient.


