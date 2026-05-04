# ZDI-21-812: Adobe Acrobat Reader DC PDF File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-812
- **ZDI-CAN:** ZDI-CAN-13766
- **Date:** 2021-07-15
- **CVE:** CVE-2021-28638
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Xu Peng from UCAS and Wang Yanhao from QiAnXin Technology Research Institute
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-812/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb21-51.html

## Disclosure Timeline

- 2021-05-26 - Vulnerability reported to vendor
- 2021-07-15 - Coordinated public release of advisory
