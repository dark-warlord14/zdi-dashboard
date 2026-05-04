# ZDI-18-1187: Adobe Acrobat ImageConversion EMF EMR_STRETCHBLT Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1187
- **ZDI-CAN:** ZDI-CAN-6789
- **Date:** 2018-10-11
- **CVE:** CVE-2018-15947
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro 2017 (classic)
- **Credit:** Ron Waisberg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1187/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMR_STRETCHBLT records in EMF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-30.html

## Disclosure Timeline

- 2018-07-12 - Vulnerability reported to vendor
- 2018-10-11 - Coordinated public release of advisory
