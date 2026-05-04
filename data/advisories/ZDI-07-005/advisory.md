# ZDI-07-005: Sun Microsystems Java GIF File Parsing Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-005
- **ZDI-CAN:** ZDI-CAN-054
- **Date:** 2007-01-16
- **CVE:** CVE-2007-0243
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-005/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Sun Microsystems Java Virtual Machine (JVM). User interaction is required to exploit this vulnerability in that the target must visit a malicious website. The specific flaw exists during the parsing of GIF image components. When the image width in an image block of a valid GIF file is set to 0, the Java runtime will allocate the specified size but subsequently copy all data to the under allocated memory chunk. The overflow results in the corruption of multiple pointers, at least one of which is later dereferenced and can therefore result in execution of arbitrary code.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.sunsolve.sun.com/search/document.do?assetkey=1-26-102760-1

## Disclosure Timeline

- 2006-06-16 - Vulnerability reported to vendor
- 2007-01-16 - Coordinated public release of advisory
