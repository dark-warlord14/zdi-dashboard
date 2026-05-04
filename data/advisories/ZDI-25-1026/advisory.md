# ZDI-25-1026: Appleton UPSMON-PRO UPSMONProService Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1026
- **ZDI-CAN:** ZDI-CAN-24122
- **Date:** 2025-11-27
- **CVE:** CVE-2024-3871
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Appleton
- **Affected Products:** UPSMON-PRO
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1026/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Appleton UPSMON-PRO. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UPSMONProService service, which listens on UDP port 2601 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Appleton has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-324-06

## Disclosure Timeline

- 2024-12-19 - Vulnerability reported to vendor
- 2025-11-27 - Coordinated public release of advisory
- 2025-11-27 - Advisory Updated
