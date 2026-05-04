# ZDI-14-363: Panasonic Network Camera Recorder NcrCtl4.NcrNet.1 GetVOLHeader Arbitrary Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-363
- **ZDI-CAN:** ZDI-CAN-2171
- **Date:** 2014-10-14
- **CVE:** CVE-2014-8756
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Panasonic
- **Affected Products:** Network Camera Recorder
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-363/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Panasonic Network Camera Recorder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within then NcrCtl4.NcrNet.1 control. The GetVOLHeader method can be used to write null bytes to an arbitrary address. An attacker can leverage this to execute arbitrary code in the context of the browser.

## Additional Details

Panasonic has issued an update to correct this vulnerability. More details can be found at: http://panasonic.net/pcc/cgi-bin/products/netwkcam/download_us/tbookmarka_m.cgi?m=%20&mm=2010073014092324

## Disclosure Timeline

- 2014-06-09 - Vulnerability reported to vendor
- 2014-10-14 - Coordinated public release of advisory
