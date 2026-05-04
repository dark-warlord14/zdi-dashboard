# ZDI-23-780: Unified Automation UaGateway NodeManagerOpcUa Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-780
- **ZDI-CAN:** ZDI-CAN-20577
- **Date:** 2023-05-31
- **CVE:** CVE-2023-32174
- **CVSS:** 9.1
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Unified Automation
- **Affected Products:** UaGateway
- **Credit:** Axel '0vercl0k' Souchet of https://doar-e.github.io/
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-780/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Unified Automation UaGateway. Authentication is required to exploit this vulnerability when the product is in its default configuration. The specific flaw exists within the handling of NodeManagerOpcUa objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Unified Automation has issued an update to correct this vulnerability. More details can be found at: https://documentation.unified-automation.com/uagateway/1.5.14/CHANGELOG.txt

## Disclosure Timeline

- 2023-04-28 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
