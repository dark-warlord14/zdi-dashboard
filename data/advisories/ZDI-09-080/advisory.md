# ZDI-09-080: Sun Java Runtime Environment JPEGImageReader Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-080
- **ZDI-CAN:** ZDI-CAN-562
- **Date:** 2009-11-04
- **CVE:** CVE-2009-3874
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-080/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun's Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the processing of JPEG image dimensions. When specifying large values to the dimensions of a subsample an integer overflow occurs leading to memory corruption. Successful exploitation of this vulnerability can lead to remote compromise under the credentials of the currently logged in user.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://sunsolve.sun.com/search/document.do?assetkey=1-66-270474-1

## Disclosure Timeline

- 2009-08-20 - Vulnerability reported to vendor
- 2009-11-04 - Coordinated public release of advisory
