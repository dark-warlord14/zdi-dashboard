# ZDI-17-579: Adobe Acrobat Pro DC ImageConversion JPEG Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-579
- **ZDI-CAN:** ZDI-CAN-4562
- **Date:** 2017-08-08
- **CVE:** CVE-2017-11211
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** @vftable
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-579/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within ImageConversion's JPEG parsing. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-24.html

## Disclosure Timeline

- 2017-03-23 - Vulnerability reported to vendor
- 2017-08-08 - Coordinated public release of advisory
