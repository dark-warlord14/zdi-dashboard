# ZDI-21-190: Advantech iView NetworkServlet ztp_config_name SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-190
- **ZDI-CAN:** ZDI-CAN-12343
- **Date:** 2021-02-11
- **CVE:** CVE-2021-22654
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-190/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NetworkServlet class. When parsing the ztp_config_name parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-040-02

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-02-11 - Coordinated public release of advisory
