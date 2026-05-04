# ZDI-10-149: Adobe Flash Player LocalConnection Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-149
- **ZDI-CAN:** ZDI-CAN-875
- **Date:** 2010-08-10
- **CVE:** CVE-2010-2188
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-149/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the connect method exposed via the ActionScript native object number 2200. If this function is called several times with differing strings, a memory corruption issue can be triggered. This can be exploited by remote attackers to execute arbitrary code under the context of the user running the web browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-16.html

## Disclosure Timeline

- 2010-07-21 - Vulnerability reported to vendor
- 2010-08-10 - Coordinated public release of advisory
