# ZDI-23-776: (Pwn2Own) Unified Automation UaGateway OPC UA Server Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-776
- **ZDI-CAN:** ZDI-CAN-20495
- **Date:** 2023-05-31
- **CVE:** CVE-2023-32171
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Unified Automation
- **Affected Products:** UaGateway
- **Credit:** Axel '0vercl0k' Souchet of https://doar-e.github.io/
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-776/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Unified Automation UaGateway. Authentication is required to exploit this vulnerability. The specific flaw exists within the ImportCsv method. A crafted XML payload can cause a null pointer dereference. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Unified Automation has issued an update to correct this vulnerability. More details can be found at: https://documentation.unified-automation.com/uagateway/1.5.14/CHANGELOG.txt

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
