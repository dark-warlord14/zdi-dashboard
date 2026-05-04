# ZDI-22-1029: (Pwn2Own) Unified Automation OPC UA C++ Infinite Loop Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1029
- **ZDI-CAN:** ZDI-CAN-17203
- **Date:** 2022-07-28
- **CVE:** CVE-2022-37013
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Unified Automation
- **Affected Products:** OPC UA C++ Demo Server
- **Credit:** Daan Keuper & Thijs Alkemade from Computest
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1029/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Unified Automation OPC UA C++ Demo Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of certificates. A crafted certificate can force the server into an infinite loop. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Unified Automation has issued an update to correct this vulnerability. More details can be found at: https://documentation.unified-automation.com/uasdkcpp/1.7.7/CHANGELOG.txt

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-07-28 - Coordinated public release of advisory
- 2022-07-28 - Advisory Updated
