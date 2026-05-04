# ZDI-21-585: Adobe InCopy DOCX File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-585
- **ZDI-CAN:** ZDI-CAN-12752
- **Date:** 2021-05-13
- **CVE:** CVE-2021-21090
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** InCopy
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-585/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe InCopy. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the conversion of DOCX files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/incopy/apsb21-25.html

## Disclosure Timeline

- 2020-12-18 - Vulnerability reported to vendor
- 2021-05-13 - Coordinated public release of advisory
