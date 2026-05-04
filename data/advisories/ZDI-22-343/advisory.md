# ZDI-22-343: Adobe FrameMaker PostScript File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-343
- **ZDI-CAN:** ZDI-CAN-15245
- **Date:** 2022-02-15
- **CVE:** CVE-2022-23200
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** FrameMaker
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-343/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe FrameMaker. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PostScript files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/after_effects/apsb22-09.html

## Disclosure Timeline

- 2021-09-15 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory
