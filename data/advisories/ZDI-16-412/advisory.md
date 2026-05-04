# ZDI-16-412: Microsoft Edge CGeolocationManager Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-412
- **ZDI-CAN:** ZDI-CAN-3747
- **Date:** 2016-07-12
- **CVE:** CVE-2016-3264
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** exp-sky (http://exp-sky.org) of Tencent's Xuanwu LAB (http://www.tencent.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-412/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Microsoft Edge requests permission from the user to allow a website to access device location information (for example, GPS). By performing certain actions in script, an attacker can force a CGeolocationManager object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-085

## Disclosure Timeline

- 2016-05-05 - Vulnerability reported to vendor
- 2016-07-12 - Coordinated public release of advisory
