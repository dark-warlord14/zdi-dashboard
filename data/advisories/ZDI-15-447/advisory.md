# ZDI-15-447: Adobe Flash AVSegmentedSource setSubscribedTags Uninitialized Memory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-447
- **ZDI-CAN:** ZDI-CAN-3110
- **Date:** 2015-09-21
- **CVE:** CVE-2015-5570
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bilou
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-447/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of AVSegmentedSource's setSubscribedTags method. By manipulating the properties of an AVSegmentedSource object and then calling the setSubscribedTags method, an attacker can dereference uninitialized memory. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-23.html

## Disclosure Timeline

- 2015-08-03 - Vulnerability reported to vendor
- 2015-09-21 - Coordinated public release of advisory
