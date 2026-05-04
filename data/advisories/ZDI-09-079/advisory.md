# ZDI-09-079: Sun Java Runtime AWT setBytePixels Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-079
- **ZDI-CAN:** ZDI-CAN-551
- **Date:** 2009-11-04
- **CVE:** CVE-2009-3871
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Peter Vreugdenhil ( http://vreugdenhilresearch.nl )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-079/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the processing of arguments to the setBytePixels AWT library function. Due to the lack of bounds checking on the parameters to the function a user controllable memcpy can result in a heap overflow. Successful exploitation of this vulnerability can lead to remote system compromise under the credentials of the currently logged in user.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://sunsolve.sun.com/search/document.do?assetkey=1-66-270474-1

## Disclosure Timeline

- 2009-08-14 - Vulnerability reported to vendor
- 2009-11-04 - Coordinated public release of advisory
