# ZDI-21-087: Trend Micro ServerProtect vsapiapp Memory Exhaustion Denial-Of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-087
- **ZDI-CAN:** ZDI-CAN-11569
- **Date:** 2021-01-27
- **CVE:** CVE-2021-25226
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L
- **Affected Vendors:** Trend Micro
- **Affected Products:** ServerProtect
- **Credit:** Michael DePlante of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-087/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Trend Micro ServerProtect. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the vsapiapp executable. The issue results from the lack of proper validation of user-supplied data, which can result in a memory exhaustion condition. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000284207

## Disclosure Timeline

- 2020-07-22 - Vulnerability reported to vendor
- 2021-01-27 - Coordinated public release of advisory
