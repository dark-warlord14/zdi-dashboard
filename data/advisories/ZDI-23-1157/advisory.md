# ZDI-23-1157: Advantech R-SeeNet device_status Local File Inclusion Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1157
- **ZDI-CAN:** ZDI-CAN-19579
- **Date:** 2023-08-21
- **CVE:** CVE-2023-3256
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** R-SeeNet
- **Credit:** Esjay (@esj4y)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1157/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Advantech R-SeeNet. Authentication is required to exploit this vulnerability. The specific flaw exists within the device_status page. The issue results from the lack of proper validation of user-supplied data prior to passing it to a PHP include function. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-173-02

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-08-21 - Coordinated public release of advisory
