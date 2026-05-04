# ZDI-26-094: Schneider Electric EcoStruxure Power Build SSD File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-094
- **ZDI-CAN:** ZDI-CAN-27478
- **Date:** 2026-02-12
- **CVE:** CVE-2025-13845
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure Power Build
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-094/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric EcoStruxure Power Build. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SSD files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-26-015-10

## Disclosure Timeline

- 2025-08-14 - Vulnerability reported to vendor
- 2026-02-12 - Coordinated public release of advisory
- 2026-02-12 - Advisory Updated
