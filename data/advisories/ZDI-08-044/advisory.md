# ZDI-08-044: Mozilla Firefox CSSValue Array Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-044
- **ZDI-CAN:** ZDI-CAN-349
- **Date:** 2008-07-17
- **CVE:** CVE-2008-2785
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Mozilla Firefox, Mozilla Firefox
- **Affected Products:** 2.0.x, 3.0.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-044/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the browser's handling reference counters to the nsCSSValue:Array class. Creating more then 65,535 references will overflow a 16-bit reference counter and therefore result in an erroneous free() while the object still exists. Properly manipulated this can result in arbitrary code execution under the context of the current user.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2008/mfsa2008-34.html

## Disclosure Timeline

- 2008-06-17 - Vulnerability reported to vendor
- 2008-07-17 - Coordinated public release of advisory
