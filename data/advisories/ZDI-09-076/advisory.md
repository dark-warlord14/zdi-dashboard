# ZDI-09-076: Sun Java HsbParser.getSoundBank Stack Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-076
- **ZDI-CAN:** ZDI-CAN-491
- **Date:** 2009-11-04
- **CVE:** CVE-2009-3867
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-076/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun Microsystems Java. User interaction is required in that a user must open a malicious file or visit a malicious web page. The specific flaw exists in the parsing of long file:// URL arguments to the getSoundbank() function. Due to a lack of bounds checking on user supplied data a stack overflow can occur leading to remote code execution. Exploitation of this vulnerability can lead to system compromise under the credentials of the currently logged in user.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://sunsolve.sun.com/search/document.do?assetkey=1-66-270474-1

## Disclosure Timeline

- 2009-06-23 - Vulnerability reported to vendor
- 2009-11-04 - Coordinated public release of advisory
