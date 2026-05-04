# ZDI-20-038: Cisco Data Center Network Manager getLanSwitchList SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-038
- **ZDI-CAN:** ZDI-CAN-9182
- **Date:** 2020-01-03
- **CVE:** CVE-2019-15984
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-038/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco Data Center Network Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the processing of requests to the DbInventoryWSService/DbInventoryWS service. When parsing a packet to the getSwitchListWithPortUse SOAP endpoint, the process does not properly validate a user-supplied string for the sortType parameter before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20200102-dcnm-sql-inject

## Disclosure Timeline

- 2019-08-29 - Vulnerability reported to vendor
- 2020-01-03 - Coordinated public release of advisory
