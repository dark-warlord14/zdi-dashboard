# ZDI-23-1286: Unified Automation UaGateway Certificate Parsing Integer Overflow Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1286
- **ZDI-CAN:** ZDI-CAN-20353
- **Date:** 2023-08-30
- **CVE:** CVE-2023-41185
- **CVSS:** 8.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:N/A:H
- **Affected Vendors:** Unified Automation
- **Affected Products:** UaGateway
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1286/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Unified Automation UaGateway. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of client certificates. When parsing the certificate length field, the process does not properly validate user-supplied data, which can result in an integer overflow. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Fixed in UaGateway 1.5.13 on March 20, 2023. https://www.unified-automation.com/news/news-details/new-uagateway-v1513-service-release.html

## Disclosure Timeline

- 2023-02-14 - Vulnerability reported to vendor
- 2023-08-30 - Coordinated public release of advisory
