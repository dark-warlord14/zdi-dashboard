# ZDI-14-365: Adobe Flash Player casi32 Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-365
- **ZDI-CAN:** ZDI-CAN-2518
- **Date:** 2014-10-14
- **CVE:** CVE-2014-0569
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** bilou
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-365/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of casi32. The issue lies in the failure to properly sanitize a user-supplied length value with a specific array implementation. An attacker can leverage this vulnerability to execute code within the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb14-22.html

## Disclosure Timeline

- 2014-09-10 - Vulnerability reported to vendor
- 2014-10-14 - Coordinated public release of advisory
