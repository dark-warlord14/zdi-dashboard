# ZDI-14-040: Adobe Flash Player RegExp Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-040
- **ZDI-CAN:** ZDI-CAN-2070
- **Date:** 2014-04-03
- **CVE:** CVE-2014-0498
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Wen Guanxing from Venustech
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-040/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of regular expressions in ActionScript where an expression could overflow a data structure on the stack. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://helpx.adobe.com/security/products/flash-player/apsb14-07.html

## Disclosure Timeline

- 2014-02-07 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
