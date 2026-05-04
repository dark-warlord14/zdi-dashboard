# ZDI-12-169: GE Proficy Historian KeyHelp ActiveX LaunchTriPane Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-169
- **ZDI-CAN:** ZDI-CAN-1491
- **Date:** 2012-08-29
- **CVE:** CVE-2012-2516
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** GE
- **Affected Products:** Proficy Historian
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-169/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of GE Proficy Historian. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the KeyHelp.ocx ActiveX control. The control contains a LaunchTriPane function that allows launching of the HTML Help executable (hh.exe) with customized command line parameters. By using the -decompile switch, an attacker can specify the folder to decompile to and a UNC path to a specially crafted .chm file. The attacker can utilize this vulnerability to execute remote code under the context of the process.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: http://support.ge-ip.com/support/index?page=kbchannel&id=S:KB14863

## Disclosure Timeline

- 2012-01-24 - Vulnerability reported to vendor
- 2012-08-29 - Coordinated public release of advisory
