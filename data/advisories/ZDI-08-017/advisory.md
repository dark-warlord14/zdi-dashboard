# ZDI-08-017: Apple QuickTime Kodak Encoding Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-017
- **ZDI-CAN:** ZDI-CAN-289
- **Date:** 2008-04-03
- **CVE:** CVE-2008-1020
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Ruben Santamarta of Reversemode.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-017/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple QuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the quicktime.qts library responsible for parsing Kodak encoded images. A lack of proper error checking can result in a heap based buffer overflow leading to arbitrary code execution under the context of the currently logged in user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1241

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-04-03 - Coordinated public release of advisory
