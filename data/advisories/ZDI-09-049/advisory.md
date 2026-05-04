# ZDI-09-049: Sun Java Pack200 Decoding Inner Class Count Integer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-049
- **ZDI-CAN:** ZDI-CAN-475
- **Date:** 2009-08-05
- **CVE:** CVE-2009-2675
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-049/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Sun Java Runtime. User interaction is required in that a target must visit a malicious web page or open a malicious JNLP file. The specific flaw exists within the code responsible for handling Pack200 compressed JAR files. During decompression, several fields within a Pack200 header are trusted and used to calculate sizes for heap buffer allocations. By providing malicious values an attacker can create undersized heap buffers and subsequently overflow them. This can be leveraged to execute arbitrary code under the context of the user accessing the file or web page.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://sunsolve.sun.com/search/document.do?assetkey=1-66-263488-1

## Disclosure Timeline

- 2009-04-15 - Vulnerability reported to vendor
- 2009-08-05 - Coordinated public release of advisory
