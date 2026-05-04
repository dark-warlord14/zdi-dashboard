# ZDI-13-182: Hewlett-Packard LoadRunner lrFileIOService ActiveX Control WriteFileBinary Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-182
- **ZDI-CAN:** ZDI-CAN-1671
- **Date:** 2013-07-26
- **CVE:** CVE-2013-2370
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LoadRunner
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-182/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP LoadRunner. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the lrFileIOService ActiveX control. The control exposes the WriteFileBinary method which accepts a parameter named data that it uses as a valid pointer. By specifying invalid values an attacker can force the application to jump to a controlled location in memory. This can be exploited to execute remote code under the context of the user running the web browser.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03862772

## Disclosure Timeline

- 2013-01-22 - Vulnerability reported to vendor
- 2013-07-26 - Coordinated public release of advisory
