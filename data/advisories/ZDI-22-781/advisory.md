# ZDI-22-781: Ivanti Avalanche EnterpriseServer Service SQL Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-781
- **ZDI-CAN:** ZDI-CAN-15333
- **Date:** 2022-05-26
- **CVE:** CVE-2022-36976
- **CVSS:** 9.1
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-781/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Ivanti Avalanche. The specific flaw exists within the GroupDaoImpl class. A crafted request can trigger execution of SQL queries composed from a user-supplied string. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://download.wavelink.com/Files/avalanche_v6.3.4_release_notes.txt

## Disclosure Timeline

- 2021-10-22 - Vulnerability reported to vendor
- 2022-05-26 - Coordinated public release of advisory
- 2022-07-27 - Advisory Updated
