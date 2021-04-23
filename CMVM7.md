[[BSIMM]] #deployment #configuration_management #vulnerability_management
**[CMVM1.2: 102] Identify software defects found in operations monitoring and feed them back to development.**


Defects identified in production through operations monitoring are fed back to development and used to change developer behavior. The contents of production logs can be revealing (or can reveal the need for improved logging). Entering incident triage data into an existing bug-tracking system (perhaps by making use of a special security flag) can close the information loop and make sure that security issues get fixed. Increasingly, organizations are relying on telemetry provided by agents packaged with software as part of cloud security posture monitoring, container configuration monitoring, RASP, or similar products to detect software defects or adversaries’ exploration prior to exploit. In most cases, organizations must also rely on additional analysis tools (e.g., ELK, Datadog) to aggregate and correlate that avalanche of data and provide useful input to development. In the best of cases, processes in the SSDL can be improved based on operational data (see [CMVM3.2 Enhance the SSDL to prevent software bugs found in operations]).


