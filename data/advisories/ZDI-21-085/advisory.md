# ZDI-21-085: Trend Micro ServerProtect splx_manual_scan Memory Exhaustion Denial-Of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-085
- **ZDI-CAN:** ZDI-CAN-11049
- **Date:** 2021-01-27
- **CVE:** CVE-2021-25224
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L
- **Affected Vendors:** Trend Micro
- **Affected Products:** ServerProtect
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-085/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro ServerProtect. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the splx_manual_scan executable. The issue results from the lack of proper validation of user-supplied data, which can result in a memory exhaustion condition. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000284207

## Disclosure Timeline

- 2020-07-16 - Vulnerability reported to vendor
- 2021-01-27 - Coordinated public release of advisory
