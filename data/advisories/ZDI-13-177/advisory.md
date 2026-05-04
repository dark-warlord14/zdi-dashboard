# ZDI-13-177: Adobe Flash Player Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-177
- **ZDI-CAN:** ZDI-CAN-1879
- **Date:** 2013-07-26
- **CVE:** CVE-2013-3347
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** vulnazoid
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-177/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the PCM processing code. By providing a malformed audio sample through ActionScript3, an attacker can cause an integer overflow. Using this overflow, an attacker can execute arbitrary code in the context of the Flash player.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb13-17.html

## Disclosure Timeline

- 2013-05-14 - Vulnerability reported to vendor
- 2013-07-26 - Coordinated public release of advisory
