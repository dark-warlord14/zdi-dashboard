# ZDI-20-536: (Pwn2Own) OPC Foundation UA .NET Standard CreateSessionRequest Race Condition Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-536
- **ZDI-CAN:** ZDI-CAN-10295
- **Date:** 2020-04-16
- **CVE:** CVE-2020-8867
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** OPC Foundation
- **Affected Products:** UA .NET Standard
- **Credit:** Steven Seeley (mr_me) and Chris Anastasio (muffin)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-536/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of OPC Foundation UA .NET Standard. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of sessions. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to create a denial-of-service condition against the application.

## Additional Details

OPC Foundation has issued an update to correct this vulnerability. More details can be found at: https://opcfoundation.org/SecurityBulletins/OPC%20Foundation%20Security%20Bulletin%20CVE-2020-8867.pdf

## Disclosure Timeline

- 2020-02-07 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
