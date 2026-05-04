# ZDI-25-1037: Emerson Movicon RTUSERS File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1037
- **ZDI-CAN:** ZDI-CAN-27649
- **Date:** 2025-12-01
- **CVE:** CVE-2024-3871
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Emerson
- **Affected Products:** Movicon
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1037/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Emerson Movicon. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of RTUSERS files within the editusr component. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Emerson has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-324-06

## Disclosure Timeline

- 2025-09-11 - Vulnerability reported to vendor
- 2025-12-01 - Coordinated public release of advisory
- 2025-12-01 - Advisory Updated
