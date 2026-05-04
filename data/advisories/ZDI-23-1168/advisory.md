# ZDI-23-1168: Zabbix Web Service Report Generation External Control of File Name Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1168
- **ZDI-CAN:** ZDI-CAN-18532
- **Date:** 2023-08-23
- **CVE:** CVE-2022-46768
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Zabbix
- **Affected Products:** Zabbix
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1168/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Zabbix Web Service. Authentication is not required to exploit this vulnerability. The specific flaw exists within PDF report generation. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Zabbix has issued an update to correct this vulnerability. More details can be found at: https://support.zabbix.com/browse/ZBX-22087

## Disclosure Timeline

- 2022-09-20 - Vulnerability reported to vendor
- 2023-08-23 - Coordinated public release of advisory
