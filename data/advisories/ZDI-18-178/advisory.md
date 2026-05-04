# ZDI-18-178: Adobe Flash Player QOSProvider attachMediaPlayerItemLoader Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-178
- **ZDI-CAN:** ZDI-CAN-5381
- **Date:** 2018-02-23
- **CVE:** CVE-2018-4877
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bo13oy of Qihoo 360 Vulcan Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-178/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of QOSProvider objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb18-03.html

## Disclosure Timeline

- 2017-12-21 - Vulnerability reported to vendor
- 2018-02-23 - Coordinated public release of advisory
- 2018-02-23 - Advisory Updated
