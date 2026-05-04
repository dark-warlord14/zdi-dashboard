# ZDI-23-1529: Delta Electronics DIAEnergie HandlerUploadCarbon Use Of Hard-Coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1529
- **ZDI-CAN:** ZDI-CAN-18857
- **Date:** 2023-10-05
- **CVE:** CVE-2022-3214
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** DIAEnergie
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1529/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Delta Electronics DIAEnergie. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of requests to the HandlerUploadCarbon endpoint. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to bypass authentication and execute arbitrary code in the context of an administrator.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-22-256-03

## Disclosure Timeline

- 2023-04-28 - Vulnerability reported to vendor
- 2023-10-05 - Coordinated public release of advisory
