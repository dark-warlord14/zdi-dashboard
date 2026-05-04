# ZDI-10-290: SAP NetWeaver Business Client SapThemeRepository ActiveX Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-290
- **ZDI-CAN:** ZDI-CAN-939
- **Date:** 2010-12-14
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** SAP
- **Affected Products:** NetWeaver
- **Credit:** Alexandr Polyakov, Alexey Sintsov from Digital Security Research Group
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-290/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP NetWeaver Business Client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Load and LoadTheme methods of the SapThemeRepository ActiveX control (sapwdpcd.dll) implemented by SAP NetWeaver Business Client. Due to a failure in bounds checking, a user-supplied parameter supplied to the vulnerable methods can overflow a stack buffer resulting in arbitrary code execution under the context of the user running the browser.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://service.sap.com/sap/support/notes/1519966

## Disclosure Timeline

- 2010-09-30 - Vulnerability reported to vendor
- 2010-12-14 - Coordinated public release of advisory
