# ZDI-08-080: Sun Java AWT Library Sandbox Violation Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-080
- **ZDI-CAN:** ZDI-CAN-319
- **Date:** 2008-12-04
- **CVE:** CVE-2008-5359
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-080/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun Microsystems Java. User interaction is required in that a user must open a malicious file or visit a malicious web page. The specific flaw occurs within the Java AWT library. If a custom image model is used for the source 'Raster' during a conversion through a 'ConvolveOp' operation, the imaging library will calculate the size of the destination raster for the conversion incorrectly leading to a heap-based overflow. This can result in arbitrary code execution under the context of the current user.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://sunsolve.sun.com/search/document.do?assetkey=1-66-244987-1

## Disclosure Timeline

- 2008-04-16 - Vulnerability reported to vendor
- 2008-12-04 - Coordinated public release of advisory
