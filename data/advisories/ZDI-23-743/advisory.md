# ZDI-23-743: (Pwn2Own) Unified Automation OPC UA C++ Demo Server DemoDynamicNodesDeleteDynamicNode Use-After Free Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-743
- **ZDI-CAN:** ZDI-CAN-17196
- **Date:** 2023-05-31
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Unified Automation
- **Affected Products:** OPC UA C++ Demo Server
- **Credit:** Omer Kaspi, JFrog Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-743/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Unified Automation OPC UA C++ Demo Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DemoDynamicNodesDeleteDynamicNode method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Unified Automation has issued an update to correct this vulnerability. More details can be found at: https://documentation.unified-automation.com/uasdkcpp/1.7.7/CHANGELOG.txt

## Disclosure Timeline

- 2022-05-10 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
