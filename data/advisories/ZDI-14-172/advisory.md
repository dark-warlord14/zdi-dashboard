# ZDI-14-172: Samsung iPOLiS Device Manager XNSSDKDEVICE.XnsSdkDeviceCtrlForIpInstaller.1 Multiple Methods Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-172
- **ZDI-CAN:** ZDI-CAN-2320
- **Date:** 2014-06-04
- **CVE:** CVE-2014-3911
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** iPOLiS Device Manager
- **Credit:** Ariele Caltabiano (kimiya) and Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-172/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung iPOLiS Device Manager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the XNSSDKDEVICE.XnsSdkDeviceCtrlForIpInstaller.1 ActiveX control. By providing a malicious value to any of a number of vulnerable methods, an attacker can execute arbitrary code in the context of the browser.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: http://www.samsungsecurity.com/support/online_tool.asp

## Disclosure Timeline

- 2014-05-06 - Vulnerability reported to vendor
- 2014-06-04 - Coordinated public release of advisory
