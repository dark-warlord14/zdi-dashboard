# ZDI-13-253: ABB RobotStudio Tools CWGraph3D ActiveX Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-253
- **ZDI-CAN:** ZDI-CAN-1834
- **Date:** 2013-11-24
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** ABB
- **Affected Products:** RobotStudio
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-253/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ABB RobotStudio Tools. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the cw3dgrph.ocx ActiveX control. The ImportStyle method allows an attacker to load a specially crafted .cwx file from a remote network share. Following this call, the attacker can invoke the ExportStyle method to save the file to an arbitrary location through the use of a directory traversal vulnerability. A remote attacker can abuse this to execute arbitrary code under the context of the user.

## Additional Details

ABB has issued an update to correct this vulnerability. More details can be found at: http://www05.abb.com/global/scot/scot348.nsf/veritydisplay/8e134e13bfa25a0cc1257c0600459b16/$file/SI10253A2%20rev%200%20.pdf

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
