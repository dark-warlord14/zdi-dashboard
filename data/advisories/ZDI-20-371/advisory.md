# ZDI-20-371: Schneider Electric IGSS IGSSupdateservice Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-371
- **ZDI-CAN:** ZDI-CAN-9757
- **Date:** 2020-04-03
- **CVE:** CVE-2020-7478
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IGSS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-371/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Schneider Electric IGSS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IGSSupdateservice service, which listens on TCP port 12414 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose files in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-084-02

## Disclosure Timeline

- 2019-12-11 - Vulnerability reported to vendor
- 2020-04-03 - Coordinated public release of advisory
