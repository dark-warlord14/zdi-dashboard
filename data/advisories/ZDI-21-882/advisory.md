# ZDI-21-882: Oracle Business Intelligence SchedulerConfigPage11g JNDI Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-882
- **ZDI-CAN:** ZDI-CAN-13105
- **Date:** 2021-07-22
- **CVE:** CVE-2021-2391
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** Business Intelligence
- **Credit:** Quynh Le of VNPT ISC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-882/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle Business Intelligence. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of the SchedulerConfigPage11g class. The issue results from the lack of proper validation of user-supplied data, which can result in execution of arbitrary Java code. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2021.html

## Disclosure Timeline

- 2021-03-12 - Vulnerability reported to vendor
- 2021-07-22 - Coordinated public release of advisory
