# ZDI-17-015: Adobe Reader DC XSLT key Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-015
- **ZDI-CAN:** ZDI-CAN-4181
- **Date:** 2017-01-10
- **CVE:** CVE-2017-2949
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-015/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within XSLT's key. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-01.html

## Disclosure Timeline

- 2016-11-03 - Vulnerability reported to vendor
- 2017-01-10 - Coordinated public release of advisory
