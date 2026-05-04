# ZDI-25-215: (Pwn2Own) Synology DiskStation DS1823xs+ LDAP Client Improper Certificate Validation Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-215
- **ZDI-CAN:** ZDI-CAN-25487
- **Date:** 2025-04-09
- **CVE:** CVE-2024-10444
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** DiskStation DS1823xs+
- **Credit:** Chris Anastasio @mufinnnnnnn & Fabius Watson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-215/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Synology DiskStation DS1823xs+ devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of LDAP queries. The issue results from the lack of proper validation of the certificate presented by the LDAP server. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-us/security/advisory/Synology_SA_25_01

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
