# ZDI-17-967: NetGain Systems Enterprise Manager tools.exec_jsp command Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-967
- **ZDI-CAN:** ZDI-CAN-5193
- **Date:** 2017-12-13
- **CVE:** CVE-2017-16602
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-967/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of NetGain Systems Enterprise Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the org.apache.jsp.u.jsp.tools.exec_jsp servlet, which listens on TCP port 8081 by default. When parsing the command parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code under the context of Administrator.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-09-08 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
