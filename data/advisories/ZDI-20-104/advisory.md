# ZDI-20-104: Cisco Data Center Network Manager getSanSwitchDataLength SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-104
- **ZDI-CAN:** ZDI-CAN-9342
- **Date:** 2020-01-03
- **CVE:** CVE-2019-15984
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-104/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Cisco Data Center Network Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of requests to the getSwitchsDataLength endpoint of the DbInventoryWS service. When parsing the colFilterStr parameter in the getSanSwitchDataLength method, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker could leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20200102-dcnm-sql-inject

## Disclosure Timeline

- 2019-09-27 - Vulnerability reported to vendor
- 2020-01-03 - Coordinated public release of advisory
