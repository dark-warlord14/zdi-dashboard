# ZDI-12-185: Apple Mac OS X DirectoryService SwapProxyMessage Unchecked objOffset Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-185
- **ZDI-CAN:** ZDI-CAN-1385
- **Date:** 2012-11-15
- **CVE:** CVE-2012-0650
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** aazubel
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-185/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Mac OSX. Authentication is not required to exploit this vulnerability. The flaw exists within the DirectoryService daemon. This process listens on TCP port 625 by default on Mac OSX Server pre 10.7. Request types to the service include a sComProxyData structure having a translate field which is responsible for describing the endianness of the payload. When passing a message to SwapProxyMessage for byte-reordering, multiple user controlled fields are trusted including lengths and offsets. When processing this data with DSSwapObjectData, the process will address memory out of the bounds of the allocated region. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2011-11-29 - Vulnerability reported to vendor
- 2012-11-15 - Coordinated public release of advisory
