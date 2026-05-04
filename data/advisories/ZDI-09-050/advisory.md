# ZDI-09-050: Sun Java Web Start JPEG Header Parsing Integer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-050
- **ZDI-CAN:** ZDI-CAN-460
- **Date:** 2009-08-05
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-050/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun Java Web Start. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the code that handles loading a custom JPEG splash screen for a WebStart application. While handling certain parts of the splash screen, javaws.exe makes an improper calculation which is later used for an allocation. Later during decompression, Java Web Start will write data into this mis-allocated buffer resulting in a heap-based buffer overflow and eventual code execution under the context of the current user.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://sunsolve.sun.com/search/document.do?assetkey=1-66-263428-1

## Disclosure Timeline

- 2009-03-26 - Vulnerability reported to vendor
- 2009-08-05 - Coordinated public release of advisory
