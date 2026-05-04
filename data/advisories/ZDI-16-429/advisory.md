# ZDI-16-429: Advantech WebAccess upAdminPg Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-429
- **ZDI-CAN:** ZDI-CAN-3746
- **Date:** 2016-07-18
- **CVE:** CVE-2016-5810
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Zhou Yu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-429/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Advantech WebAccess. Authentication is required to exploit this vulnerability. The specific flaw exists within upAdminPg.asp. One project administrator can view other project administrators' passwords along with the system administrator's password. An attacker can leverage this vulnerability to escalate privileges within the system.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-173-01

## Disclosure Timeline

- 2016-05-11 - Vulnerability reported to vendor
- 2016-07-18 - Coordinated public release of advisory
