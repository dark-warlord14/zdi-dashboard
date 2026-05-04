# ZDI-17-923: systemd Network Name Resolution Manager NSEC Resource Record Pseudo-Types Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-923
- **ZDI-CAN:** ZDI-CAN-5076
- **Date:** 2017-11-20
- **CVE:** CVE-2017-15908
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** systemd
- **Affected Products:** Network Name Resolution Manager
- **Credit:** Nelson William Gamazo Sanchez - Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-923/
## Vulnerability Details

This vulnerability allows remote attackers to cause a denial of service condition on vulnerable installations of systemd Network Name Resolution Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of NSEC resource records in systemd-resolved. The issue results from the lack of proper handling of the pseudo-types in the NSEC bitmap which causes an infinite loop. An attacker can leverage this vulnerability to trigger a denial of service condition for the system users.

## Additional Details

systemd has issued an update to correct this vulnerability. More details can be found at: https://people.canonical.com/~ubuntu-security/cve/2017/CVE-2017-15908.html

## Disclosure Timeline

- 2017-07-25 - Vulnerability reported to vendor
- 2017-11-20 - Coordinated public release of advisory
