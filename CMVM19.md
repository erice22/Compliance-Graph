[[BSIMM]] #deployment #configuration_management #vulnerability_management
**[CMVM3.1: 5] Fix all occurrences of software bugs found in operations.**


The organization fixes all instances of each bug found during operations—not just the small number of instances that trigger bug reports—to meet recovery, continuity, and resiliency goals. Doing this proactively requires the ability to reexamine the entire inventory of software delivery value streams when new kinds of bugs come to light (see [CR3.3 Create capability to eradicate bugs]). One way to approach this is to create a ruleset that generalizes a deployed bug into something that can be scanned for via automated code review. Use of orchestration can greatly simplify deploying the fix for all occurrences of a software bug (see [SE3.5 Use orchestration for containers and virtualized environments]).


