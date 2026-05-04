# ZDI-17-964: NetGain Systems Enterprise Manager misc.sample_jsp type Directory Traversal Arbitrary File Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-964
- **ZDI-CAN:** ZDI-CAN-5190
- **Date:** 2017-12-13
- **CVE:** CVE-2017-16599
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:C/A:C
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-964/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of NetGain Systems Enterprise Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the org.apache.jsp.u.jsp.reports.templates.misc.sample_jsp servlet, which listens on TCP port 8081 by default. When parsing the type parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of Administrator.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-09-06 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
