# ZDI-22-1433: Adobe ColdFusion Application Server Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1433
- **ZDI-CAN:** ZDI-CAN-16884
- **Date:** 2022-10-14
- **CVE:** CVE-2022-38421
- **CVSS:** 6.6
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** ColdFusion
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1433/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe ColdFusion. Authentication is required to exploit this vulnerability. The specific flaw exists within the Application Server endpoint, which listens on TCP port 8500 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/coldfusion/apsb22-44.html

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-10-14 - Coordinated public release of advisory
