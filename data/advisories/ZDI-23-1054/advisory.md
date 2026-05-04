# ZDI-23-1054: (Pwn2Own) Softing edgeConnector Siemens ConditionRefresh Resource Exhaustion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1054
- **ZDI-CAN:** ZDI-CAN-20498
- **Date:** 2023-08-09
- **CVE:** CVE-2023-27334
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Softing
- **Affected Products:** edgeConnector Siemens
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1054/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Softing edgeConnector Siemens. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of OPC UA ConditionRefresh requests. By sending a large number of requests, an attacker can consume all available resources on the server. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Softing has issued an update to correct this vulnerability. More details can be found at: https://industrial.softing.com/fileadmin/psirt/downloads/syt-2023-1.html

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-08-09 - Coordinated public release of advisory
