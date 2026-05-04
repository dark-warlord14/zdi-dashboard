# ZDI-21-607: Synology DiskStation Manager webapi CRLF Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-607
- **ZDI-CAN:** ZDI-CAN-12460
- **Date:** 2021-05-25
- **CVE:** CVE-2021-29084
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation Manager
- **Credit:** Justin Taft (@oneupsecurity)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-607/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Synology DS418play. Authentication is not required to exploit this vulnerability. The specific flaw exists within the webapi component. The issue results from incorrect neutralization of CRLF sequences in HTTP requests. An attacker can leverage this vulnerability to disclose information in the context of the Admin user.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-uk/security/advisory/Synology_SA_20_26

## Disclosure Timeline

- 2021-01-19 - Vulnerability reported to vendor
- 2021-05-25 - Coordinated public release of advisory
