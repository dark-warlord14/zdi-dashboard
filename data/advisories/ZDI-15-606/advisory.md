# ZDI-15-606: Adobe Flash AS2 SharedObject getRemote Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-606
- **ZDI-CAN:** ZDI-CAN-3328
- **Date:** 2015-12-08
- **CVE:** CVE-2015-8439
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bilou
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-606/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the SharedObject objects. By calling the getRemote method, it is possible to trigger a type confusion condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-32.html

## Disclosure Timeline

- 2015-10-01 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
