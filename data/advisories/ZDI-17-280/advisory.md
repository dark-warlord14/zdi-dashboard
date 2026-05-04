# ZDI-17-280: (Pwn2Own) Adobe Reader DC JPEG2000 Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-280
- **ZDI-CAN:** ZDI-CAN-4575
- **Date:** 2017-04-11
- **CVE:** CVE-2017-3055
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** LiuBenjin from 360 Codesafe Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-280/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within JPEG2000 parsing. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-11.html

## Disclosure Timeline

- 2017-03-19 - Vulnerability reported to vendor
- 2017-04-11 - Coordinated public release of advisory
