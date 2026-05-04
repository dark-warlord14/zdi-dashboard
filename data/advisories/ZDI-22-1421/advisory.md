# ZDI-22-1421: Adobe ColdFusion ODBC Server Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1421
- **ZDI-CAN:** ZDI-CAN-16898
- **Date:** 2022-10-14
- **CVE:** CVE-2022-35710
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** ColdFusion
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1421/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe ColdFusion. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of GIOP packets. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/coldfusion/apsb22-44.html

## Disclosure Timeline

- 2022-05-13 - Vulnerability reported to vendor
- 2022-10-14 - Coordinated public release of advisory
