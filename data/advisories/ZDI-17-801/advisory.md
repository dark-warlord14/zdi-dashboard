# ZDI-17-801: Trend Micro Mobile Security for Enterprise eas_agent_command SlinkId SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-801
- **ZDI-CAN:** ZDI-CAN-4799
- **Date:** 2017-09-15
- **CVE:** CVE-2017-14078
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Mobile Security for Enterprise
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-801/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Mobile Security for Enterprise. Authentication is not required to exploit this vulnerability. The specific flaw exists within processing of the eas_agent_command action. When parsing the 'slink_id' field, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1118224

## Disclosure Timeline

- 2017-05-09 - Vulnerability reported to vendor
- 2017-09-15 - Coordinated public release of advisory
