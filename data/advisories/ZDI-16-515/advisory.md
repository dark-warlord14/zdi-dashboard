# ZDI-16-515: Adobe Flash TextFormat Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-515
- **ZDI-CAN:** ZDI-CAN-3862
- **Date:** 2016-09-16
- **CVE:** CVE-2016-4279
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Mumei
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-515/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the TextFormat object. The issue lies in the failure to properly validate user-supplied data which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-29.html

## Disclosure Timeline

- 2016-07-27 - Vulnerability reported to vendor
- 2016-09-16 - Coordinated public release of advisory
