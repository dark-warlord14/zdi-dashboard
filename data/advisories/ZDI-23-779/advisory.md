# ZDI-23-779: Unified Automation UaGateway AddServer XML Injection Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-779
- **ZDI-CAN:** ZDI-CAN-20576
- **Date:** 2023-05-31
- **CVE:** CVE-2023-32173
- **CVSS:** 5.8
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:C/C:N/I:N/A:H
- **Affected Vendors:** Unified Automation
- **Affected Products:** UaGateway
- **Credit:** Axel '0vercl0k' Souchet of https://doar-e.github.io/
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-779/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Unified Automation UaGateway. Authentication is required to exploit this vulnerability when the product is in its default configuration. The specific flaw exists within the implementation of the AddServer method. By specifying crafted arguments, an attacker can cause invalid characters to be inserted into an XML configuration file. An attacker can leverage this vulnerability to create a persistent denial-of-service condition on the system.

## Additional Details

Unified Automation has issued an update to correct this vulnerability. More details can be found at: https://documentation.unified-automation.com/uagateway/1.5.14/CHANGELOG.txt

## Disclosure Timeline

- 2023-04-28 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
