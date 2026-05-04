# ZDI-13-206: Hewlett-Packard LoadRunner LrWebIEBrowserMgr.dll ActiveX Control FlushSnapshotToFile Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-206
- **ZDI-CAN:** ZDI-CAN-1690
- **Date:** 2013-08-13
- **CVE:** CVE-2013-4797
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LoadRunner
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-206/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP LoadRunner. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the LrWebIEBrowserMgr.dll ActiveX control. The control exposes the FlushSnapshotToFile method. The method does not properly sanitize the destination path allowing for directory traversal. An attacker can leverage this vulnerability to write files and ultimately execute code under the context of the current user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03862772

## Disclosure Timeline

- 2013-01-22 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
