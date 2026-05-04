# ZDI-14-250: Advantech WebAccess Password Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-250
- **ZDI-CAN:** ZDI-CAN-2085
- **Date:** 2014-07-18
- **CVE:** CVE-2014-2366
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** Advantech WebAccess
- **Credit:** John Leitch
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-250/
## Vulnerability Details

This vulnerability allows remote attackers to disclose arbitrary credentials on vulnerable versions of Advantech WebAccess. Authentication is required to exploit this vulnerability. The specific flaw exists within the upAdminPg.asp component. An authenticated user can provide an arbitrary existing account name to this page and receive the account password. An attacker can leverage this vulnerability to then authenticate as the WebAccess Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: http://ics-cert.us-cert.gov/advisories/ICSA-14-198-02

## Disclosure Timeline

- 2014-04-23 - Vulnerability reported to vendor
- 2014-07-18 - Coordinated public release of advisory
