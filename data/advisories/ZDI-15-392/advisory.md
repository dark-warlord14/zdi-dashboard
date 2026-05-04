# ZDI-15-392: Moxa VPort ActiveX SDK PLUS GetClientReg Name Parameter Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-392
- **ZDI-CAN:** ZDI-CAN-2525
- **Date:** 2015-08-13
- **CVE:** CVE-2015-0986
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Moxa
- **Affected Products:** VPort ActiveX SDK PLUS
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-392/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of VPort ActiveX SDK PLUS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the VPORTSDK.VPortSDKCtrl.1 ActiveX control. By passing an overly long string to the GetClientReg method's Name parameter, an attacker can overflow a buffer on the stack. This vulnerability could be used to execute arbitrary code in the context of the browser.

## Additional Details

Moxa has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-097-01

## Disclosure Timeline

- 2015-02-05 - Vulnerability reported to vendor
- 2015-08-13 - Coordinated public release of advisory
