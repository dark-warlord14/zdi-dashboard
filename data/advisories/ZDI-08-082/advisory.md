# ZDI-08-082: BMC PatrolAgent Version Logging Format String Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-082
- **ZDI-CAN:** ZDI-CAN-325
- **Date:** 2008-12-08
- **CVE:** CVE-2008-5982
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** BMC Software
- **Affected Products:** Patrol
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-082/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of BMC PatrolAgent. Authentication is not required to exploit this vulnerability. The specific flaw exists due to a format string handling error during log message writing. Supplying an invalid version number containing format string tokens to a vulnerable target on TCP port 3181 triggers an exploitable format string vulnerability which can result in arbitrary code execution.

## Additional Details

BMC has issued an update to correct this vulnerability. Customers should upgrade PATROL Agent to version 3.7.30

## Disclosure Timeline

- 2008-05-08 - Vulnerability reported to vendor
- 2008-12-08 - Coordinated public release of advisory
