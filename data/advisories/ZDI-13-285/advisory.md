# ZDI-13-285: IBM Rational Focal Point RequestAccessController Servlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-285
- **ZDI-CAN:** ZDI-CAN-1949
- **Date:** 2013-12-20
- **CVE:** CVE-2013-5398
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** IBM
- **Affected Products:** Rational Focal Point
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-285/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Rational Focal Point. Authentication is not required to exploit this vulnerability. The specific flaw exists within com.telelogic.focalpoint.pres.controller.RequestAccessController servlet which contains a file disclosure vulnerability in the file variable. A remote attacker could gain access to configuration files which could lead to remote code execution in the context of the process.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21654471

## Disclosure Timeline

- 2013-09-04 - Vulnerability reported to vendor
- 2013-12-20 - Coordinated public release of advisory
