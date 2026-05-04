# ZDI-15-514: Adobe Flash TextFormat tabStops Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-514
- **ZDI-CAN:** ZDI-CAN-2960
- **Date:** 2015-10-13
- **CVE:** CVE-2015-7629
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** instruder of alibaba security research team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-514/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the TextFormat objects. By manipulating the tabStops property of a TextFormat object, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-25.html

## Disclosure Timeline

- 2015-06-25 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
