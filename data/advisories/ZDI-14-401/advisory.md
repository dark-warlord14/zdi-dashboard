# ZDI-14-401: Samsung SmartViewer CNC_Ctrl ActiveX Control BackupToAvi Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-401
- **ZDI-CAN:** ZDI-CAN-2355
- **Date:** 2014-12-04
- **CVE:** CVE-2014-9265
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** SmartViewer
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-401/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung SmartViewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the BackupToAvi method. The issue lies in the failure to validate the size of the input buffer before copying it into a fixed-size buffer on the stack. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: http://www.samsungcctv.co.kr/product/product_view.asp?pagesize=8&sort=&dscYN=N&cid=45&clvl=1&page=1&idx=6276

## Disclosure Timeline

- 2014-07-28 - Vulnerability reported to vendor
- 2014-12-04 - Coordinated public release of advisory
