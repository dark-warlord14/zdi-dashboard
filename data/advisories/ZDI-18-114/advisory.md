# ZDI-18-114: Oracle WebLogic Remote Diagnosis Assistant Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-114
- **ZDI-CAN:** ZDI-CAN-5031
- **Date:** 2018-01-18
- **CVE:** CVE-2018-2617
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** WebLogic
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-114/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Oracle WebLogic Remote Diagnosis Server. The specific flaw exists within the Remote Diagnosis Assistant, which listens on TCP port 8888 when enabled. The issue results from unrestricted access to the log file which contains sensitive authentication information. An attacker can leverage this vulnerability to access the Remote Diagnosis Assistant under the context of admin.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpujan2018-3236628.html

## Disclosure Timeline

- 2017-07-19 - Vulnerability reported to vendor
- 2018-01-18 - Coordinated public release of advisory
