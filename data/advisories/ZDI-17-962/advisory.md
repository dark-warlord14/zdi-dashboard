# ZDI-17-962: NetGain Systems Enterprise Manager TFtpServer Filename Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-962
- **ZDI-CAN:** ZDI-CAN-5137
- **Date:** 2017-12-13
- **CVE:** CVE-2017-16597
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-962/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of NetGain Systems Enterprise Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of WRQ requests. When parsing the Filename field, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code under the context of Administrator.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-09-08 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
