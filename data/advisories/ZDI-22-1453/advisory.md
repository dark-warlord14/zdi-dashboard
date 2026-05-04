# ZDI-22-1453: Delta Industrial Automation DIAEnergie Use Of Hard-Coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1453
- **ZDI-CAN:** ZDI-CAN-16858
- **Date:** 2022-10-21
- **CVE:** CVE-2022-3214
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** DIAEnergie
- **Credit:** Y4er
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1453/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Delta Industrial Automation DIAEnergie. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of requests to the web service. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-256-03

## Disclosure Timeline

- 2022-06-17 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
