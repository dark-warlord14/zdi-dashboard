# ZDI-22-855: (Pwn2Own) OPC Foundation UA .NET Standard TranslateBrowsePathsToNodeId Resource Exhaustion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-855
- **ZDI-CAN:** ZDI-CAN-17197
- **Date:** 2022-06-16
- **CVE:** CVE-2022-29866
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** OPC Foundation
- **Affected Products:** UA .NET Standard
- **Credit:** Uriya Yavnieli, JFrog Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-855/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of OPC Foundation UA .NET Standard. Authentication is not required to exploit this vulnerability. The specific flaw exists within the TranslateBrowsePathsToNodeId method. The issue results from the lack of proper validation of user-supplied data, which can result in a memory exhaustion condition. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

OPC Foundation has issued an update to correct this vulnerability. More details can be found at: https://files.opcfoundation.org/SecurityBulletins/OPC%20Foundation%20Security%20Bulletin%20CVE-2022-29866.pdf

## Disclosure Timeline

- 2022-05-10 - Vulnerability reported to vendor
- 2022-06-16 - Coordinated public release of advisory
- 2022-06-16 - Advisory Updated
