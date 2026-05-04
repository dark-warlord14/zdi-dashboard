# ZDI-07-040: Symantec AntiVirus Engine CAB Parsing Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-040
- **ZDI-CAN:** ZDI-CAN-124
- **Date:** 2007-07-12
- **CVE:** CVE-2007-0447
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec
- **Affected Products:** Symantec AntiVirus Engine
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-040/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with affected installations of Symantec's AntiVirus Engine. User interaction is not required to exploit this vulnerability. The specific flaw exists during the process of scanning multiple maliciously formatted CAB archives. The parsing routine implicitly trusts certain user-supplied values that can result in an exploitable heap corruption.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/avcenter/security/Content/2007.07.11f.html

## Disclosure Timeline

- 2006-11-09 - Vulnerability reported to vendor
- 2007-07-12 - Coordinated public release of advisory
