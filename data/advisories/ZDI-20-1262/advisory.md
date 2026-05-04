# ZDI-20-1262: Advantech R-SeeNet device_position device_id SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1262
- **ZDI-CAN:** ZDI-CAN-11373
- **Date:** 2020-10-19
- **CVE:** CVE-2020-25157
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** R-SeeNet
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1262/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech R-SeeNet. Authentication is not required to exploit this vulnerability. The specific flaw exists within device_position.php. When parsing the device_id parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-289-02

## Disclosure Timeline

- 2020-07-07 - Vulnerability reported to vendor
- 2020-10-19 - Coordinated public release of advisory
