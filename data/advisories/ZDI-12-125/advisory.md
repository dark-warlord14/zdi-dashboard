# ZDI-12-125: Apple Quicktime QTPlugin SetLanguage Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-125
- **ZDI-CAN:** ZDI-CAN-1398
- **Date:** 2012-07-12
- **CVE:** CVE-2012-0666
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** CHkr_D591
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-125/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Quicktime.qts. The stack buffer overflow occurs as a result of an unbounded string copy function in Quicktime.qts, reachable through the IQTPluginControl::SetLanguage COM method exposed by the COM object QTPlugin.ocx. This vulnerability can be leveraged to execute code under the context of the user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-07-12 - Coordinated public release of advisory
