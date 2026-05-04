# ZDI-16-160: Adobe Flash instanceof Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-160
- **ZDI-CAN:** ZDI-CAN-3452
- **Date:** 2016-02-09
- **CVE:** CVE-2016-0975
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-160/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of instanceof. The issue lies in the failure to safely hold a reference to arguments during execution of the function. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-04.html

## Disclosure Timeline

- 2015-12-08 - Vulnerability reported to vendor
- 2016-02-09 - Coordinated public release of advisory
