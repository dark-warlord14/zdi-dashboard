# ZDI-20-346: IBM Spectrum Protect Plus serveradmin Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-346
- **ZDI-CAN:** ZDI-CAN-9953
- **Date:** 2020-03-31
- **CVE:** CVE-2020-4208
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** IBM
- **Affected Products:** Spectrum Protect Plus
- **Credit:** KPC of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-346/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of IBM Spectrum Protect Plus. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Administrative Console Framework service. The service uses a hard-coded password as the current password while resetting the password of the serveradmin user. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www.ibm.com/support/pages/node/6114130

## Disclosure Timeline

- 2019-12-12 - Vulnerability reported to vendor
- 2020-03-31 - Coordinated public release of advisory
