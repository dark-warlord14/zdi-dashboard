# ZDI-17-961: NetGain Systems Enterprise Manager designer.script_005fsamples_jsp type Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-961
- **ZDI-CAN:** ZDI-CAN-5119
- **Date:** 2017-12-13
- **CVE:** CVE-2017-16596
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-961/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of NetGain Systems Enterprise Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the org.apache.jsp.u.jsp.designer.script_005fsamples_jsp servlet, which listens on TCP port 8081 by default. When parsing the type parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of Administrator.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-09-06 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
