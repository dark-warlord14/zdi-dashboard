# ZDI-08-010: Java Web Start encoding Stack Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-010
- **ZDI-CAN:** ZDI-CAN-235
- **Date:** 2008-03-12
- **CVE:** CVE-2008-1188
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-010/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun Java Web Start. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the useEncodingDecl() function used while parsing the xml header character encoding attribute. When a user downloads a malicious JNLP file, the charset value is read into a static buffer. If an overly charset name in the xml header is included, a stack based buffer overflow occurs, resulting in an exploitable condition.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://sunsolve.sun.com/search/document.do?assetkey=1-66-233323-1

## Disclosure Timeline

- 2007-09-14 - Vulnerability reported to vendor
- 2008-03-12 - Coordinated public release of advisory
