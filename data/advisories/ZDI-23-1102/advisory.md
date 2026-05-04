# ZDI-23-1102: Adobe ColdFusion copydirectory Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1102
- **ZDI-CAN:** ZDI-CAN-20474
- **Date:** 2023-08-14
- **CVE:** CVE-2023-26361
- **CVSS:** 4.9
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** ColdFusion
- **Credit:** Dusan Stevanovic of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1102/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe ColdFusion. Authentication is required to exploit this vulnerability. The specific flaw exists within the copydirectory endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/coldfusion/apsb23-25.html

## Disclosure Timeline

- 2023-02-21 - Vulnerability reported to vendor
- 2023-08-14 - Coordinated public release of advisory
