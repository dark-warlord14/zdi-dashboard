# ZDI-23-1065: (0Day) (Pwn2Own) Softing edgeConnector Siemens OPC UA Server Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1065
- **ZDI-CAN:** ZDI-CAN-20508
- **Date:** 2023-08-09
- **CVE:** CVE-2023-27336
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Softing
- **Affected Products:** edgeConnector Siemens
- **Credit:** Team ECQ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1065/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Softing edgeConnector Siemens. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of OPC client certificates. The issue results from dereferencing a NULL pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

02/16/23 – The ZDI reported this vulnerability to the vendor during the Pwn2Own Miami contest. 02/20/23 – The vendor states they would review and report back with the security advisories. 03/08/23 – The vendor requested CVE Numbers. 03/15/23 – ZDI provided the vendor with CVE numbers. 07/31/23 – ZDI asked for an update. 08/03/23 – ZDI asked for an update. 08/07/23 – The ZDI asked for an update and informed the vendor that we are publishing this case as a zero-day advisory on 08/09/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-08-09 - Coordinated public release of advisory
