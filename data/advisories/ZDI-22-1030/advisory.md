# ZDI-22-1030: (Pwn2Own) Unified Automation OPC UA C++ Improper Update of Reference Count Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1030
- **ZDI-CAN:** ZDI-CAN-16927
- **Date:** 2022-07-28
- **CVE:** CVE-2022-37012
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Unified Automation
- **Affected Products:** OPC UA C++ Demo Server
- **Credit:** 20urdjk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1030/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Unified Automation OPC UA C++ Demo Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the OpcUa_SecureListener_ProcessSessionCallRequest method. A crafted OPC UA message can force the server to incorrectly update a reference count. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Unified Automation has issued an update to correct this vulnerability. More details can be found at: https://documentation.unified-automation.com/uasdkcpp/1.7.7/CHANGELOG.txt

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-07-28 - Coordinated public release of advisory
- 2022-07-28 - Advisory Updated
