# ZDI-16-626: Adobe Flash MovieClip swapDepth Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-626
- **ZDI-CAN:** ZDI-CAN-4041
- **Date:** 2016-12-13
- **CVE:** CVE-2016-7872
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Saber
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-626/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within MovieClip's swapDepth method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-39.html

## Disclosure Timeline

- 2016-10-06 - Vulnerability reported to vendor
- 2016-12-13 - Coordinated public release of advisory
