# ZDI-15-047: Adobe Flash HLS Playlist Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-047
- **ZDI-CAN:** ZDI-CAN-2625
- **Date:** 2015-02-19
- **CVE:** CVE-2015-0331
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** bilou
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-047/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of an invalid m3u8 playlist. By manipulating this playlist an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-04.html

## Disclosure Timeline

- 2014-11-19 - Vulnerability reported to vendor
- 2015-02-19 - Coordinated public release of advisory
