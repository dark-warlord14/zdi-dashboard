# ZDI-14-400: Samsung SmartViewer STWConfig ActiveX Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-400
- **ZDI-CAN:** ZDI-CAN-2413
- **Date:** 2014-12-04
- **CVE:** CVE-2014-9266
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** SmartViewer
- **Credit:** Carlo Di Dato
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-400/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samsung SmartViewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the STWConfig ActiveX control. The issue lies in the failure to initialize a variable prior to using it. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: http://www.samsungcctv.co.kr/product/product_view.asp?pagesize=8&sort=&dscYN=N&cid=45&clvl=1&page=1&idx=6276

## Disclosure Timeline

- 2014-07-28 - Vulnerability reported to vendor
- 2014-12-04 - Coordinated public release of advisory
