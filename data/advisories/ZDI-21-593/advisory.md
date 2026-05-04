# ZDI-21-593: Advantech BB-ESWGP506-2SFP-T Use of Hard-coded Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-593
- **ZDI-CAN:** ZDI-CAN-11786
- **Date:** 2021-05-25
- **CVE:** CVE-2021-22667
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** BB-ESWGP506-2SFP-T
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-593/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech BB-ESWGP506-2SFP-T industrial switches. Authentication is not required to exploit this vulnerability. The specific flaw exists within the telnet service, which listens on TCP port 23 by default. The service contains a hard-coded password for the administrator user account. An attacker can leverage this vulnerability to execute code in the context of the administrator user.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-054-02

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-05-25 - Coordinated public release of advisory
- 2021-05-25 - Advisory Updated
