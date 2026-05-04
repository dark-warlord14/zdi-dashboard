# ZDI-10-165: Trend Micro Internet Security Pro 2010 ActiveX extSetOwner Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-165
- **ZDI-CAN:** ZDI-CAN-824
- **Date:** 2010-08-25
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Internet Security Pro 2010
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-165/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Internet Security Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the UfPBCtrl.dll ActiveX control. The extSetOwner function accepts a parameter and assumes it is an initialized pointer. By specifying an invalid address, an attacker can force the process to call into a controlled memory region. This can be exploited to execute remote code under the context of the user invoking the browser.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: http://esupport.trendmicro.com/pages/Hot-Fix-UfPBCtrldll-is-vulnerable-to-remote-attackers.aspx

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-08-25 - Coordinated public release of advisory
