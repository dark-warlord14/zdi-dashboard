# ZDI-17-965: NetGain Systems Enterprise Manager network.traffic_005freport_jsp filename Directory Traversal Arbitrary File Overwrite Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-965
- **ZDI-CAN:** ZDI-CAN-5191
- **Date:** 2017-12-13
- **CVE:** CVE-2017-16600
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:N/I:P/A:C
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-965/
## Vulnerability Details

This vulnerability allows remote attackers to overwrite files on vulnerable installations of NetGain Systems Enterprise Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the org.apache.jsp.u.jsp.reports.templates.network.traffic_005freport_jsp servlet, which listens on TCP port 8081 by default. When parsing the filename parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to overwrite any files accessible to the Administrator.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-09-08 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
