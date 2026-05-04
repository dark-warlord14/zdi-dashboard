# ZDI-10-113: Mozilla Firefox XSLT Sort Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-113
- **ZDI-CAN:** ZDI-CAN-747
- **Date:** 2010-06-23
- **CVE:** CVE-2010-1199
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** Martin Barbella
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-113/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or otherwise render a malicious file. The specific flaw exists within a particular XSLT transformation when applied to an XML document. If a large number of elements have this transformation applied to them, the application will misallocate a buffer. Upon usage of this buffer the application will copy more data than allocated thus causing an overflow. This can lead to code execution under the context of the application.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-30.html

## Disclosure Timeline

- 2010-03-22 - Vulnerability reported to vendor
- 2010-06-23 - Coordinated public release of advisory
