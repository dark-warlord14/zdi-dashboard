# ZDI-07-013: Kaspersky AntiVirus Engine ARJ Archive Parsing Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-013
- **ZDI-CAN:** ZDI-CAN-113
- **Date:** 2007-04-05
- **CVE:** CVE-2007-0445
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Kaspersky
- **Affected Products:** Anti-Virus
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-013/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with affected installations of the Kaspersky Anti-Virus Engine. User interaction is not required to exploit this vulnerability. The specific flaw exists in the engine's handling of the ARJ archive format. The Kaspersky engine copies data from scanned archives into an unchecked heap-based buffer. This results in heap corruption when a malformed ARJ archive is processed by an application that utilizes the engine. This corruption can be exploited to execute arbitrary code.

## Additional Details

Kaspersky has issued an update to correct this vulnerability. More details can be found at: http://www.kaspersky.com/technews?id=203038693

## Disclosure Timeline

- 2006-11-09 - Vulnerability reported to vendor
- 2007-04-05 - Coordinated public release of advisory
