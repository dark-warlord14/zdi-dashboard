# ZDI-22-891: Advantech iView findSummaryUpdateDeviceListExport VALUE SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-891
- **ZDI-CAN:** ZDI-CAN-16564
- **Date:** 2022-06-30
- **CVE:** CVE-2022-2135
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** @rgod777
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-891/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NetworkServlet endpoint, which listens on TCP port 8080 by default. When parsing the VALUE element of the findSummaryUpdateDeviceListExport action, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-179-03

## Disclosure Timeline

- 2022-03-02 - Vulnerability reported to vendor
- 2022-06-30 - Coordinated public release of advisory
