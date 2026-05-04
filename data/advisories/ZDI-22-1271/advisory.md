# ZDI-22-1271: Adobe InCopy EPS File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1271
- **ZDI-CAN:** ZDI-CAN-17607
- **Date:** 2022-09-19
- **CVE:** CVE-2022-38407
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** InCopy
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1271/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe InCopy. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EPS files. Crafted data in an EPS file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/incopy/apsb22-53.html

## Disclosure Timeline

- 2022-06-03 - Vulnerability reported to vendor
- 2022-09-19 - Coordinated public release of advisory
