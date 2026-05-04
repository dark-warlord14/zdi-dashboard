# ZDI-26-049: Delta Electronics DIAView Exposed Dangerous Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-049
- **ZDI-CAN:** ZDI-CAN-27093
- **Date:** 2026-01-28
- **CVE:** CVE-2026-0975
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** DIAView
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-049/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics DIAView. User interaction is required to exploit this vulnerability in that the target must open and run a malicious project. The specific flaw exists within the DIAView script component. The issue results from the lack of restrictions on script in DIAView projects. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-26-022-07

## Disclosure Timeline

- 2025-06-09 - Vulnerability reported to vendor
- 2026-01-28 - Coordinated public release of advisory
- 2026-01-28 - Advisory Updated
