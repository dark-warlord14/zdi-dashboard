# ZDI-22-1486: Delta Industrial Automation InfraSuite Device Master ModifyPrivByID Missing Authentication Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1486
- **ZDI-CAN:** ZDI-CAN-17681
- **Date:** 2022-10-27
- **CVE:** CVE-2022-41644
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1486/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges or create a denial-of-service condition on affected installations of Delta Industrial Automation InfraSuite Device Master. Authentication is not required to create a denial-of-service condition. Authentication is required to achieve privilege escalation. The specific flaw exists within the ModifyPrivByID function. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user or to create a denial-of-service condition on system.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-298-07

## Disclosure Timeline

- 2022-06-22 - Vulnerability reported to vendor
- 2022-10-27 - Coordinated public release of advisory
