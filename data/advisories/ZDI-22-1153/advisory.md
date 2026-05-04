# ZDI-22-1153: (Pwn2Own) Softing Secure Integration Server OPC UA Messages NULL Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1153
- **ZDI-CAN:** ZDI-CAN-16442
- **Date:** 2022-08-23
- **CVE:** CVE-2022-1748
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Softing
- **Affected Products:** Secure Integration Server
- **Credit:** Vera Mens, Uri Katz, Sharon Brizinov of Claroty Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1153/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Softing Secure Integration Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the the handling of OPC UA messages. The issue results from dereferencing a NULL pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Softing has issued an update to correct this vulnerability. More details can be found at: https://industrial.softing.com/fileadmin/psirt/downloads/syt-2022-7.html

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
