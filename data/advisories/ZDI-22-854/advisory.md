# ZDI-22-854: (Pwn2Own) OPC Foundation UA .NET Standard Resource Exhaustion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-854
- **ZDI-CAN:** ZDI-CAN-16440
- **Date:** 2022-06-16
- **CVE:** CVE-2022-29864
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** OPC Foundation
- **Affected Products:** UA .NET Standard
- **Credit:** Vera Mens, Uri Katz, Sharon Brizinov of Claroty Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-854/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of OPC Foundation UA .NET Standard. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of message chunks. By sending a large number of requests, an attacker can cause the number of sessions to grow without limit. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

OPC Foundation has issued an update to correct this vulnerability. More details can be found at: https://files.opcfoundation.org/SecurityBulletins/OPC%20Foundation%20Security%20Bulletin%20CVE-2022-29864.pdf

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-06-16 - Coordinated public release of advisory
- 2022-06-22 - Advisory Updated
