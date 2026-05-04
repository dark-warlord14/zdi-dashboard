# ZDI-10-109: Adobe Flash Player Multiple Atom MP4 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-109
- **ZDI-CAN:** ZDI-CAN-560
- **Date:** 2010-06-16
- **CVE:** CVE-2010-2162
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-109/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of the Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code responsible for parsing embedded MP4 files. When handling the STSC, STSZ, and STCO atoms the player can be made to improperly calculate length values later used as size parameters during memory copy operations. By providing a specially crafted file an attacker can corrupt heap memory and execute arbitrary code under the context of the currently logged in user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-14.html

## Disclosure Timeline

- 2009-10-27 - Vulnerability reported to vendor
- 2010-06-16 - Coordinated public release of advisory
