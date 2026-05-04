# ZDI-09-093: Adobe Flash Player ActionScript Exception Handler Integer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-093
- **ZDI-CAN:** ZDI-CAN-392
- **Date:** 2009-12-09
- **CVE:** CVE-2009-3799
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-093/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page or open a malicious SWF file. The specific flaw exists in the generation of ActionScript exception handlers. In Verifier::parseExceptionHandlers(), a large value for exception_count will result in an integer overflow condition leading to a memory corruption which can be leveraged to execute arbitrary code under the context of the currently logged in user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb09-19.html

## Disclosure Timeline

- 2008-10-15 - Vulnerability reported to vendor
- 2009-12-09 - Coordinated public release of advisory
