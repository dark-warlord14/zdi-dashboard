# ZDI-08-021: Adobe Flash Player DeclareFunction2 Invalid Object Use Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-021
- **ZDI-CAN:** ZDI-CAN-277
- **Date:** 2008-04-08
- **CVE:** CVE-2007-6019
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Javier Vicente Vallejo Shane Macaulay CanSecWest 2008 PWN2OWN Winner
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-021/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on vulnerable installations of Adobe's Flash Player. User interaction is required in that a user must visit a malicious web site. The specific flaw exists when the Flash player attempts to access embedded Actionscript objects that have not been properly instantiated. In order for exploitation to occur, an attacker would have to modify a DeclareFunction2 Actionscript tag within an SWF file. Exploitation of this vulnerability can result in arbitrary code execution under the context of the currently logged in user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb08-11.html

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-04-08 - Coordinated public release of advisory
