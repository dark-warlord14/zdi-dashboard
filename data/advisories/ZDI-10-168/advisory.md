# ZDI-10-168: Apple QuickTime ActiveX _Marshaled_pUnk Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-168
- **ZDI-CAN:** ZDI-CAN-823
- **Date:** 2010-08-31
- **CVE:** CVE-2010-1818
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** HBelite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-168/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the QTPlugin.ocx ActiveX control. The plugin accepts a parameter named _Marshaled_pUnk that it uses as a valid pointer. By specifying invalid values an attacker can force the application to jump to a controlled location in memory. This can be exploited to execute remote code under the context of the user running the web browser.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4339

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-08-31 - Coordinated public release of advisory
