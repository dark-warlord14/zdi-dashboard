# ZDI-24-1149: Ivanti Avalanche deleteSkin Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1149
- **ZDI-CAN:** ZDI-CAN-21401
- **Date:** 2024-08-15
- **CVE:** CVE-2024-38652
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1149/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the deleteSkin method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-Avalanche-6-4-4-CVE-2024-38652-CVE-2024-38653-CVE-2024-36136-CVE-2024-37399-CVE-2024-37373?language=en_US

## Disclosure Timeline

- 2023-07-18 - Vulnerability reported to vendor
- 2024-08-15 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
