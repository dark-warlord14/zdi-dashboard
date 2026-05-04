# ZDI-16-569: Adobe Flash Accessibility sendEvent Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-569
- **ZDI-CAN:** ZDI-CAN-3989
- **Date:** 2016-10-12
- **CVE:** CVE-2016-6987
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Akitsu Madoka
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-569/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Accessibility's sendEvent method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-32.html

## Disclosure Timeline

- 2016-09-08 - Vulnerability reported to vendor
- 2016-10-12 - Coordinated public release of advisory
