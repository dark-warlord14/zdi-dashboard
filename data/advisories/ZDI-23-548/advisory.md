# ZDI-23-548: (Pwn2Own) OPC Foundation UA .NET Standard ConditionRefresh Resource Exhaustion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-548
- **ZDI-CAN:** ZDI-CAN-20505
- **Date:** 2023-05-04
- **CVE:** CVE-2023-27321
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** OPC Foundation
- **Affected Products:** UA .NET Standard
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-548/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of OPC Foundation UA .NET Standard. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of OPC UA ConditionRefresh requests. By sending a large number of requests, an attacker can consume all available resources on the server. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

OPC Foundation has issued an update to correct this vulnerability. More details can be found at: https://files.opcfoundation.org/SecurityBulletins/OPC%20Foundation%20Security%20Bulletin%20CVE-2023-27321.pdf

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory
