# ZDI-17-968: NetGain Systems Enterprise Manager settings.upload_005ffile_005fdo_jsp filename Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-968
- **ZDI-CAN:** ZDI-CAN-5194
- **Date:** 2017-12-13
- **CVE:** CVE-2017-16603
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-968/
## Vulnerability Details

This vulnerability allows remote attackers to execute code by creating arbitrary files on vulnerable installations of NetGain Systems Enterprise Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the org.apache.jsp.u.jsp.settings.upload_005ffile_005fdo_jsp servlet, which listens on TCP port 8081 by default. When parsing the filename parameter, the process does not properly validate user-supplied data, which can allow for the upload of files. An attacker can leverage this vulnerability to execute code under the context of Administrator.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-09-08 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
