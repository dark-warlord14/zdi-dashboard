# ZDI-14-017: IBM Platform Symphony DE Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-017
- **ZDI-CAN:** ZDI-CAN-1969
- **Date:** 2014-02-13
- **CVE:** CVE-2013-5387
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** Platform Symphony DE
- **Credit:** AbdulAziz Hariri HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-017/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Platform Symphony DE. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the way SOAP requests are handled. A malformed SOAP request would overwrite a statically sized buffer that could allow remote code execution in the context of the process.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=isg3T1020072

## Disclosure Timeline

- 2013-09-04 - Vulnerability reported to vendor
- 2014-02-13 - Coordinated public release of advisory
