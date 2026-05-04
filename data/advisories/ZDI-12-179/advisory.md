# ZDI-12-179: EMC ApplicationXtender Desktop Viewer AEXView ActiveX AnnoSave Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-179
- **ZDI-CAN:** ZDI-CAN-1493
- **Date:** 2012-08-29
- **CVE:** CVE-2012-2289
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** EMC
- **Affected Products:** ApplicationXtender Workflow
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-179/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC ApplicationXtender. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AEXView.ocx ActiveX control. By manipulating a combination of the DisplayImageFile, AnnoLoad and AnnoSave methods, the vulnerable AnnoSave() method can enable an attacker to save arbitrary files in arbitrary locations. The attacker is able to control the file extension and the creation path via a directory traversal issue. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/523993/30/0/threaded

## Disclosure Timeline

- 2012-01-24 - Vulnerability reported to vendor
- 2012-08-29 - Coordinated public release of advisory
