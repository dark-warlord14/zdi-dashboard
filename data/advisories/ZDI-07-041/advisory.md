# ZDI-07-041: Panda Software AdminSecure Agent Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-041
- **ZDI-CAN:** ZDI-CAN-127
- **Date:** 2007-07-20
- **CVE:** CVE-2007-3026
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Panda Software
- **Affected Products:** AdminSecure
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-041/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Panda AdminSecure. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AdminSecure agent which binds by default to TCP port 19226 or 19227. When processing traffic on the listening port, the agent trusts a user-supplied length value for a memory allocation. Specific size values can result in an integer overflow and subsequently insufficient allocation size. This results in a heap-based buffer overflow that can be leverage to execute arbitrary code.

## Additional Details

Panda Software has issued an update to correct this vulnerability. More details can be found at: http://www.pandasoftware.com/Download/tree/

## Disclosure Timeline

- 2006-11-15 - Vulnerability reported to vendor
- 2007-07-20 - Coordinated public release of advisory
