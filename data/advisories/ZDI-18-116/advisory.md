# ZDI-18-116: Oracle WebLogic Remote Diagnosis Assistant rda_tfa_hrs Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-116
- **ZDI-CAN:** ZDI-CAN-5033
- **Date:** 2018-01-18
- **CVE:** CVE-2018-2616
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:M/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** WebLogic
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-116/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle WebLogic. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the processing of the rda_tfa_hrs command in the Remote Diagnosis Assistant. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code under the context of Administrator.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpujan2018-3236628.html

## Disclosure Timeline

- 2017-07-19 - Vulnerability reported to vendor
- 2018-01-18 - Coordinated public release of advisory
