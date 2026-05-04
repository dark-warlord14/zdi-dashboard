# ZDI-14-417: Adobe Flash Player parseFloat Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-417
- **ZDI-CAN:** ZDI-CAN-2552
- **Date:** 2014-12-09
- **CVE:** CVE-2014-9163
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** bilou
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-417/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists when calling parseFloat on a specific datatype. This can allow for an attacker to cause a fixed size stack buffer to overflow. An attacker can leverage this vulnerability to execute code within the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb14-27.html

## Disclosure Timeline

- 2014-10-15 - Vulnerability reported to vendor
- 2014-12-09 - Coordinated public release of advisory
