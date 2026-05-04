# ZDI-23-1559: F5 BIG-IP OS unzip Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1559
- **ZDI-CAN:** ZDI-CAN-21463
- **Date:** 2023-10-18
- **CVE:** CVE-2023-41373
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** F5
- **Affected Products:** BIG-IP OS
- **Credit:** Alex Birnberg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1559/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of F5 BIG-IP OS. Authentication is required to exploit this vulnerability. The specific flaw exists within the unzip method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the apache user.

## Additional Details

F5 has issued an update to correct this vulnerability. More details can be found at: https://my.f5.com/manage/s/article/K000135689

## Disclosure Timeline

- 2023-07-20 - Vulnerability reported to vendor
- 2023-10-18 - Coordinated public release of advisory
