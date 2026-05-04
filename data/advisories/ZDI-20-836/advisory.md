# ZDI-20-836: Advantech iView DeviceTreeTable updateNamingData SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-836
- **ZDI-CAN:** ZDI-CAN-10656
- **Date:** 2020-07-16
- **CVE:** CVE-2020-14497
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-836/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the updateNamingData method of the DeviceTreeTable class. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-196-33

## Disclosure Timeline

- 2020-04-24 - Vulnerability reported to vendor
- 2020-07-16 - Coordinated public release of advisory
