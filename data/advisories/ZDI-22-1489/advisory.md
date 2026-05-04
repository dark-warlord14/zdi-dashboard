# ZDI-22-1489: Delta Industrial Automation InfraSuite Device Master WriteConfiguration Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1489
- **ZDI-CAN:** ZDI-CAN-17640
- **Date:** 2022-10-27
- **CVE:** CVE-2022-41776
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1489/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Delta Industrial Automation InfraSuite Device Master. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WriteConfiguration function. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-298-07

## Disclosure Timeline

- 2022-06-17 - Vulnerability reported to vendor
- 2022-10-27 - Coordinated public release of advisory
