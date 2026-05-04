# ZDI-23-777: (Pwn2Own) Unified Automation UaGateway OPC UA Server Use-After-Free Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-777
- **ZDI-CAN:** ZDI-CAN-20497
- **Date:** 2023-05-31
- **CVE:** CVE-2023-32172
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Unified Automation
- **Affected Products:** UaGateway
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-777/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Unified Automation UaGateway. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the ImportXML function. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Unified Automation has issued an update to correct this vulnerability. More details can be found at: https://documentation.unified-automation.com/uagateway/1.5.14/CHANGELOG.txt

## Disclosure Timeline

- 2023-02-24 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
