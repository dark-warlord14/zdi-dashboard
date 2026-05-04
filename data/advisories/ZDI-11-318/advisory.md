# ZDI-11-318: Novell Zenworks Software Packaging LaunchHelp.dll ActiveX Control LaunchProcess Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-318
- **ZDI-CAN:** ZDI-CAN-1204
- **Date:** 2011-11-07
- **CVE:** CVE-2011-2657
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-318/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Zenworks Software Packaging. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the function LaunchProcess exposed via the LaunchHelp.dll ActiveX Control (ProgID LaunchHelp.HelpLauncher.1). The first argument to LaunchProcess is a path to a command to execute, but the argument is not sanitized and is subject to directory traversal. This can be exploited to execute arbitrary commands on the user's system.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7009570&sliceId=1

## Disclosure Timeline

- 2011-07-20 - Vulnerability reported to vendor
- 2011-11-07 - Coordinated public release of advisory
