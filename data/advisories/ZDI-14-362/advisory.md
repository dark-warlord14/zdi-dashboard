# ZDI-14-362: Foxit ActiveX Pro SDK SetLogFile Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-362
- **ZDI-CAN:** ZDI-CAN-2490
- **Date:** 2014-10-14
- **CVE:** CVE-2014-8074
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** ActiveX Pro SDK
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-362/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Foxit ActiveX Pro SDK ActiveX control. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Foxit.FoxitPDFSDKProCtrl.5 ActiveX control. By passing an overly long string to the SetLogFile method, an attacker is able to overflow global variables in the control. This could be used to execute arbitrary code in the context of the browser.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: http://www.foxitsoftware.com/support/security_bulletins.php

## Disclosure Timeline

- 2014-09-05 - Vulnerability reported to vendor
- 2014-10-14 - Coordinated public release of advisory
