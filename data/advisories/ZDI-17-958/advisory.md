# ZDI-17-958: NetGain Systems Enterprise Manager restore.del_005fdo_jsp filenames Directory Traversal Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-958
- **ZDI-CAN:** ZDI-CAN-5104
- **Date:** 2017-12-13
- **CVE:** CVE-2017-16593
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-958/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of NetGain Systems Enterprise Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the org.apache.jsp.u.jsp.restore.del_005fdo_jsp servlet, which listens on TCP port 8081 by default. When parsing the filenames parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete any files accessible to the Administrator user.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-09-06 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
