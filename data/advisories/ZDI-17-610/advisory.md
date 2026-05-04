# ZDI-17-610: Adobe Acrobat Pro DC JPEG2000 Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-610
- **ZDI-CAN:** ZDI-CAN-4817
- **Date:** 2017-08-08
- **CVE:** CVE-2017-11228
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Giwan Go of STEALIEN & HIT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-610/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JPEG2000 images. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-24.html

## Disclosure Timeline

- 2017-05-17 - Vulnerability reported to vendor
- 2017-08-08 - Coordinated public release of advisory
