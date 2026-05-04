# ZDI-25-877: Delta Electronics ISPSoft ISP File Parsing Improper Control of Dynamically-Managed Code Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-877
- **ZDI-CAN:** ZDI-CAN-25875
- **Date:** 2025-08-28
- **CVE:** CVE-2025-53419
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** ISPSoft
- **Credit:** Guillaume Orlando
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-877/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics ISPSoft. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ISP files. The issue results from insufficient restriction of dynamically-managed code. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-240-05

## Disclosure Timeline

- 2025-05-22 - Vulnerability reported to vendor
- 2025-08-28 - Coordinated public release of advisory
- 2025-08-28 - Advisory Updated
