# ZDI-22-1420: Adobe ColdFusion Application Server Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1420
- **ZDI-CAN:** ZDI-CAN-16892
- **Date:** 2022-10-14
- **CVE:** CVE-2022-38423
- **CVSS:** 4.4
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** ColdFusion
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1420/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe ColdFusion. Authentication is required to exploit this vulnerability. The specific flaw exists within the Application Server endpoint, which listens on TCP port 8500 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/coldfusion/apsb22-44.html

## Disclosure Timeline

- 2022-06-10 - Vulnerability reported to vendor
- 2022-10-14 - Coordinated public release of advisory
