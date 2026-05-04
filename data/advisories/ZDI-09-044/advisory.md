# ZDI-09-044: Adobe Shockwave Player Director File Parsing Pointer Overwrite Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-044
- **ZDI-CAN:** ZDI-CAN-327
- **Date:** 2009-06-24
- **CVE:** CVE-2009-1860
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Paul Kurczaba
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-044/
## Vulnerability Details

This vulnerability allows remote attackers to execute code on vulnerable installations of Adobe's Shockwave Player. User interaction is required in that a user must visit a malicious web site. The specific flaw exists when the Shockwave player attempts to load a specially crafted Adobe Director File. When a malicious value is used during a memory dereference a possible 4-byte memory overwrite may occur. Exploitation can lead to remote system compromise under the credentials of the currently logged in user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb09-08.html

## Disclosure Timeline

- 2008-05-12 - Vulnerability reported to vendor
- 2009-06-24 - Coordinated public release of advisory
